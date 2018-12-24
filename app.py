from flask import Flask
from flask import render_template
from flask_cors import CORS, cross_origin

from flask import request
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def hello_world():
    return "HELLO WORLD"
    #Template rendering işlemini de gerçekleştiriyoruz kolaylıkla
@app.route("/summarize",methods=["GET","POST"])
@cross_origin()
def summarize():
    from gensim.summarization import summarize
    form=request.form
    print(form)
    print("forum"+form['text']) #this line is work just fine
    #Still work fine.
    textdata=form['text']
    summary=summarize(textdata)
    #work just fine
    return summary
if __name__ == '__main__':
    app.run()
