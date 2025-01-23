// 생성
//db.createCollection("users", {capped:false})

// 이름바꾸기
//db.users.renameCollection("customers")

// 삭제하기
//db.customers.drop() // 삭제는 됐지만, 눈에만 안 보이는 것? db라고 명령어 검색하면 뜸 // 근데 show dbs로 하면 안뜨긴
//show dbs

//db.dropDatabase()
//db



// use mongodbtest;
//db.createCollection("users", {capped:false})
//db.users.insertOne({name: "Alice", age:30, address: "123 Maple St"})
//db.users.find()
// 데이터를 리스트형태로 넣을수도 있다. // 아래의 테이블에서 3elements를 더블클릭하면 리스트를 볼 수 있음 
//db.users.insertOne({name: "Alice", age:30, address: ["123 Maple St", "124 Maple St", "125 Maple St"]})
//db.users.find()

// 여러개의 데이터 넣을 때 (insertmany)   데이터1개 넣을 때 (insertone)
//db.users.insertMany([
//    { name: "Bob", age: 25, address: "456 Oak St" },
//    { name: "Charlie", age: 35, city: "California" }
//])
//
//// 조회
//db.users.find({}, {name:1})  // 앞에 {} 꼭 붙여야함!!
//db.users.find({}, {name:1, address:1})
//db.users.find({}, {address:"Maple"})
//db.users.find({}, {age:30, address:"Maple"})


// 갱신(update)
db.users.updateOne({name:"Alice"}, {$set: {age:31}})  // 이떄는 앞에 {}가 없어도됨  // 이거하면 첫번째 앨리스만 바뀜 (첫번째 데이터만 바뀜)
db.users.find()

db.users.updateMany({name:"Alice"}, {$set: {age:31}})  // 매니를 붙이면 앨리스인 애들 전부 바뀜


// 삭제 (delete)
db.users.deleteOne({name:"Alice"})
db.users.deleteMany({name:"Bob"})


//연습문제(작성만해보기)
// 초급레벨
// 1. db.sports.insertOne({name:"Football", players: 11})
// 2-1. db.products.find({}, {price: {$lte: 500}})
// 2-2. db.books.find({}, {author:"John Doe})
// 3-1. db.orders.updateMany({status:"Pending"}, {$set: {status:"Complete"}})
// 3-2. db.movies.updateMany({genre:"comedy"}, {$set: {rating:5}})
// 4. db.customers.deleteMany({age:{$lt:30}})

// 중급레벨
// 1. db.myCollection.insertOne({name:"Gadget", type:"Eletronics", price:300, ratings:[4, 5, 5]})
// 2-1. db.employees.find({department:"Sales", age:{$gte:30}})
// 2-2. db.employees.find({salary:{$gte:50000}}, {name:1, title:1}) 
// 3-1. db.products.updateMany({stock:{$exists:false}}, {$set:{stock:10}})
// 3-2. db.vehicles.updateMany({type:"car"}, {$set:{wheels:4}})
// 4-1. db.orders.deleteMany({orderDate:{$lt:new Date('2023-01-01')}})
// 4-2. db.restaurants.deleteMany({rating: {$lt:3}})

// 고급레벨
// 1-1. db.customers.find({age:{$gte:30}}).sort({name:1})
// 1-2. db.users.aggregate([{$match: { birthdate: { $lt: new Date('1990-01-01') }}},{$group:{_id: null, avgAge: { $avg: "$age" }}}])
// 2-1. db.employees.updateMany({department:"HR"}, {$set:{department:"Human Resources", title:"HR Manager"})
// 2-2. db.orders.updateMnay({delivered:false}, {$set:{deliveryDate:new Date()})
// 3-1. db.products.deleteMany({lastModified:{$lt: new Date(new Date() - 30 * 24 * 60 * 60 * 1000)}})
// 3-2. db.products.deleteMany({stock:0)


// 연습문제
// 1. db.products.find({}, {pritc: {$gt:100}})
// 2. db.employees.find({}, $or: [{age: {$lt:30}}, {department:"HR"}]})
// 3. db.orders.find({}, {quantity: {$gte:5, $lte:10}})
// 4. db.customers.find({}, {city: {$ne: "Seoul"}})
// 5. db.movies.find({}, {rating: {$gt:8}, genre: {$in:["comedy", "drama"]}})
// 6. db.books.find({}, {author:"John Doe", pulishedYear: {$gt: 2000}})
// 7. db.vehicles.find({}, {type: {$ne: "car"}, {price: {$gt:20000}})
// 8. db.restaurants.find({}, {rating:5}, cuisine: {$nin: ["Italian", "French"]}})
// 9. db.users.find({}, {age: {$gt:30}, city: {$ne: "New York"}})
// 10. db.flights.find({}, $or: [{departure: "London"}, {arrival: "Tokyo"}]})