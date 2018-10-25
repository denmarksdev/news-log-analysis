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


def get_top_articles_by_num_views():
    results = get_query_result("SELECT * FROM view_top_article_by_views")

    articles = []
    for article, views in results:
        articles.append('%s - %s' % (article, views,))

    return articles


def get_top_authors_by_num_views_articles():
    results = get_query_result(
        "SELECT * FROM view_top_authors_by_views_article")

    articles = []
    for author, views in results:
        articles.append('%s - %s' % (author, views,))

    return articles


def get_error_request_by_day_more_than_1percent():
    results = get_query_result(
        "SELECT * FROM view_errors_request_by_day_more_than_1percent")

    errors = []
    for date, percent in results:
        errors.append('%s - %s' % (date, percent,))

    return errors

print(get_error_request_by_day_more_than_1percent())
