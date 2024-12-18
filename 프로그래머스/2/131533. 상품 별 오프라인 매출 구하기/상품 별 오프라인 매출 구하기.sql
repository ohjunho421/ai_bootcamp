-- 코드를 입력하세요
SELECT product.product_code, sum(product.price * offline_sale.sales_amount) as sales
from product
left join offline_sale
on product.product_id=offline_sale.product_id
group by product_code
order by sales desc, product_code
