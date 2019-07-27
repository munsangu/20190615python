from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('form_input2.html')

@app.route('/login/',methods=['POST'])
def login():
        result=request.form.to_dict()
        print(type(result))
        return render_template('form_result.html',result=result)    

if __name__=='__main__':
    app.run()
