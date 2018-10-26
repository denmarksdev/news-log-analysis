import newsdb


def show_top_articles():
    print("***Show top articles***")
    print("searching...")
    results = newsdb.get_top_articles_by_num_views()
    for result in results:
        print(result)


def show_top_authors():
    print("***Show top authors***")
    print("searching...")
    results = newsdb.get_top_authors_by_num_views_articles()
    for result in results:
        print(result)


def show_errors_on_request():
    print("***Show errors request more then 1 percent of total by day***")
    print("searching...")
    results = newsdb.get_errors_request_by_day_more_than_1percent()
    for result in results:
        print(result)


def main():
    show_top_articles()
    print("")
    show_top_authors()
    print("")
    show_errors_on_request()


if (__name__ == "main"):
    main()
