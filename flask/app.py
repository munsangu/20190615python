from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/user/<username>')
def user(username):
    return "User %s" % username

@app.route('/user/<username>/<int:age>')
def user1(username,age):
    # return "Username %s, age %d"%(username,age)
    return render_template('index.html', username=username, age=age)

@app.route('/forminput/')
def forminput():
    return render_template('form_input.html')

@app.route('/method/',methods=['GET','POST'])
def method():
    if request.method == "POST":
        return "POST"
    else:
        return "GET"

@app.route('/login/')
def login():
    username = request.args.get('name')
    return  render_template('index.html',username=username)       

@app.route('/form_input1/')
def forminput1():
    return render_template('form_input1.html')

@app.route('/login/', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    return  render_template('index.html',username=username, password=password)  


if __name__=='__main__':
    app.run()
