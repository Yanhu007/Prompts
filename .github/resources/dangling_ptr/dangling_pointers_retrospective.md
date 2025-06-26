# Dangling Pointers Retrospective

**Author:** Arthur Sonzogni  
**Visibility:** Public  
**Status:** Current  
**Date:** Nov 15, 2022  
**URL:** https://docs.google.com/document/d/11YYsyPF9rQv_QFf982Khie3YuNPXV0NdhzJPojpZfco/edit

## Overview

To get a better understanding of what it means to fix dangling pointers, 128 patches made so far have been classified into several categories. Those patches fix 179 dangling pointers. The raw data and list of patches can be found in the original document. A public copy of the list of patches (for non-alphabet employees) can be found there as well.

> **Note:** This is about the *fixed* dangling pointers. It means the numbers are biased, because the difficult ones have likely been skipped.

## Summary

### Remove Pointer (24%)
- **14.6%** - use `unique_ptr`
- **3.13%** - use `weak_ptr`
- **2.34%** - use function call
- **1.56%** - use object composition
- **Other** - `scoped_refptr`, `RenderFrameHost` ID, etc.

### Fix Ordering (25%)
- **20.31%** - fix member declaration order
- **4.7%** - fix reset ordering

### Reset Pointer (39%)
- **10.9%** - derived from object about to be deleted
- **10.16%** - self deleting object
- **3.9%** - observer callback
- **3.9%** - destroy object owned elsewhere
- **3.13%** - pointer vended from C API

### Other (10%)
- Various other solutions

## Categories

### Use `unique_ptr` (14.6%)

**Example CLs:**
- [Example CL 1 - Generic](#)
- [Example CL 2 - Using base::ScopedFile to wrap a C API](#)
- [Example CL 3 - Object conditionally owned](#)

When a pointer represents ownership over an object, prefer using `std::unique_ptr` over using `new`/`delete`. It guarantees the pointer to be reset after the referenced object has been freed. Most of the time, because of RAII, it also simplifies code, because the object is now guaranteed to be automatically freed at the end of the pointer lifetime.

This is the **strongly encouraged solution**. See [developer guide](#).

#### Before / After Example

| Before | After |
|--------|-------|
| ```cpp<br>class A {<br> public:<br>  void CreateB() { b_ = new B; }<br><br>  ~A() {<br>    if (b_)<br>      delete b_; // |b_| is left dangling<br>  }<br><br> private:<br>  raw_ptr<B, DanglingUntriaged> b_;<br>};<br>``` | ```cpp<br>class A {<br> public:<br>  void CreateB() { b_ = std::make_unique<B>(); }<br><br> private:<br>  std::unique_ptr<B> b_;<br>};<br>``` |

### Use `weak_ptr` (3.13%)

**Example CL:** [Link](#)

It can be challenging to deal with an object's lifespan. When an object needs to be safely accessed by one or more objects other than its owner and those callers are able to deal with the object disappearing, weak pointers can be useful.

Another use for `WeakPtr` is to break reference cycles formed by `scoped_ptr`. Compared to a raw pointer, it ensures the pointer is not used after free during the cycle destruction.

### Use Function Call (2.34%)

**Example CL:** [Link](#)

Sometimes, more pointers are created than necessary. There are other ways to access the object being referenced, such as invoking a function. This could be due to historical factors (such as the fact that it was once necessary) or premature optimization (e.g. to avoid indirections).

In some cases, the lifetime of the referenced object is shorter than the one of the pointer and it isn't always safe to use the pointer. Removing the pointer for using the function reduces the amount of states to manage, and allows the callee to enforce some preconditions.

#### Before / After Example

| Before | After |
|--------|-------|
| ```cpp<br>class A {<br> public:<br>  A() : b_(GetCurrentB()) = default;<br><br>  void Action() {<br>    b_->Action();<br>  }<br><br> private:<br>  raw_ptr<B, DanglingUntriaged> b_;<br>};<br>``` | ```cpp<br>class A {<br> public:<br>  void Action() {<br>    GetCurrentB()->Action();<br>  }<br>};<br>``` |

### Use Object Composition (1.56%)

**Example CL:** [Link](#)

In some cases, a raw pointer could almost be a `std::unique_ptr`. However, the `unique_ptr` is (often) implemented to return `nullptr` while executing the destructor of the referenced object. This could be an issue, when the referenced object needs to access the pointer during the destruction.

In some cases, the choice was to remove the pointer, and use direct object composition:

#### Before / After Example

| Before | After |
|--------|-------|
| ```cpp<br>class Tree {<br> public:<br>  Tree() {<br>    root_ = new Node();<br>  }<br><br>  ~Tree() {<br>    delete root_;<br>  }<br><br>  Node* root() { return root_; }<br><br> private:<br>  // This is an owned ptr to the root<br>  // Node. It is not a unique_ptr,<br>  // because we need the pointer to<br>  // remain valid, even while the Node<br>  // is being destroyed, since it is<br>  // common for a node to test whether<br>  // it is the root node.<br>  raw_ptr<Node, DanglingUntriaged> root_;<br>};<br><br>class Node {<br> public:<br>  Node(Tree* tree) : tree_(tree);<br>  bool IsRoot() { return tree_->root() == this; }<br> private:<br>  Tree* tree_;<br>};<br>``` | ```cpp<br>class Tree {<br> public:<br>  const Node* root() const { return &root_; }<br><br> private:<br>  Node root_;<br>};<br><br>class Node {<br> public:<br>  Node(Tree* tree) : tree_(tree);<br>  bool IsRoot() { return tree_->root() == this; }<br> private:<br>  Tree* tree_;<br>};<br>``` |

### Fix Member Declaration Order (20.3%)

**Example CL:** [Link](#)

In a class, dependent objects are sometimes declared in the incorrect order. When one class depends on the second, it must be declared last, so that it is destroyed first. If you don't, then the second class might use its dependency after free during its destructor.

#### Before / After Example

| Before | After |
|--------|-------|
| ```cpp<br>class A {<br> public:<br>  void Action() {<br>    b_ = std::make_unique<B>();<br>    c_ = std::make_unique<C>(b_.get());<br>  }<br><br> private:<br>  std::unique_ptr<C> c_;<br>  std::unique_ptr<B> b_;<br>};<br><br>class C {<br> public:<br>  C(B* b) : b_(b) = default;<br><br> private:<br>  raw_ptr<B, DanglingUntriaged> b_;<br>};<br>``` | ```cpp<br>class A {<br> public:<br>  void Action() {<br>    b_ = std::make_unique<B>();<br>    c_ = std::make_unique<C>(b_.get());<br>  }<br><br> private:<br>  std::unique_ptr<B> b_;<br>  std::unique_ptr<C> c_; // Depends on |b_|<br>};<br><br>class C {<br> public:<br>  C(B* b) : b_(b) = default;<br><br> private:<br>  raw_ptr<B> b_;<br>};<br>``` |

### Fix Reset Ordering (4.7%)

**Example CL:** [Link](#)

This is similar to "Fix member declaration order", but happens when two dependent objects are destroyed manually in the wrong order. Risk is the dependent object to use its dependencies after it has been freed.

#### Before / After Example

| Before | After |
|--------|-------|
| ```cpp<br>class A {<br> public:<br>  void Setup() {<br>    c_ = std::make_unique<C>();<br>    b_ = std::make_unique<B>(c_.get());<br>  }<br><br>  void TearDown() {<br>    c_.reset(); // B::c_ is dangling<br>    b_.reset();<br>  }<br><br> private:<br>  std::unique_ptr<B> b_;<br>  std::unique_ptr<C> c_;<br>};<br><br>class B {<br> public:<br>  B(C* c) : c_(c) = default;<br> private:<br>  raw_ptr<C, DanglingUntriaged> c_;<br>};<br>``` | ```cpp<br>class A {<br> public:<br>  void Setup() {<br>    c_ = std::make_unique<C>();<br>    b_ = std::make_unique<B>(c_.get());<br>  }<br><br>  void TearDown() {<br>    b_.reset(); // Depends on |c_|. Delete first.<br>    c_.reset();<br>  }<br><br> private:<br>  std::unique_ptr<B> b_;<br>  std::unique_ptr<C> c_;<br>};<br><br>class B {<br> public:<br>  B(C* c) : c_(c) = default;<br> private:<br>  raw_ptr<C> c_;<br>};<br>``` |

### Reset Pointer Derived From Object About to be Deleted (4.6%)

**Example CL:** [Link](#)

To avoid keeping a dangling pointer, it must be reset when the object from which it was derived is about to be deleted.

#### Before / After Example

| Before | After |
|--------|-------|
| ```cpp<br>class A {<br> public:<br>  void Initialize() {<br>    b_.Initialize();<br>    c_ = b_->GetC();<br>  }<br><br>  void Shutdown() {<br>    b_.Shutdown(); // `c_` is dangling<br>  }<br><br> private:<br>  B b_;<br>  raw_ptr<C, DanglingUntriaged> c_;<br>};<br>``` | ```cpp<br>class A {<br> public:<br>  void Initialize() {<br>    b_.Initialize();<br>    c_ = b_->GetC();<br>  }<br><br>  void Shutdown() {<br>    c_ = nullptr; // Destroyed by `b_` below:<br>    b_.Shutdown();<br>  }<br><br> private:<br>  B b_;<br>  raw_ptr<C> c_;<br>};<br>``` |

### Reset Pointer Toward Self Deleting Object (10.16%)

**Example CL:** [Link](#)

Self deleting classes are common in Chrome, but it's rather a bad pattern. It is better to have the class connected to "the world" somehow.

When the pointer is used to represent ownership over the pointee, it would be better to start using `std::unique_ptr`. However, in some cases, it is rather complicated. `ExtractAsDangling()` is used to reset the pointer, while using it to request the deletion of the pointee.

> **NOTE:** `ExtractAsDangling()` temporarily extracts the pointer as "allowed to dangle", but its lifetime is limited to the line that performs the destruction – it must not be saved in a variable and used later!

#### Before / After Example

| Before | After |
|--------|-------|
| ```cpp<br>class A {<br>  // [...]<br>  void Action() {<br>    b_->SelfDelete(); // b_ is dangling.<br>  }<br>  private:<br>    raw_ptr<B, DanglingUntriaged> b_;<br>};<br><br>class B {<br>  void SelfDelete() {<br>    delete this;<br>  }<br>;<br>``` | ```cpp<br>class A {<br>  // [...]<br>  void Action() {<br>    b_.ExtractAsDangling()->SelfDelete();<br>    // `b_` is nullptr.<br>  }<br>  private:<br>    raw_ptr<B> b_;<br>};<br><br>class B {<br>  void SelfDelete() {<br>    delete this;<br>  }<br>;<br>``` |

### Reset Pointer During Observer Destruction Callback (3.91%)

**Example CL:** [Link](#)

Chrome uses the observer pattern heavily. In some cases, the `observee` pointer become dangling, because the observer did not clear it when notified of its destruction:

#### Before / After Example

| Before | After |
|--------|-------|
| ```cpp<br>class A : public B::Observer {<br><br>  void BDestroyed() override {<br>    // [...]<br>  }<br><br>  raw_ptr<B, DanglingUntriaged> b_;<br>};<br>``` | ```cpp<br>class A : public B::Observer {<br><br>  void BDestroyed() override {<br>    b_ = nullptr;<br>    // [...]<br>  }<br><br>  raw_ptr<B> b_;<br>};<br>``` |

### Reset Pointer When Deleting Objects Whose Lifetime is Managed Elsewhere (3.91%)

**Example CL:** [Link](#)

Sometimes, the pointer is holding an alive object, but it is not implemented as a `unique_ptr`. The "real" owner is providing an API to request the deletion of the object. In this case, `ExtractAsDangling()` has been used to reset the pointer, while calling the API. See also [this note](#).

### Pointer Vended From C API (3.13%)

**Example CL:** [Link](#)

Most pointers vended from C API have been converted to a `unique_ptr` with a custom deleter. However, some haven't. Instead `ExtractAsDangling()` was used to clear the `raw_ptr<T>`, and then call the C deleter function.

---

*Source: [Dangling Pointers Retrospective](https://docs.google.com/document/d/11YYsyPF9rQv_QFf982Khie3YuNPXV0NdhzJPojpZfco/edit)*
