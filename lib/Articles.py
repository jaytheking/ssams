from os import listdir
from math import ceil
from copy import deepcopy


class Articles(object):

    def __init__(self, articles, per_page):
        self.articles = articles
        self.article_count = len(self.articles)
        self.per_page = per_page

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    def get_articles_for_page(self, page, per_page, count):
        pass
