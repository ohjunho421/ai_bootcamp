-- 코드를 입력하세요
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, sum(price*amount) as TOTAL_SALES
from food_product p
left join food_order o
on p.product_id = o.product_id
where o.produce_date like '2022-05-%'
group by p.product_id
order by total_sales desc, p.product_id