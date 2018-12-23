from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html',baslik='Özet mevzusu',content="Ersan ilyasova çok ilginç bir oyuncudur.")
    #Template rendering işlemini de gerçekleştiriyoruz kolaylıkla
@app.route("/summarize",methods=["GET","POST"])
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