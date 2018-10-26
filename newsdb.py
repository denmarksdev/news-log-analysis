#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2
from string import Template

DBNAME = "news"


def get_query_result(query):
    try:
        db = psycopg2.connect(database=DBNAME)
        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        db.close()
    except:
        print ("unable to connect to the database")
    return result


def get_top_3_articles_by_num_views():

    results = get_query_result('''
    SELECT v.title, v.views 
    FROM view_top_article_by_views AS v
    LIMIT 3
    ''')

    articles = []
    for article, views in results:
        articles.append('%s - %s views' % (article, views,))

    return articles


def get_top_authors_by_num_views_articles():

    results = get_query_result('''
    SELECT authors.name, SUM(v.views) as views
    FROM view_top_article_by_views AS v, authors
    WHERE authors.id = v.author
    GROUP BY authors.name
    ORDER BY views DESC
    ''')

    authors = []
    for author, views in results:
        authors.append('%s - %s views' % (author, views,))

    return authors


def get_error_request_by_day_more_than_1percent():

    results = get_query_result('''
    SELECT * FROM  view_errors_request_by_day_more_than_1percent
    ''')
    errors = []
    for date, percent in results:
        errors.append('%s - %s errors' % (date, percent,))

    return errors
