-- 코드를 입력하세요
SELECT u.user_id, u.nickname, sum(b.price) as total_sales
from used_goods_board b
left join used_goods_user u
on u.user_id = b.writer_id
where b.status = 'done'
group by u.user_id
having sum(b.price)>=700000
order by total_sales
