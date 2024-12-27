-- 코드를 입력하세요
SELECT c.car_id
from car_rental_company_car c
inner join car_rental_company_rental_history r
on c.car_id = r.car_id
where c.car_type = '세단'and r.start_date like '2022-10-%'
group by 1
order by 1 desc