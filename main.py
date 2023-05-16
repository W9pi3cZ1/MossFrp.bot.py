import json
import requests
import os
import base64
import time

def startreq(pwdfilename):
    if os.path.exists(pwdfilename) :
        with open(pwdfilename,"r") as f:
            d = f.read()
            d = base64.b64decode(d)
            d = d.decode()
            pobj = json.loads(d)

        email = pobj["email"]
        pwd = pobj["pwd"]
        print(email+" "+pwd)
    else :
        email = input("输入邮箱:")
        pwd = input("输入密码:")
        pobj = {"pwd":pwd,"email":email}
        b = base64.b64encode(bytes(json.dumps(pobj),'utf-8'))
        with open(pwdfilename,"w") as f:
            f.write(b.decode())

    reqjson = {
        "type": "login",
        "loginType": "email",
        "account": email,
        "password": pwd,
    }

    req1 = requests.get("https://https.ghs.wiki:7002/API?",params=reqjson)
    token = json.loads(req1.text)["token"]
    print(token)

    reqjson = {
      "type": "signIn",
      "token": token
    }
    req2 = requests.get("https://https.ghs.wiki:7002/API?",params=reqjson)
    print(req2.text)
if os.path.exists("odate"):
    with open("odate","r") as f:
        odate = f.read()
        if odate==time.strftime("%Y %m %d ", time.localtime()):
            print("已签到！")
            time.sleep(1)
        else:
            with open("odate","w") as f:
                f.write(time.strftime("%Y %m %d ", time.localtime()))
            startreq("pwd")
            startreq("pwd1")
            startreq("pwd2")
            
else:
    with open("odate","w") as f:
        f.write(time.strftime("%Y %m %d ", time.localtime()))
    startreq("pwd")
    startreq("pwd1")
    startreq("pwd2")
