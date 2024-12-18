SELECT book.category, sum(book_sales.sales) as Total_sales
from book
right join book_sales
on book.book_id = book_sales.book_id
where book_sales.sales_date between '2022-01-01' and '2022-01-31' 
group by category
order by category