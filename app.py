from flask import Flask, render_template, abort, request, url_for
import os
import codecs
import markdown
import settings
from lib.Articles import Articles
from lib.utility import url_for_other_page

app = Flask(__name__)
app.config.from_object(settings.dev)
articles = Articles(
                    app.config["FILE_LIST"],
                    app.config["ARTICLES_PER_PAGE"]
                    )

# PER_PAGE = 1
# article_dir = 'articles/'
# articles = os.listdir(article_dir)
# articles = Articles(articles, PER_PAGE)

@app.route('/', defaults={'page': 0})
@app.route('/page/<int:page>')
def show_articles(page):
    article_list = articles.get_articles(page, app.config["ARTICLES_PER_PAGE"])
    pages = articles.iter_pages()
    if not articles and page != 1:
        abort(404)
    return render_template(
                           'index.html',
                           header=True,
                           articles=article_list,
                           per_page=app.config["ARTICLES_PER_PAGE"]
                           page_list=page)

@app.route('/a/<file_name>')
def article(file_name):
    path = app.config["ARTICLE_BASE_DIR"] + file_name
    try:
        article = codecs.open(path, mode='r', encoding='utf-8')
    except IOError:
        return abort(404)
    html = markdown.markdown(article.read())
    article.close()
    return render_template('article.html', html=html, header=False)

app.jinja_env.globals['url_for_other_page'] = url_for_other_page

if __name__ == '__main__':
    app.run(debug=True)
