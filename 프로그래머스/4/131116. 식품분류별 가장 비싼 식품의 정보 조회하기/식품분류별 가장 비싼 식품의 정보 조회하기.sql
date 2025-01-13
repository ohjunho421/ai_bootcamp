-- 코드를 입력하세요
SELECT CATEGORY, price, PRODUCT_NAME
from food_product
where (category,price) in (select category, max(price) as PRICE 
from food_product group by category having category in('과자','국','김치','식용유'))
order by price desc