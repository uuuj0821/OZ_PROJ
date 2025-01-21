-- use yes24;

-- 3-1. 기본 조회 및 필터링
-- 모든 책의 제목과 저자를 조회하세요.
-- SELECT title, author FROM books;

-- 평점이 8 이상인 책 목록을 조회하세요.
 -- SELECT * FROM books WHERE rating >= 8;

-- 리뷰 수가 100개 이상인 책들의 제목과 리뷰 수를 조회하세요.
-- SELECT title, review FROM books WHERE review >= 100

-- 가격이 20,000원 미만인 책들의 제목과 가격을 조회하세요.
-- SELECT title, price FROM books WHERE price < 20000

-- 국내도서TOP100에 4주 이상 머문 책들을 조회하세요.
-- SELECT * FROM books WHERE ranking_weeks >= 4

-- 특정 저자의 모든 책을 조회하세요.
-- SELECT * FROM books WHERE author LIKE "%한강%"

-- 특정 출판사가 출판한 책들을 조회하세요.
-- SELECT * FROM books WHERE publisher LIKE "%이투스%"


-- 3-2. 조인 및 관계
-- 저자별로 출판한 책의 수를 조회하세요.
-- SELECT author, COUNT(author) AS count_publish FROM books GROUP BY author

-- 가장 많은 책을 출판한 출판사를 찾으세요.
-- SELECT publisher, COUNT(publisher) AS count_publish FROM books GROUP BY publisher
-- ORDER BY count_publish DESC LIMIT 1

-- 가장 높은 평균 평점을 가진 저자를 찾으세요.
-- SELECT author, AVG(rating) AS avg_rating FROM books GROUP BY author
-- ORDER BY avg_rating DESC LIMIT 1

-- 국내도서랭킹이 1위인 책의 제목과 저자를 조회하세요.
-- SELECT title, author FROM books WHERE ranking = 1

-- 판매지수와 리뷰 수가 모두 높은 상위 10개의 책을 조회하세요.
-- SELECT * FROM books ORDER BY sales DESC, review DESC LIMIT 10

-- 가장 최근에 출판된 5권의 책을 조회하세요.
-- SELECT * FROM books ORDER BY publishing DESC LIMIT 5


-- 3-3. 집계 및 그룹화
-- 저자별 평균 평점을 계산하세요.
-- SELECT author, AVG(rating) AS avg_rating FROM books GROUP BY author

-- 출판일별 출간된 책의 수를 계산하세요.
-- SELECT publishing, COUNT(*) AS count_publish FROM books GROUP BY publishing
-- ORDER BY publishing DESC

-- 책 제목별 평균 가격을 조회하세요.
-- SELECT title, AVG(price) AS avg_price FROM books GROUP BY title

-- 리뷰 수가 가장 많은 상위 5권의 책을 찾으세요.
-- SELECT * FROM books ORDER BY review DESC LIMIT 5

-- 국내도서랭킹 별 평균 리뷰 수를 계산하세요.
-- SELECT ranking, AVG(review) AS avg_review FROM books GROUP BY ranking


-- 3-4. 서브쿼리 및 고급 기능
-- 평균 평점보다 높은 평점을 받은 책들을 조회하세요
-- SELECT AVG(rating) FROM books
-- SELECT * FROM books WHERE rating > (SELECT AVG(rating) FROM books)

-- 평균 가격보다 비싼 책들의 제목과 가격을 조회하세요.
-- SELECT title, price FROM books WHERE price > (SELECT AVG(price) FROM books)

-- 가장 많은 리뷰를 받은 책보다 많은 리뷰를 받은 다른 책들을 조회하세요. ????
-- SELECT title, review FROM books WHERE review > (SELECT MAX(review) FROM books)

-- 평균 판매지수보다 낮은 판매지수를 가진 책들을 조회하세요.
-- SELECT title, sales FROM books WHERE sales < (SELECT AVG(sales) FROM books)

-- 가장 많이 출판된 저자의 책들 중 최근에 출판된 책을 조회하세요.
-- SELECT title, author, publishing FROM books 
-- WHERE author = (SELECT author FROM books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1)
-- ORDER BY publishing DESC LIMIT 1


-- 3-5. 데이터 수정 및 관리
-- 특정 책의 가격을 업데이트하세요.
-- UPDATE books SET price = 99999 WHERE bookID = 1

-- 특정 저자의 책 제목을 변경하세요.
-- SET SQL_SAFE_UPDATES = 0; -- (세이프 모드 비활성화)
-- UPDATE Books SET title = "제목업데이트" WHERE author LIKE "%한강%"

-- 판매지수가 가장 낮은 책을 데이터베이스에서 삭제하세요.
-- DELETE FROM books WHERE sales = (SELECT MIN(sales) FROM books)
-- DELETE FROM books WHERE sales = (SELECT min FROM (SELECT MIN(sales) AS min FROM books) AS T)
-- SELECT sales FROM (SELECT MIN(sales) FROM books) as t
-- SELECT min FROM (SELECT MIN(sales) AS min FROM books)

-- 특정 출판사가 출판한 모든 책의 평점을 1점 증가시키세요.
-- UPDATE books SET rating = rating + 1 WHERE publisher LIKE "%이투스%"


-- 3.6 데이터 분석 예제
-- 저자별 평균 평점 및 판매지수를 분석하여 인기 있는 저자를 확인합니다.
-- SELECT author, AVG(rating) AS avg_rating, AVG(sales) AS avg_sales
-- FROM books GROUP BY author
-- ORDER BY avg_rating DESC, avg_sales DESC LIMIT 1

-- 출판일에 따른 책 가격의 변동 추세를 분석합니다.
-- SELECT publishing, AVG(price) AS avg_price FROM books GROUP BY publishing
-- ORDER BY publishing DESC

-- 출판사별 출간된 책의 수와 평균 리뷰 수를 비교 분석합니다.
-- SELECT publisher, COUNT(*) AS count_publish, AVG(review) AS avg_review
-- FROM books GROUP BY publisher
-- ORDER BY count_publish DESC, avg_review DESC

-- 국내도서랭킹과 판매지수의 상관관계를 분석합니다.
-- SELECT ranking, AVG(sales) AS avg_sales FROM books GROUP BY ranking
-- ORDER BY avg_sales DESC

-- 가격 대비 리뷰 수와 평점의 관계를 분석하여 가성비 좋은 책을 찾습니다.
-- SELECT price, AVG(review) AS avg_review, AVG(rating) AS avg_rating
-- FROM books GROUP BY price
-- ORDER BY avg_rating DESC, avg_review DESC


-- 3.7 난이도 있는 문제
-- 출판사별 평균 판매지수가 가장 높은 저자 찾기
-- SELECT publisher, author, AVG(sales) AS avg_sales
-- FROM books
-- GROUP BY publisher, author
-- ORDER BY publisher, avg_sales DESC

-- 리뷰 수가 평균보다 높으면서 가격이 평균보다 낮은 책 조회
-- SELECT title FROM books
-- WHERE review > (SELECT AVG(review) FROM books) AND price < (SELECT AVG(price) FROM books)

-- 가장 많은 종류의 책을 출판한 저자 찾기
-- SELECT author, COUNT(DISTINCT title) AS count_publish FROM books GROUP BY author
-- -- DISTINCT : 유니크한값 조회, 중복 제거
-- ORDER BY count_publish DESC LIMIT 1

-- 각 저자별로 가장 높은 판매지수를 기록한 책 조회
-- SELECT author, MAX(sales) AS max_sales FROM books GROUP BY author

-- 연도별 출판된 책 수와 평균 가격 비교
-- SELECT YEAR(publishing) AS year_publish, COUNT(*) AS count_publish, AVG(price) AS avg_price
-- FROM books GROUP BY year_publish
-- ORDER BY year_publish DESC

-- 출판사가 같은 책들 중 평점 편차가 가장 큰 출판사 찾기
-- SELECT publisher, MAX(rating) - MIN(rating) AS difference_rating
-- FROM books GROUP BY publisher
-- ORDER BY difference_rating DESC LIMIT 1

-- 특정 저자의 책들 중 판매지수 대비 평점이 가장 높은 책 찾기
SELECT title, rating/sales AS ratio
FROM books
WHERE author LIKE "%최태성%"
ORDER BY ratio DESC LIMIT 1
