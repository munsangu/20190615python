from flask import Flask, render_template,request, redirect
import db

app = Flask(__name__)
db.create_table()

@app.route('/')
def index():
    return redirect('/list')

@app.route('/insertform')
def insertform():
    return render_template('main.html')

@app.route('/insert',methods=['POST'])
def insert_user():
        user = request.form.to_dict()
        db.insert_users(list(user.values()))
        return redirect('/list')

@app.route('/list')
def list_user():
        users=db.all_users()
        return render_template('list.html',users=users)

@app.route('/content/<userid>')
def content_user(userid):
        user=db.one_user(userid)
        return render_template('content.html',user=user)

@app.route('/delete/<userid>')
def delete_user(userid):
    db.delete_user(userid)
    return redirect('/list')

@app.route('/updateform/<userid>')
def updataform(userid):
        user=db.one_user(userid)
        return render_template('updateform.html',user=user)

@app.route('/update', methods=['POST'])
def update_user():
    user = request.form.to_dict()
    db.update_user(user)
    return redirect('/list')

if __name__ == '__main__':
    app.run()
