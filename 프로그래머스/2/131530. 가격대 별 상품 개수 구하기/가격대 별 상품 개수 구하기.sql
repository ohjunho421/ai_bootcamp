-- 코드를 입력하세요
SELECT floor(price/10000)*10000 as price_group,
count(*) as products
from product
where price is not null
group by floor(price/10000)
order by floor(price/10000)