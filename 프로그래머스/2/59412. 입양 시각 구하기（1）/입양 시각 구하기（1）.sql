-- 코드를 입력하세요
SELECT date_format(datetime,'%H')as hour, count(*) as count
from animal_outs
where date_format(datetime,'%H') between 09 and 19
group by hour
order by hour