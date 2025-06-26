
<div style="background-color:var(--communication-background);color:var(--text-on-communication-background);border:var(--communication-background) 10px solid;margin:20px 0;">
<div style="padding-bottom:10px;font-weight:bold">💻 How to run locally</div>
<p>Add these to your <strong>args.gn</strong></p>
<pre>
goma_dir = "C:\Edge\depot_tools\.cipd_bin"
use_remoteexec = true
use_siso = true
is_debug = false  # Important! (*)
is_component_build = false  # Important! (*)
dcheck_always_on = true
enable_clang_use_chrome_plugins = true
enable_backup_ref_ptr_support = true  # true by default on some platforms
enable_dangling_raw_ptr_checks = true
enable_backup_ref_ptr_instance_tracer = true
blink_symbol_level = 0
v8_symbol_level = 0
</pre>
<p>Make sure you enable these feature flags in your unit test or browser test:</p>
<pre>
--enable-features=PartitionAllocBackupRefPtr,PartitionAllocDanglingPtr:type/all/mode/log_only
</pre>
</div>

[[_TOC_]]

This page is in draft, and mileage may vary. Feel free to reach out to [Security channel](https://teams.microsoft.com/l/channel/19%3Adfce36fbdf184309a73d49b8b95a6e40%40thread.skype/Security?groupId=0183ae9f-67b8-4ab0-80bf-761036ec893d&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47) for dangling pointer assistance.

A dangling pointer occurs when a `raw_ptr<T>` is freed and it's underlying memory has already been released. This does not specifically mean a use after free can occur, but that the environment exists in which one could.

# Building with Dangling pointer detector enabled
Dangling pointer detector (`DPD`) requires a build with specific gn args:
```
C:\Edge\src>gn args ./out/dangling/
```

If using RBE (recommended)
```
goma_dir = "C:\Edge\depot_tools\.cipd_bin"
use_remoteexec = true
use_siso = true
is_debug = false  # Important! (*)
is_component_build = false  # Important! (*)
dcheck_always_on = true
enable_clang_use_chrome_plugins = true
enable_backup_ref_ptr_support = true  # true by default on some platforms
enable_dangling_raw_ptr_checks = true
enable_backup_ref_ptr_instance_tracer = true
blink_symbol_level = 0
v8_symbol_level = 0
```


Don't forget to switch to the build folder you just created.

``` 
C:\Edge\src> cd out\dangling
```


It also requires specific command line arguments, Eg: 
`--enable-features=PartitionAllocBackupRefPtr,PartitionAllocDanglingPtr:type/all/mode/log_only`


If you encounter an error like `Output data too large` while building in the `dangling` build folder, it's a known issue—especially when building `unit_tests` and `browser_tests`.

```
lld-link: error: Output data is larger than 8 GiB. File size 8,607,637,504 too large for current PDB page size 8192  
lld-link: error: try setting a larger /pdbpagesize  
lld-link: error: failed to write PDB file ./unit_tests.exe.pdb
```

![==image_0==.png](/.attachments/==image_0==-1ced57ef-446c-4a6a-b58d-a31b1dce47c3.png) 

#### Workaround
To fix this, add the following lines to your `out/dangling/args.gn` and build the test-suite again:

```
blink_symbol_level = 0
v8_symbol_level = 0 
```



Further details of both can be found here: https://chromium.googlesource.com/chromium/src/+/refs/heads/main/docs/dangling_ptr.md
[How to Fix Upstream Dangling Pointers](https://microsoft.visualstudio.com/Edge/_wiki/wikis/Edge.wiki/145139/How-to-Fix-Upstream-Dangling-Pointers-(DanglingUntriaged))

# How to Triage?

## Failing Tests
Failing tests will likely be assigned in one of two triage states:
1. Triage Needed - in this state a dangling pointer issue has been identified but the offending pointer not yet located.
2. Investigate the issue - initial triage is complete and the dangling pointer has been identified - marked with `EDGE_DANGLING_UNTRIAGED` in code (discussed further below).

### 1. Triage Needed
In this scenario the dangling pointer is not identified but the repro steps are available in the bug report. Build the `unit_tests`/`components_unittests`/`browser_tests` and run using the specified command line. One should receive a dangling pointer report.

The report will contain two useful main call stacks:
* where the memory pointer to was freed
* where the dangling pointer was released

Here is an example output, with some frames removed for brevity:
```
[66936:36468:ERROR:partition_alloc_support.cc(640)] Detected dangling raw_ptr with id=0x0000431800027d78:
[DanglingSignature]     edge_assistance_home::AssistanceHomeActionAdapter::~AssistanceHomeActionAdapter No active task  edge_assistance_home::AssistanceHomeNurturingActionHandler::~AssistanceHomeNurturingActionHandler       No active task

The memory was freed at:
        base::debug::CollectStackTrace [0x00007FF6BE67AAD2+18] (F:\Edge\src\base\debug\stack_trace_win.cc:329)
        base::debug::StackTrace::StackTrace [0x00007FF6BE689DB2+18] (F:\Edge\src\base\debug\stack_trace.cc:218)
        base::allocator::`anonymous namespace'::DanglingRawPtrDetected [0x00007FF6BE67DC1B+843] (F:\Edge\src\base\allocator\partition_alloc_support.cc:454)
        allocator_shim::internal::PartitionFree [0x00007FF6BE9EFDE8+1624] (F:\Edge\src\base\allocator\partition_allocator\src\partition_alloc\shim\allocator_shim_default_dispatch_to_partition_alloc.cc:340)
        edge_assistance_home::AssistanceHomeActionAdapter::~AssistanceHomeActionAdapter [0x00007FF6C07A15CA+42] (F:\Edge\src\chrome\browser\ui\webui\edge_assistance_home\assistance_home_chrome_delegate_impl.cc:113)
        edge_assistance_home::AssistanceHomeClient::~AssistanceHomeClient [0x00007FF6C079FD9E+52] (F:\Edge\src\chrome\browser\ui\webui\edge_assistance_home\assistance_home_client.cc:42)
        edge_assistance_home::AssistanceHomeClient::~AssistanceHomeClient [0x00007FF6C07A0200+16] (F:\Edge\src\chrome\browser\ui\webui\edge_assistance_home\assistance_home_client.cc:42)
    ...
        main [0x00007FF6C568F676+462] (F:\Edge\src\chrome\test\base\run_all_unittests.cc:83)
        __scrt_common_main_seh [0x00007FF6C58A3078+268] (D:\a\_work\1\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl:288)
        BaseThreadInitThunk [0x00007FF8FD4B8D17+23]
        RtlUserThreadStart [0x00007FF8FE427450+32]

Task trace:
No active task.
The dangling raw_ptr was released at:
        base::debug::CollectStackTrace [0x00007FF6BE67AAD2+18] (F:\Edge\src\base\debug\stack_trace_win.cc:329)
        base::debug::StackTrace::StackTrace [0x00007FF6BE689DB2+18] (F:\Edge\src\base\debug\stack_trace.cc:218)
        base::allocator::`anonymous namespace'::DanglingRawPtrReleased<0,0> [0x00007FF6BE67DEA7+55] (F:\Edge\src\base\allocator\partition_alloc_support.cc:612)
        base::internal::RawPtrBackupRefImpl<0,0>::ReleaseInternal [0x00007FF6BE9E04DB+395] (F:\Edge\src\base\allocator\partition_allocator\src\partition_alloc\pointers\raw_ptr_backup_ref_impl.cc:53)
        edge_assistance_home::AssistanceHomeNurturingActionHandler::~AssistanceHomeNurturingActionHandler [0x00007FF6C4ACF795+49] (F:\Edge\src\components\edge_assistance_home\core\common\actionhandler\assistance_home_nurturing_action_handler.cc:14)
        edge_assistance_home::AssistanceHomeNurturingActionHandler::~AssistanceHomeNurturingActionHandler [0x00007FF6C4ACF860+16] (F:\Edge\src\components\edge_assistance_home\core\common\actionhandler\assistance_home_nurturing_action_handler.cc:14)
        edge_assistance_home::AssistanceHomeManager::~AssistanceHomeManager [0x00007FF6C3D67FA3+141] (F:\Edge\src\components\edge_assistance_home\core\common\managers\assistance_home_manager.cc:20)
        edge_assistance_home::AssistHomeNurturingOfflineManager::~AssistHomeNurturingOfflineManager [0x00007FF6C3D67C36+38] 
...
        testing::UnitTest::Run [0x00007FF6BC9919D7+209] (F:\Edge\src\third_party\googletest\src\googletest\src\gtest.cc:5440)
        base::TestSuite::Run [0x00007FF6BE0016C6+166] (F:\Edge\src\base\test\test_suite.cc:418)
        content::UnitTestTestSuite::Run [0x00007FF6C569055F+159] (F:\Edge\src\content\public\test\unittest_test_suite.cc:191)
        base::OnceCallback<dual_engine::CacheFileWriteStatus ()>::Run [0x00007FF6B986F83F+75] (F:\Edge\src\base\functional\callback.h:156)
        base::`anonymous namespace'::LaunchUnitTestsInternal [0x00007FF6BDFFB816+465] (F:\Edge\src\base\test\launcher\unit_test_launcher.cc:264)
        base::LaunchUnitTests [0x00007FF6BDFFB61A+268] (F:\Edge\src\base\test\launcher\unit_test_launcher.cc:312)
        main [0x00007FF6C568F676+462] (F:\Edge\src\chrome\test\base\run_all_unittests.cc:83)
        __scrt_common_main_seh [0x00007FF6C58A3078+268] (D:\a\_work\1\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl:288)
        BaseThreadInitThunk [0x00007FF8FD4B8D17+23]
        RtlUserThreadStart [0x00007FF8FE427450+32]

Task trace:
No active task.
```
Here we can see two useful pieces of information:
1. The memory is released in the destructor of `AssistanceHomeActionAdapter::~AssistanceHomeActionAdapter`
2. The `raw_ptr` left dangling is released in `AssistanceHomeNurturingActionHandler::~AssistanceHomeNurturingActionHandler`

Using these two pieces of information we see that:
1. `AssistanceHomeNurturingActionHandler` has a member `raw_ptr<AssistanceHomeChromeDelegate> chrome_delegate_`
2. `AssistanceHomeActionAdapter` derives from `AssistanceHomeChromeDelegate`

We likely have our dangling pointer identified. To test this hypothesis, we can mark out raw_ptr<T> `EDGE_DANGLING_UNTRIAGED(<your_ado_id_here>)` to test our hypothesis:
```cpp
  raw_ptr<AssistanceHomeChromeDelegate, EDGE_DANGLING_UNTRIAGED(49096907)>
      chrome_delegate_ = nullptr;
```
Rebuild and run the unit test with DPD enabled and your error should be removed. Be aware you may now find other errors so ensure that the previous error report has changed.

If your task is initial triage submit your patch to main and mark the associated ado bug to `Investigate`. If you are also required to fix the bug proceed through the next section.

### 2. Investigate the issue
An initial triage is complete, and the problematic pointer has been identified. This pointer can be located by searching the codebase for `EDGE_DANGLING_UNTRIAGED(<ADOBUGID>)` - replacing `<ADOBUGID>` with the ID of the bug you have been assigned.

First triage step is to repro the bug - so remove the `EDGE_DANGLING_UNTRIAGED` trait from the `raw_ptr` and [rebuild with dangling pointer detector enabled](https://microsoft.visualstudio.com/Edge/_wiki/wikis/Edge.wiki/145036/Dangling-Pointer-Detector-Triage?anchor=building-with-dangling-pointer-detector-enabled). Then run the failing test described in the repro steps - you should now have a dangling pointer report to work from. Any issues at this point contact the reporting engineer.

#### Fixing the issue
1. Take a look at the common bug patterns discussed below in case you're also hitting the same
2. Take a look at [this](https://docs.google.com/spreadsheets/d/1WREayvW_0wPucyxRAOriecbLWmfGWBLZN_xNrOu7epc/edit?gid=652611543#gid=652611543) great documentation on various fix strategies upstream has used for fixing dangling pointers
3. Another good starting point is the excellent document [How to Fix Upstream Dangling Pointers - Fixing the Failure](https://microsoft.visualstudio.com/Edge/_wiki/wikis/Edge.wiki/145139/How-to-Fix-Upstream-Dangling-Pointers-(DanglingUntriaged)?anchor=fixing-the-failure)

#### Not repro?

Every effort is made to ensure bugs reproduce, but on occasion there will non repro cases. Please do not close without following these steps:
1. Remove the `EDGE_DANGLING_UNTRIAGED<_ADOID_>` decoration from the offending pointer
2. Create a new branch with this change
3. Run this new branch through the DPD pipeline: [link](https://microsoft.visualstudio.com/Edge/_build?definitionId=124907&_a=summary)
4. If you see no recurrence of the issue the create a PR from your branch and close the bug
5. If a problem persists but in a different unit test this may still be your responsibility, bugs are assigned based on believed root cause, not failing test, so please investigate. If you believe this is not your responsibility **please do not just close not repro**, reassign to the bug creator or speak to them directly about your issue.

# Common Patterns
A brief listing of observed patterns which may assist in understanding and fixing of DPD issues one finds.

## Leaking Objects

If an object is not correctly freed then any `raw_ptr` members it has, or its owned members have, will not be released and report an error in dangling pointer detector. Therefore, all objects owning raw pointers should be correctly freed.

## Destruction Order

This is one of the simpler, less exploitable, and quick to fix patterns which represents ~25% of dangling pointers. 

Recall that destructors destroy class members in the inverse order of their appearance. It is usually possible to resolve destruction order issues by re-ordering member declarations so that members which need to live longer come first. It is important to order members correctly to prevent pre-existing and
future UAF in destructors.

The object which owns the memory pointed at by a raw pointer is destroyed prior to the `raw_ptr`. A common example see two class members that depends on one another:

```cpp
raw_ptr<TestingProfile> profile_; // [2]
TestingProfileManager profile_manager_; // [1]
```

Note:
__[1]__ `profile_manager_` is released first due to destruction order. This owns the underlying memory that `profile_` points at. `profile_` is now dangling.
__[2]__ `profile_` is freed - The underlying memory is quarantined and as such dangling pointer detector throws an error.

Reversing the declaration order will fix this issue.

See [Fix member declaration order](https://docs.google.com/document/d/11YYsyPF9rQv_QFf982Khie3YuNPXV0NdhzJPojpZfco/edit?resourcekey=0-h1dr1uDzZGU7YWHth5TRAQ#bookmark=id.jgjtzldk9pvc) and [Fix reset ordering](https://docs.google.com/document/d/11YYsyPF9rQv_QFf982Khie3YuNPXV0NdhzJPojpZfco/edit?resourcekey=0-h1dr1uDzZGU7YWHth5TRAQ#bookmark=id.xdam727ioy4q) examples.

> One good practice is make owning members (`unique_ptr<>`, `scoped_refptr<>`) appear before unowned members (`raw_ptr<>`), and to make the unowned members appear last in the class, since the unowned members often refer to resources owned by the owning members or the class itself.

One sub-category of destruction order issues is related to `KeyedService`s which
need to correctly [declare their dependencies](https://source.chromium.org/chromium/chromium/src/+/main:components/keyed_service/core/keyed_service_base_factory.h;l=60-62;drc=8ba1bad80dc22235693a0dd41fe55c0fd2dbdabd) and [are expected to drop references](https://source.chromium.org/chromium/chromium/src/+/main:components/keyed_service/core/keyed_service.h;l=12-13;drc=8ba1bad80dc22235693a0dd41fe55c0fd2dbdabd) to their dependencies in their [`Shutdown`](https://source.chromium.org/chromium/chromium/src/+/main:components/keyed_service/core/keyed_service.h;l=36-39;drc=8ba1bad80dc22235693a0dd41fe55c0fd2dbdabd) method (i.e. before their destructor runs).

## Observer callback

This represents ~4% of the dangling pointers.

It is important to clear the pointer when the object is about to be deleted. Chromium uses the observer pattern heavily. In some cases, the observer does not clear its pointer toward the observed class when notified of its destruction.

## Cyclic pointers

Sometimes two (or more) objects can have unowned references between each other, with neither one owning the other. This creates a situation where neither can be deleted without creating a dangling pointer unless some action is first taken to break the cycle. In order to create such a cycle in the first place, a call to a "setter" method or equivalent must have occurred handing one object a reference to the other. Balance out this call with another call to the same setter, but passing `nullptr` instead, before the destroying the other object.

## Challenging lifespan

It can be challenging to deal with an object's lifespan. Sometimes, the lifetime of two objects are completely different.

Removing the pointer may be a good thing to do. Sometimes, it can be replaced
by:
-   Passing the pointer as a function argument instead of getting access to it
    from a long-lived field.
-   A token / ID. For instance [blink::LocalFrameToken](https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/public/common/tokens/tokens.h;drc=898134d0d40dbbcd308e7d51655518ac7c6392b5;l=34), [content::GlobalRenderFrameHostId](https://source.chromium.org/chromium/chromium/src/+/main:content/public/browser/global_routing_id.h;drc=898134d0d40dbbcd308e7d51655518ac7c6392b5;l=64)
-   A [WeakPtr](https://docs.google.com/document/d/11YYsyPF9rQv_QFf982Khie3YuNPXV0NdhzJPojpZfco/edit?resourcekey=0-h1dr1uDzZGU7YWHth5TRAQ#bookmark=id.geuhahom0twd)
-   [Calling a function](https://docs.google.com/document/d/11YYsyPF9rQv_QFf982Khie3YuNPXV0NdhzJPojpZfco/edit?resourcekey=0-h1dr1uDzZGU7YWHth5TRAQ#heading=h.wh99ri7bbq23)

## The pointer manages ownership over the object

`raw_ptr`, just like raw pointers `T*`, are not meant to keep an object alive. It is preferable not to manage memory manually using them and `new`/`delete`. Calling `delete` on a `raw_ptr` will cause the `raw_ptr` to become immediately dangling.

Consider replacing the `raw_ptr` with a smart pointer like `std::unique_ptr` (See [example](https://docs.google.com/document/d/11YYsyPF9rQv_QFf982Khie3YuNPXV0NdhzJPojpZfco/edit?resourcekey=0-h1dr1uDzZGU7YWHth5TRAQ#heading=h.6itq8twigqt3))

# Branch Sheriff
If you are facing issues with the dangling pointer pipeline.
1. If the commit causing the failure is identified by finding the diff between 2 runs. Revert the offending commit. 
2. If a handful of tests are failing. Disable the tests. Add the tag 'DanglingPointer' to it.
3. If a test suite is failing disable the suite with ""--disable-features=PartitionAllocBackupRefPtr" flag.
4. If there is more than 2 test suites failing. Please reach out to the [Security channel](https://teams.microsoft.com/l/channel/19%3Adfce36fbdf184309a73d49b8b95a6e40%40thread.skype/Security?groupId=0183ae9f-67b8-4ab0-80bf-761036ec893d&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47) for assistance.

#PoC
1. tatiwari@microsoft.com
2. utkarshpal@microsoft.com
3. farazak@microsoft.com
