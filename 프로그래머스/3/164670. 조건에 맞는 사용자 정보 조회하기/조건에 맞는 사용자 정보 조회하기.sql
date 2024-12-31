-- 코드를 입력하세요
SELECT u.USER_ID,u.NICKNAME, 
concat(u.city,' ',u.street_address1,' ',u.street_address2) as 전체주소, 
insert(insert(u.TLNO,4,0,'-'), 9,0,'-') as 전화번호

from used_goods_user u
join used_goods_board g
on g.writer_id = u.user_id

group by g.writer_id
having count(*)>=3
order by u.user_id desc