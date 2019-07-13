from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_admin():
    return render_template('main.html')

@app.route('/moviecontents')
def moviecontents():
    return render_template('moviecontents.html')


if __name__ == '__main__':
    app.run(debug=True)