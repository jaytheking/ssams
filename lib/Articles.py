from os import listdir
from math import ceil
from copy import deepcopy


class Articles(object):

    def __init__(self, articles, per_page):
        self.articles = deepcopy(articles)
        self.article_count = len(self.articles)
        self.articles_paginated = {}
        self.per_page = per_page
        self.__paginate_articles(self.per_page, self.article_count)

    def get_articles_for_page(self, page, art_count):
        if self.articles_paginated:
            return self.articles_paginated["page{0}".format(str(page))]
        else:
            self.__paginate_articles(self.per_page, art_count)
        return self.articles_paginated["page{0}".format(str(page))]

    def __paginate_articles(self, per_page, art_count):
        local_articles = deepcopy(self.articles)
        num_pages = int(ceil(art_count / float(per_page)))
        for page in range(num_pages):
            page_num = "page{0}".format(str(page))
            self.articles_paginated[page_num] = []
            for article in range(per_page):
                if len(local_articles) > 0:
                    next_article = local_articles.pop()
                    self.articles_paginated[page_num].append(next_article)