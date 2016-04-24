from flask import Flask, render_template, abort
import os
import codecs
import markdown

app = Flask(__name__)

article_dir = 'articles/'
print(os.listdir('articles'))



@app.route('/')
def index():

    flist = os.listdir('articles')
    return render_template('index.html', flist=flist, header=True)




@app.route('/a/<file_name>')
def article(file_name):
    try:
        fin = codecs.open(article_dir + file_name, mode='r', encoding='utf-8')
    except IOError:
        return abort(404)
    html = markdown.markdown(fin.read())
    fin.close()
    return render_template('article.html', html=html, header=False)


if __name__ == '__main__':
    app.run(debug=True)
