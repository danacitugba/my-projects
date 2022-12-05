# bu uygulamada template kullancağımız için render_template modülünü de import ediyoruz
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1 = 117000, number2 = 229000)
    # index.html isimli templatei kullan; number1 ve number2 ise index.html argumaları
    # index.html templates klasörü içerisinde

@app.route('/sum')
def number():
    var1, var2 = 15210, 38960
    return render_template('body.html', value1 = var1, value2 = var2, sum = var1 + var2)


if __name__ == '__main__':
    app.run(debug=True) # default port = 5000 fakat çalışmıyorsa boş port ataması yapılacak. 