from math import ceil
from flask import request, url_for

class Articles(object):

    def __init__(self, articles, per_page):
        self.articles = articles
        self.article_count = len(self.articles)
        self.per_page = per_page

    @property
    def pages(self):
        return int(ceil(self.article_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self):
        for pg in range(1, self.pages):
            yield pg

    def get_articles(self, page, per_page):
        if(per_page > self.article_count):
            for art_num in range(self.article_count):
                yield self.articles[art_num]
        else:
            offset = page * per_page
            for art_num in range(offset, (offset+per_page), 1):
                print(art_num)
                if(art_num < len(self.articles)):
                    yield self.articles[art_num]
