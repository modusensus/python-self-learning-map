# Conda 使用笔记

## 安装 Conda

- 推荐 [Miniconda](https://docs.anaconda.com/miniconda/)（轻量级，够用）
- 或 [Anaconda](https://www.anaconda.com/download)（自带大量数据科学包）
- 安装时勾选 **Add to PATH**

## 为本项目创建环境

```bash
# 进入项目目录
cd python-self-learning-map

# 创建环境（指定 Python 3.10）
conda create -n py-learn python=3.10

# 激活环境
conda activate py-learn

# 按需安装依赖（取消注释 requirements.txt 中的包再执行）
pip install -r requirements.txt
```

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

# 删除环境
conda remove -n myenv --all
```