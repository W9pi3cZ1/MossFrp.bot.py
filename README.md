# MossFrp.bot.py

## 主要功能
主要功能是模拟一个自动签到程序，首先检查当前日期是否与之前存储的日期（odate文件）相同，如果不同，就执行签到操作。

## 签到操作
签到操作首先读取一个密码文件（可以是多个不同的文件，默认是：pwd,pwd1,pwd2)，如果文件已经存在，那么从文件中读取邮箱和密码信息，否则等待用户输入邮箱和密码，然后将邮箱和密码存储在一个JS0N对象中，并以base64编码的形式存储在文件中。

## 请求API接口操作
接着，MossFrp.bot.py使用这个邮箱和密码向一个服务器发送HTTP请求，以获取一个token令牌(用于后续操作的认证验证)，然后再用这个token完成签到操作。如果程序在同一天内已经签过到了，就不再执行签到操作。

上面这一段是ChatGPT对main.py这段的代码的解释（被我稍稍修改了一下）
![New Chat](https://github.com/W9pi3cZ1/MossFrp.bot.py/assets/116885083/fe5779c1-8843-4df6-93d2-526ed7ad0624)


通过项目的main.py第一次运行需要用pip安装requests（用于代码请求API接口）

```` bash
pip install requests
# Run Scripts
python main.py
````
