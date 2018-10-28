-- Show most top articles views

CREATE VIEW view_top_article_by_views AS
	SELECT articles.title, articles.author, COUNT(log.*) AS views
	FROM articles, log
	WHERE  log.path  CONCAT('/article/',articles.slug)
	GROUP BY articles.title, articles.id, articles.author 
	ORDER BY views DESC;

--

-- Em quais dias mais de 1% das requisições resultaram em erros?

CREATE VIEW view_errors_request_by_day_more_than_1percent AS
	SELECT to_char(date_error,'FMMon FMDD, YYYY'), round(percent_error,2) || '%'  AS percent FROM ( 
		SELECT *, ((error * 100)::numeric / access ) as percent_error FROM 
			(SELECT time::date as date_total, COUNT(time) AS access 
		 FROM log
			 GROUP BY date_total) AS total,
			(SELECT time::date as date_error, COUNT(time) AS error
			 FROM log
			 WHERE log.status != '200 OK'
			 GROUP BY date_error) AS errors 
		WHERE total.date_total = errors.date_error 
		ORDER BY total.date_total
	) AS result
	WHERE percent_error > 1;