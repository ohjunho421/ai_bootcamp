SELECT
    case
        when product_id in (1 ,2) then 'A1'
        when product_id in (3 ,4 ,5) then 'C3'
        when product_id in (6) then 'K1'
    end as CATEGORY,
    count(product_id) as products
from product
where product_id in(1,2,3,4,5,6)
GROUP BY CATEGORY;