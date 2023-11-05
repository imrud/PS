-- 코드를 입력하세요
SELECT b.BOOK_ID, a.AUTHOR_NAME, DATE_FORMAT(b.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
from book b join author a
on b.AUTHOR_ID = a.AUTHOR_ID
where b.category = "경제"
order by PUBLISHED_DATE