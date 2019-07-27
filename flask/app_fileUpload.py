from flask import Flask, render_template,request
import os

app=Flask(__name__)

@app.route('/fileform')
def fileform():
    return render_template('upload.html')

@app.route('/fileUpload',methods=['POST'])
def fileUpload():
        f = request.files['file']
        print(type(f))
        dirname = os.path.dirname(__file__)+'/uploads/'+f.filename
        f.save(dirname)
        return 'upload 성공'

if __name__=='__main__':
    app.run()
