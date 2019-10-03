
# 系统环境
ubuntu18.04 64位

# 安装python3.6.5
1、打开终端<br>
首先创建安装目录，
```python
sudo mkdir /usr/local/python3
```
2、然后下载安装包，解压，并且进入
```python
wget --no-check-certificate https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
tar -xzvf Python-3.6.5.tgz
cd Python-3.6.5
```
3、接着编译安装
```python
sudo ./configure --prefix=/usr/local/python3
sudo make
sudo make install
```
如果第一步编译的时候出现了报错，则试试
```python
sudo apt-get install build-essential
```
4、创建python3的链接
```python
sudo ln -s /usr/local/python3/bin/python3 /usr/bin/python3
```
5、检查python3是否可以用
```python
huyq@huyq-OptiPlex-3050:~/下载$ python -V
Python 3.6.5
```
6、安装pip以及setuptools
由于安装pip前需要安装setuptools，我们先安装setuptools
还是在home的“下载”路径中，







