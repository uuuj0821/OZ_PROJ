const form = document.getElementById("joinForm")
form.addEventListener("submit", function(e){
  e.preventDefault();  // submit 이벤트는 기본적으로 새로고침을 같이 진행함, 새로고침을 실행하지 않기 위해서 작성해야함.

  let userId = e.target.id.value
  let userPw1 = e.target.pw1.value
  let userPw2 = e.target.pw2.value
  let userName = e.target.name.value
  let userPhone = e.target.phone.value
  let userGender = e.target.gender.value
  let userEmail = e.target.email.value

  console.log(userId, userPw1, userPw2, userName,
    userPhone, userGender, userEmail)

  if(userId.length < 6){
    alert("아이디가 너무 짧습니다. 6자 이상 입력해주세요.")
    return;
  }

  if(userPw1 !== userPw2){
    alert("비밀번호가 일치하지 않습니다.")
    return;
  }

  alert(
    `${userId}님 환영합니다.
    회원 가입 시 입력하신 내역은 다음과 같습니다.
    아이디 : ${userId}
    이름 : ${userName}
    전화번호 : ${userPhone}
    이메일 : ${userEmail}
    `)

    goToAnotherPage()
})


// 현재 날짜 및 시간 업데이트
function updateDateTime() {
    const now = new Date();
    document.getElementById("currentDateTime").innerText = now.toLocaleString();
    }
    setInterval(updateDateTime, 1000);
    updateDateTime();

// 다크 모드 기능
function toggleDarkMode() {
document.body.classList.toggle("dark-mode");
const isDarkMode = document.body.classList.contains("dark-mode");
localStorage.setItem("darkMode", isDarkMode);
}

// 페이지 로드 시 다크 모드 설정 확인
if (localStorage.getItem("darkMode") === "true") {
document.body.classList.add("dark-mode");
}

// 회원가입 폼 토글
function toggleSignUpForm() {
const form = document.getElementById("signUpForm");
form.style.display = (form.style.display === "none" || form.style.display === "") ? "block" : "none";
}

// 회원 가입 완료 시 화면 전환
function goToAnotherPage() {
    window.location.href = "sign_up.html";
}

// 제품 데이터
const product_data = [
{ category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티1', price: '1390,000' },
{ category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티2', price: '2390,000' },
{ category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티3', price: '3390,000' },

{ category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠1', price: '1,188,000' },
{ category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠2', price: '2,188,000' },
{ category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠3', price: '3,188,000' },

{ category: "신발", brand: 'Nike', product: '에어포스 11', price: '337,000' },
{ category: "신발", brand: 'Nike', product: '에어포스 12', price: '437,000' },
{ category: "신발", brand: 'Nike', product: '에어포스 13', price: '537,000' },

{ category: "패션잡화", brand: 'Music&Goods', product: '빵빵이1 키링', price: '229,000' },
{ category: "패션잡화", brand: 'Music&Goods', product: '빵빵이2 키링', price: '329,000' },
{ category: "패션잡화", brand: 'Music&Goods', product: '빵빵이3 키링', price: '429,000' },
{ category: "패션잡화", brand: 'Music&Goods', product: '빵빵이4 키링', price: '529,000' },

];

const product_data_Table = document.getElementById('product_data_Table');
    const itemsPerPage = 4; // 한 페이지당 보여줄 아이템 수
    let currentPage = 1;

function renderTable(data, page = 1) {
product_data_Table.innerHTML = "";
const start = (page - 1) * itemsPerPage;
const end = start + itemsPerPage;
const paginatedData = data.slice(start, end);

paginatedData.forEach((item) => {
    const row = product_data_Table.insertRow();
    row.insertCell(0).innerHTML = item.category;
    row.insertCell(1).innerHTML = item.brand;
    row.insertCell(2).innerHTML = item.product;
    row.insertCell(3).innerHTML = item.price;
});

renderPagination(data.length);
}

function renderPagination(totalItems) {
const totalPages = Math.ceil(totalItems / itemsPerPage);
const pagination = document.getElementById("pagination");
pagination.innerHTML = "";

for (let i = 1; i <= totalPages; i++) {
    const li = document.createElement("li");
    li.classList.add("page-item");
    if (i === currentPage) li.classList.add("active");
    
    const a = document.createElement("a");
    a.classList.add("page-link");
    a.href = "#";
    a.innerText = i;
    a.onclick = function () {
    currentPage = i;
    renderTable(product_data, currentPage);
    };

    li.appendChild(a);
    pagination.appendChild(li);
}
}

function filterProducts() {
const category = document.getElementById("inlineFormSelectPref").value;
const searchQuery = document.getElementById("searchInput").value.toLowerCase();

const filteredData = product_data.filter(item =>
    (category === "" || item.category === category) &&
    (searchQuery === "" || item.product.toLowerCase().includes(searchQuery))
);

currentPage = 1;
renderTable(filteredData, currentPage);
}

renderTable(product_data);