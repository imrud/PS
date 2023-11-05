-- 코드를 입력하세요
select fp.PRODUCT_ID, fp.PRODUCT_NAME, sum(fo.amount*fp.price)as TOTAL_SALES
from food_product fp join food_order fo
on fp.product_id = fo.product_id
where DATE_FORMAT(PRODUCE_DATE,'%Y-%m')  = '2022-05'
group by fo.product_id
order by TOTAL_SALES desc, fp.PRODUCT_ID