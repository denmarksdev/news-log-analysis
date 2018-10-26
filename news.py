#!/usr/bin/env python3

import newsdb


def show_top_articles():
    print("searching for articles...\n")
    break_line_print()
<<<<<<< HEAD
    results = newsdb.get_top3_articles_by_num_views()
=======
    results = newsdb.get_top_3_articles_by_num_views()
>>>>>>> 5e2173e6b781c1f0bc82f21d1f96d080a75baa32
    print("***Top articles***")
    show_results("articles", results)


def show_top_authors():
    print("searching for authors...")
    break_line_print()
    results = newsdb.get_top_authors_by_num_views_articles()
    print("***Top authors***")
    show_results("authors", results)


def show_errors_on_request():
    print("searching for errors on request...")
    break_line_print()
    results = newsdb.get_error_request_by_day_more_than_1percent()
    print("***Errors request more then 1 percent of total by day***")
    show_results("errors on request", results)


def show_results(name_search, results):
    if (results.count > 0):
        for result in results:
            print(result)
    else:
        print("not found " + name_search)


def break_line_print():
    print("")


def main():
    break_line_print()
    show_top_articles()

    break_line_print()
    show_top_authors()

    break_line_print()
    show_errors_on_request()
    break_line_print()


main()
