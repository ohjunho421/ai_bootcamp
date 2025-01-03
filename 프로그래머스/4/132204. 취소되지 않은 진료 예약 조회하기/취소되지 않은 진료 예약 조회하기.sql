-- 코드를 입력하세요
SELECT a.APNT_NO, p.PT_NAME,p.PT_NO,d.MCDP_CD,d.DR_NAME,a.APNT_YMD
from appointment a
join doctor d on a.MDDR_ID = d.DR_ID
join patient p on a.PT_NO = p.PT_NO 
where a.APNT_YMD like '2022-04-13%' and a.APNT_CNCL_YN = 'N' and d.MCDP_CD = 'CS'
order by a.APNT_YMD