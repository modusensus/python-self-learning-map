# VS Code 设置

## 推荐扩展

- Python (Microsoft)
- Pylance
- Ruff（代码检查 + 格式化）
- Jupyter

## 实用设置

```json
{
  "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe",
  "editor.formatOnSave": true,
  "python.analysis.typeCheckingMode": "basic",
  "files.exclude": {
    "**/__pycache__": true,
    "**/.pytest_cache": true
  }
}
```