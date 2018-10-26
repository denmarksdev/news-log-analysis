#!/usr/bin/env python3

import psycopg2
from string import Template

DBNAME = "news"


def get_query_result(query):
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result


<<<<<<< HEAD
def get_top3_articles_by_num_views():
    results = get_query_result("SELECT * FROM view_top3_article_by_views")

=======
def get_top_3_articles_by_num_views():
    results = get_query_result("SELECT * FROM " +
                               "view_top_article_by_views")
>>>>>>> 5e2173e6b781c1f0bc82f21d1f96d080a75baa32
    articles = []
    for article, views in results:
        articles.append('%s - %s views' % (article, views,))

    return articles


def get_top_authors_by_num_views_articles():
<<<<<<< HEAD
    results = get_query_result(
        "SELECT * FROM view_top_authors_by_views_article")

=======
    results = get_query_result("SELECT * FROM " +
                               "view_top_authors_by_views_article")
>>>>>>> 5e2173e6b781c1f0bc82f21d1f96d080a75baa32
    articles = []
    for author, views in results:
        articles.append('%s - %s views' % (author, views,))

    return articles


def get_error_request_by_day_more_than_1percent():
<<<<<<< HEAD
    results = get_query_result(
        "SELECT * FROM view_errors_request_by_day_more_than_1percent")

=======
    results = get_query_result("SELECT * FROM " +
                               "view_errors_request_by_day_more_than_1percent")
>>>>>>> 5e2173e6b781c1f0bc82f21d1f96d080a75baa32
    errors = []
    for date, percent in results:
        errors.append('%s - %s errors' % (date, percent,))

    return errors
