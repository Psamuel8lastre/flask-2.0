from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hola():
    return render_template('index.html')



@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/recuperacion')
def recuperar():
    return render_template('recuperacion.html')
if __name__ == '__main__':
    app.run(debug=True)