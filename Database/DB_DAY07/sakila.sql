-- 데이터 조회 및 필터링
-- 'GUINESS PENELOPE'가 출연한 모든 영화의 제목을 조회하시오.
-- SELECT f.title FROM film f
-- JOIN film_actor fa ON f.film_id = fa.film_id
-- JOIN actor a ON fa.actor_id = a.actor_id
-- WHERE a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS';

-- 각 카테고리별로 몇 개의 영화가 있는지 조회하시오.
-- SELECT category_id, COUNT(*) count_film FROM film f
-- JOIN film_category fc ON f.film_id = fc.film_id
-- GROUP BY category_id ORDER BY category_id 

-- 고객 ID가 5인 고객의 모든 대여 기록을 조회하시오.
-- SELECT r.*, f.* FROM rental r 
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- WHERE r.customer_id = 5

-- 가장 최근에 데이터베이스에 추가된 10개의 영화 제목을 조회하시오.
-- SELECT title, release_year FROM film
-- ORDER BY release_year DESC LIMIT 10


-- 조인 및 관계
-- 'ACADEMY DINOSAUR' 영화에 출연한 모든 배우의 이름을 조회하시오.
-- SELECT a.actor_id, a.first_name, a.last_name FROM actor a
-- JOIN film_actor fa ON a.actor_id = fa.actor_id
-- JOIN film f ON fa.film_id = f.film_id
-- WHERE f.title = 'ACADEMY DINOSAUR'

-- 'ACADEMY DINOSAUR' 영화를 대여한 모든 고객의 이름을 조회하시오.
-- SELECT c.customer_id, c.first_name, c.last_name FROM customer c
-- JOIN rental r ON c.customer_id = r.customer_id
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- WHERE f.title = 'ACADEMY DINOSAUR'

-- 각 고객별로 가장 최근에 대여한 영화의 제목을 조회하시오.
-- SELECT c.customer_id, MAX(r.rental_date) lately_date, f.title  FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- JOIN customer c ON r.customer_id = c.customer_id
-- GROUP BY c.customer_id, f.title
-- ORDER BY lately_date DESC 

-- 각 영화별 평균 대여 기간을 일 단위로 계산하시오.
-- SELECT f.title, AVG(DATEDIFF(r.return_date, r.rental_date)) AS avg_duration
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- GROUP BY f.title


-- 집계 및 그룹화
-- 가장 많이 대여된 영화의 제목과 대여 횟수를 조회하시오.
-- SELECT f.title, COUNT(i.film_id) count_rental FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- GROUP BY f.title
-- ORDER BY count_rental DESC LIMIT 1

-- 각 카테고리별 평균 대여 요금을 계산하시오.
-- SELECT c.category_id, c.name, AVG(p.amount) avg_payment
-- FROM category c
-- JOIN film_category fc ON c.category_id = fc.category_id
-- JOIN film f ON fc.film_id = f.film_id
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- JOIN payment p ON r.rental_id = p.rental_id
-- GROUP BY c.category_id, c.name

-- SELECT c.name, AVG(f.rental_rate) as average_rental_rate
-- FROM category c
-- JOIN film_category fc ON c.category_id = fc.category_id
-- JOIN film f ON fc.film_id = f.film_id
-- GROUP BY c.name;

-- 각 월별로 총 매출액을 계산하시오.
-- SELECT YEAR(payment_date) year_payment, MONTH(payment_date) month_payment, SUM(amount) FROM payment
-- GROUP BY year_payment, month_payment
-- ORDER BY month_payment, year_payment

-- 각 배우별로 출연한 영화 수를 계산하시오.
-- SELECT a.actor_id, a.first_name, a.last_name, COUNT(film_id) count_film
-- FROM actor a
-- JOIN film_actor fa ON a.actor_id = fa.actor_id
-- GROUP BY a.actor_id, a.first_name, a.last_name


-- 서브쿼리 및 고급 기능
-- 가장 많은 수익을 낸 영화의 제목과 수익을 조회하시오.
-- SELECT f.film_id, f.title, SUM(p.amount) AS profit
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- JOIN payment p ON r.rental_id = p.rental_id
-- GROUP BY f.film_id, f.title
-- ORDER BY profit DESC LIMIT 1

-- 평균 대여 요금보다 높은 요금의 영화 제목과 요금을 조회하시오.
-- SELECT title, rental_rate FROM film
-- WHERE rental_rate > (SELECT AVG(rental_rate) FROM film)

-- 가장 많은 영화를 대여한 고객의 이름과 대여 횟수를 조회하시오.
-- SELECT c.customer_id, c.first_name, c.last_name, COUNT(r.customer_id) count_rental
-- FROM customer c
-- JOIN rental r ON c.customer_id = r.customer_id
-- GROUP BY c.customer_id, c.first_name, c.last_name
-- ORDER BY count_rental DESC LIMIT 1

-- 배우 'PENELOPE GUINESS'가 출연한 영화 중 가장 많이 대여된 영화의 제목과 대여 횟수를 조회하시오.
-- SELECT a.first_name, a.last_name, f.title, COUNT(f.title) count_title
-- FROM actor a
-- JOIN film_actor fa ON a.actor_id = fa.actor_id
-- JOIN film f ON fa.film_id = f.film_id
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- WHERE a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS'
-- GROUP BY  f.title
-- ORDER BY count_title DESC LIMIT 1


-- 데이터 수정 및 관리
-- 'film' 테이블에 'New Adventure Movie'라는 새로운 영화를 추가하시오.
-- INSERT INTO film (title, description, release_year,language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features)
-- VALUES ('New Adventure Movie', 'A thrilling adventure of the unknown', 2023, 1, 3, 4.99, 120, 19.99, 'PG', 'Trailers,Commentaries')

-- 고객 ID가 5인 고객의 주소를 '123 New Address, New City'로 변경하시오.
-- (아래의 쿼리문을 사용하면, address의 값 자체를 바꿔버림)
-- UPDATE customer c
-- JOIN address a ON c.address_id = a.address_id
-- SET a.address = '123 Incheon'
-- WHERE c.customer_id = 5

-- (아래의 쿼리문을 사용하면, 주소록을 변경 해줌 // 단, 기존의 주소록에 존재해야함)
-- SET foreign_key_checks = 0;
-- UPDATE customer
-- SET address_id = CASE
-- 	WHEN (SELECT address_id FROM address WHERE address = '123 New Address, New City') IS NULL THEN 0
--     ELSE (SELECT address_id FROM address WHERE address = '123 New Address, New City')
-- END
-- WHERE customer_id = 5;
-- SET foreign_key_checks = 1

-- 대여 ID가 200인 대여 기록의 상태를 'returned'로 변경하시오. ???
-- UPDATE rental
-- SET return_date = NOW()
-- WHERE rental_id = 200

-- 배우 ID가 10인 배우의 정보를 삭제하시오.  // actor_id 키를 참조하고 있는 곳의 데이터를 먼저 삭제한 후 삭제해야한다. 아님 에러남!!
-- 방법은 2가지? 1. 참조하는곳의 데이터를 먼저 삭제하기 2. 일시적으로 참조키 체크 해제 하기 (0 -> 1 로 값을 제때 변경해줘야함 // 왜냐 데이터를 임시로 손을 대는거니까)
-- DELETE FROM film_actor WHERE actor_id = 10
DELETE FROM actor WHERE actor_id = 10



