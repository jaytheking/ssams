from flask import Flask, render_template, abort, request, url_for
import os
import codecs
import markdown
from lib.Pagination import Pagination
from lib.Articles import Articles

app = Flask(__name__)

ARTICLES_PER_PAGE = 10
article_dir = 'articles/'
articles = os.listdir(article_dir)
article_collection = Articles(articles, ARTICLES_PER_PAGE)


def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)
app.jinja_env.globals['url_for_other_page'] = url_for_other_page

@app.route('/', defaults={'page': 0})
@app.route('/page/<int:page>')
def show_articles(page):
    article_list = article_collection.get_articles_for_page(page, article_collection.article_count)
    if not articles and page != 1:
        abort(404)
    pagination = Pagination(page, ARTICLES_PER_PAGE, article_collection.article_count)
    return render_template('index.html', header=True, pagination=pagination, articles=article_list, per_page=(int(12/ARTICLES_PER_PAGE)))

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
