#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import newsdb


def show_top_articles():
    print("searching for articles...\n")
    break_line_print()
    results = newsdb.get_top_3_articles_by_num_views()
    print("1. Who are the authors of the most popular articles of all time?")
    break_line_print()
    show_results("articles", results)


def show_top_authors():
    print("searching for authors...")
    break_line_print()
    results = newsdb.get_top_authors_by_num_views_articles()
    print("2. Who are the authors of the most popular articles of all time?")
    break_line_print()
    show_results("authors", results)


def show_errors_on_request():
    print("searching for errors on request...")
    break_line_print()
    results = newsdb.get_error_request_by_day_more_than_1percent()
    print("3. On what days more than 1% of requests resulted in errors?")
    break_line_print()
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
    print("Reporter tool - by MarksDev")

    break_line_print()
    show_top_articles()

    break_line_print()
    show_top_authors()

    break_line_print()
    show_errors_on_request()
    break_line_print()


if __name__ == '__main__':
        main()


