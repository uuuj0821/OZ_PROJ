-- [Database Day02 과제1]
-- USE mysql;  -- 유저확인
-- CREATE USER 'fishbread_user'@'localhost' IDENTIFIED BY '0701'  -- 유저생성
-- GRANT ALL PRIVILEGES ON *.* TO 'fishbread_user'@'localhost';   -- 권한부여(모든 데이터베이스에 대한 권한 부여)
-- FLUSH PRIVILEGES;  -- 변경된 권한 적용
-- SHOW GRANTS FOR 'fishbread_user'@'localhost';  -- 부여된 권한 확인
-- SHOW GRANTS;   -- 현재 로그인한 유저의 권한 확인

-- [Database Day02 과제2]
-- 1. 데이터베이스 생성
CREATE DATABASE fishbread_db;
USE fishbread_db;

-- 2. users 테이블 생성
CREATE TABLE users(
	user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100) UNIQUE,
    is_business VARCHAR(10) DEFAULT False    
);

-- 3. orders 테이블 생성
CREATE TABLE orders(
	order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    order_data DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- 4. inventory 테이블 생성
CREATE TABLE inventory(
	item_id INT PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL
);

-- 5. sales 테이블 생성
CREATE TABLE sales(
	sale_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    item_id INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (item_id) REFERENCES inventory(item_id),
    quantity_sold INT NOT NULL
);

-- 6. daily_sales 테이블 생성
CREATE TABLE daily_sales(
	data DATE PRIMARY KEY,
    total_sales DECIMAL(10,2) NOT NULL
);