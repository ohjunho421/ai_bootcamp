SELECT 
HISTORY_ID,
CAR_ID,
date_format(START_DATE,"%Y-%m-%d")as start_date,
date_format(END_DATE,"%Y-%m-%d")as end_date,
if(datediff(end_date,start_date)>=29,"장기 대여","단기 대여") as RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date like "2022-09%"
order by history_id desc