# 🔧 GitHub Pages 部署故障排除

## ❌ 当前问题

GitHub Pages 部署失败，错误信息显示：
```
Get Pages site failed. Please verify that the repository has Pages enabled and configured to build using GitHub Actions
```

## ✅ 解决步骤

### 第一步：启用 GitHub Pages

1. **访问仓库设置**
   - 打开：https://github.com/Yanhu007/Prompts/settings/pages

2. **配置 Pages 源**
   - 在 "Source" 部分选择 **"GitHub Actions"**
   - **不要**选择 "Deploy from a branch"
   - 点击 **Save**

### 第二步：设置 Actions 权限

1. **访问 Actions 设置**
   - 打开：https://github.com/Yanhu007/Prompts/settings/actions

2. **配置工作流权限**
   - 滚动到 "Workflow permissions" 部分
   - 选择 **"Read and write permissions"**
   - 勾选 **"Allow GitHub Actions to create and approve pull requests"**
   - 点击 **Save**

### 第三步：手动触发部署

1. **访问 Actions 页面**
   - 打开：https://github.com/Yanhu007/Prompts/actions

2. **重新运行工作流**
   - 点击最新的失败的工作流
   - 点击 **"Re-run all jobs"**

## 🔍 验证步骤

完成上述设置后：

1. **检查部署状态**
   - 在 Actions 页面查看工作流是否成功运行
   - 绿色✅表示成功，红色❌表示失败

2. **访问网站**
   - 成功后访问：https://yanhu007.github.io/Prompts/
   - 首次部署可能需要5-10分钟

## 🚨 常见问题

### Q: 仍然显示 404 错误？
**A:** 
- 确保 `index.html` 文件在仓库根目录
- 等待几分钟让DNS传播
- 清除浏览器缓存

### Q: Actions 权限被拒绝？
**A:**
- 检查仓库是否为私有（私有仓库需要 GitHub Pro）
- 确认已启用 "Read and write permissions"

### Q: 工作流一直失败？
**A:**
- 检查 YAML 语法是否正确
- 确认文件路径正确
- 查看具体错误日志

## 📞 需要帮助？

如果问题持续存在，请：

1. 截图错误信息
2. 检查以下设置是否正确：
   - Repository Settings > Pages > Source = "GitHub Actions"
   - Repository Settings > Actions > Workflow permissions = "Read and write permissions"
3. 提供 Actions 页面的错误详情

---

**重要提醒**：GitHub Pages 对于公开仓库是免费的，但私有仓库需要 GitHub Pro 订阅。
