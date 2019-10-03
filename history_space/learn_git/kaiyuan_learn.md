
# 开源学习
# 一、注册账号
GITHUB账号
NPM账号
# 二、开发环境搭建
##安装工具
```
安装webpack，安装node： https://blog.csdn.net/NeroSolomon/article/details/78934358
npm install -g cnpm --registry=https://registry.npm.taobao.org
npm install webpack -g
npm install webpack --save-dev
```
##初始化开发环境
```
npm init
name:(fast-cache)       # 不填，回车
version: (1.0.0)        # 0.0.1
description:            # 短小精悍的前端缓存工具，防止内存泄露
entry point: (index.js) # src/index.js
test command:           # 不填，回车
git repository: (https://github.com/shaoxiaozuo/fast-cache.git)  # 不填，回车
keywords:            # cache
author:              # https://github.com/shaoxiaozuo
license: (ISC)       # MIT

Is this OK? (yes)    # yes
```
##规范一级目录
```
mkdir src release test doc example
```
##创建src/index.js文件
```

```
##构建工具
```
# 创建 .babelrc 文件
{
	"presets" : ["es2015","latest"],
	"plugins" : []
}
# 创建 webpack.config.js 文件
module.exports = {
	entry: './src/index.js',
	output: {
		path:__dirname,
		filename: './release/bundle.js'
	},
	module: {
		rules: [{
			test: /\.js?$/,
			exclude: /(node_modules)/,
			loader: 'babel-loader'
		}]
	}
}
```


