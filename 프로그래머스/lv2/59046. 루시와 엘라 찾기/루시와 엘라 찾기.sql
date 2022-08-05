-- 코드를 입력하세요
SELECT ins.ANIMAL_ID, ins.NAME, ins.SEX_UPON_INTAKE from ANIMAL_INS as ins
where ins.NAME in ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')
ORDER BY ins.ANIMAL_ID