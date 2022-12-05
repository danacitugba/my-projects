# flaskten gerekli kütüphaneyi ve ilgili metodları çeker
from flask import Flask 

# app isimli yeni bir object oluşturduk
app = Flask(__name__)

# Bu alan decorater alanının başladığı kısımdır. 
@app.route('/')
def hello():
    return "Hello World from Flask!!!"

@app.route('/second')
def second():
    return 'Bize Her Yer Trabzon!!!!'

@app.route('/third/subthird')
def third():
    return 'This is the subpage of third page'

@app.route('/forth/<string:id>') # girilen id yi dinamik olarak çekerek return değerine gönderir
def forth(id):
    return f'Id number of this page is {id}'



# eğer herşey yolundaysa çalıştırmayı Debug modunda gerçekleştir. Hata varsa gösterir çalıştırırken. 
if __name__ == '__main__':
    app.run(debug=True, port = 2000) # port default değeri 5000 dir. 


# Bu kodlar html durum kodlarıdır.
# 127.0.0.1 - - [05/Dec/2022 22:35:36] "GET / HTTP/1.1" 200 -
# 127.0.0.1 - - [05/Dec/2022 22:35:36] "GET /favicon.ico HTTP/1.1" 404 -