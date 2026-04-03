# conda环境配置常见命令
## 创建环境
```
conda create -n env_name python=3.8
```
其中`env_name`是你想要创建的环境名称，`python=3.8`指定了Python版本，可以根据需要更改。还可以添加其他包，例如：
```
conda create -n env_name python=3.8 numpy pandas
``` 
## 列出所有环境
```
conda env list
```
## 激活环境
```
conda activate env_name
``` 
## 退出环境
```
conda deactivate
```
## 删除环境
```
conda remove -n env_name --all
```

## 导出环境配置
```
conda env export > environment.yml
```
## 从配置文件创建环境
```
conda env create -f environment.yml
```
## 查看环境中已安装的包
```
conda list
```
## 更新环境中的包
```
conda update package_name
```
## 删除环境中的包
```
conda remove package_name
```
