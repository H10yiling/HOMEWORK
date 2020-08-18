#先輸入較小的數再輸入較大的數   
# EX：http://127.0.0.1:5000/index/3/9/  會顯示出3*3~3*9...9*3~9*9的乘法表
from flask import Flask
app = Flask(__name__)

@app.route("/index/<n1>/<n2>/")
def index(n1,n2):
    a = " "
    for i in range(int(n1),int(n2)+1):
        for j in range(int(n1),int(n2)+1):
            a = a + str("%d * %d = %2d ; "%(j,i,i*j))
        a = a +"<br/>"
    return a

if __name__ == "__main__":
    app.run()     #输出