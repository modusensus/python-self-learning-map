# Conda 使用笔记

## 常用命令

```bash
# 创建环境
conda create -n myenv python=3.10

# 激活环境
conda activate myenv

# 退出环境
conda deactivate

# 查看环境列表
conda env list

# 安装包
conda install numpy pandas

# 导出环境
conda env export > environment.yml

# 从文件创建环境
conda env create -f environment.yml
```