-- 생성
-- 1. employees 테이블을 생성해주세요
CREATE DATABASE database_day03;  -- 데이터베이스 생성 (데이터베이스명 : database_day03)
USE database_day03;  -- 해당 데이터베이스를 사용하겠다! // 이 라인 없이 CREATE TABLE 명령하면 에러났음
CREATE TABLE employees( -- 선택된 데이터베이스 안에 employees 라는 테이블을 생성 
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2)
);

-- 2. 직원 데이터를 employees에 추가해주세요.
INSERT INTO employees (name, position, salary)
VALUES ("혜린", "PM", 90000),
("은우", "Frontend", 8000),
("가을", "Backend", 92000),
("지수", "Frontend", 78000),
("민혁", "Frontend", 96000),
("하은", "Backend", 130000);