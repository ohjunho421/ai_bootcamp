-- 코드를 입력하세요
SELECT BOARD_ID,WRITER_ID,TITLE,PRICE, 
CASE WHEN STATUS='sale' THEN '판매중'
     WHEN STATUS='reserved' then '예약중'
     else '거래완료'end AS STATUS
FROM USED_GOODS_BOARD
where created_date = '2022-10-05'
order by board_id desc