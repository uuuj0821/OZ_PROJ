// console.log("hello world");
// console.log(1 + 3);

// let num1 = 10
// let num2 = 20

// console.log(num1 * num2);

// 유저가 버튼을 클릭했을 때 특정한 동작이 실행되도록 만들고 싶다.
// class : . , id : #
const btn = document.querySelector('#button')
const num = document.querySelector('#number')
console.log(btn);
console.log(num);

// 특정한 동작? == 함수
// addEventListener는 2개의 전달인자를 갖는다.
// 첫번째 전달인자 : 이벤트의 종류
// 두번째 전달인자 : 함수
btn.addEventListener('click', function () {
    num.textContent = Number(num.textContent) + 1;
})