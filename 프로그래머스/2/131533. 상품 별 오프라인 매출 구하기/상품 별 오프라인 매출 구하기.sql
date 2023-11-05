-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, sum(o.sales_amount)*p.price as SALES
from product p join offline_sale o
on p.product_id = o.product_id
group by p.PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE ASC;