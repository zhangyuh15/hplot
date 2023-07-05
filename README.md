# hplot

A plot package for myself



# upload method

### Create `.pypirc`

```
[distutils] 
index-servers=pypi 
 
[pypi] repository = https://upload.pypi.org/legacy/ 
username = 账户名 
password = 密码
```

### 打包

```

pip install build

python -m build

# or 

python -m build --sdist
python -m build --wheel

```

### 上传

```

pip install twine

twine check dist/*
```
