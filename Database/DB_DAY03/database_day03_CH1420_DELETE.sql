-- 생성
-- 1. employees 테이블을 생성해주세요
-- CREATE DATABASE database_day03;  -- 데이터베이스 생성 (데이터베이스명 : database_day03)
-- USE database_day03;  -- 해당 데이터베이스를 사용하겠다! // 이 라인 없이 CREATE TABLE 명령하면 에러났음
-- CREATE TABLE employees( -- 선택된 데이터베이스 안에 employees 라는 테이블을 생성 
-- 	id INT PRIMARY KEY AUTO_INCREMENT,
--     name VARCHAR(100),
--     position VARCHAR(100),
--     salary DECIMAL(10, 2)
-- );

-- 2. 직원 데이터를 employees에 추가해주세요.
-- INSERT INTO employees (name, position, salary)
-- VALUES ("혜린", "PM", 90000),
-- ("은우", "Frontend", 8000),
-- ("가을", "Backend", 92000),
-- ("지수", "Frontend", 78000),
-- ("민혁", "Frontend", 96000),
-- ("하은", "Backend", 130000);

-- 읽기
-- 3. 모든 직원의 이름과 연봉 정보만을 조회하는 쿼리를 작성해주세요.
-- SELECT name, salary FROM employees;

-- 4. Frontend 직책을 가진 직원 중에서 연봉이 90000 이하인 직원의 이름과 연봉을 조회하세요.
-- SELECT name, salary FROM employees WHERE position = "Frontend" AND salary <= 90000;

-- 5. PM 직책을 가진 모든 직원의 연봉을 10% 인상한 후 그 결과를 확인하세요.
-- SELECT name, position, salary, salary * 1.1 AS "연봉 10% 인상" FROM employees WHERE position = "PM";

-- 갱신
-- 6. 모든 Backend 직책을 가진 직원의 연봉을 5% 인상하세요.
-- SET SQL_SAFE_UPDATES = 0; -- 세이프 모드 비활성화, UPDATE문 사용을 위함 // UPDATE문은 위험한 명령이기에 기본적으로 세이프모드가 활성화되어있다.
-- UPDATE employees
-- SET salary = salary * 1.05
-- WHERE position = "Backend"


-- 삭제 외
-- 7. 민혁 사원의 데이터를 삭제하세요
DELETE FROM employees WHERE name = "민혁";

-- 8. 모든 직원을 position 별로 그룹화하여 각 직책의 평균 연봉을 계산하세요.
SELECT position, AVG(salary) as avg_salary FROM employees GROUP BY position;

-- 9. employees 테이블을 삭제하세요.
DROP TABLE employees;