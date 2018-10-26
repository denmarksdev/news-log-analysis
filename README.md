# News Log Analysis
Create a reporter tool to **Analysis database news**, answering the following questions:
- What are the three most popular articles of all time?
- Who are the authors of the most popular articles of all time?
- On what days more than 1% of requests resulted in errors? 

# Requirements
- [Python 3.7](https://www.python.org/downloads/)
- [PostgreSQL 9.5](https://www.postgresql.org/download/)

# Usage
   
1. Download [news database sample](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
2. Run the command  `$ psql -d news -f newsdata.sql` to create database news 
3. Create follow view in database news:
```
CREATE VIEW view_top_article_by_views AS
	SELECT articles.title, articles.author, COUNT(log.*) AS views
	FROM articles, log
	WHERE  log.path LIKE ('/article/' || articles.slug)
	GROUP BY articles.title, articles.id, articles.author 
	ORDER BY views DESC;```
```
```
CREATE VIEW view_errors_request_by_day_more_than_1percent AS
	SELECT to_char(date_error,'FMMon FMDD, YYYY'), round(percent_error,2) || '%'  AS percent FROM ( 
		SELECT *, ((error * 100)::numeric / access ) as percent_error FROM 
			(SELECT time::date as date_total, COUNT(time) AS access 
		 FROM log
			 GROUP BY date_total) AS total,
			(SELECT time::date as date_error, COUNT(time) AS error
			 FROM log
			 WHERE status LIKE '4%'
			 GROUP BY date_error) as errors 
		WHERE total.date_total = errors.date_error 
		ORDER BY total.date_total
	) AS result
	WHERE percent_error > 1;
```
4. Run the command `$ python news.py` to start reporter tool!     
