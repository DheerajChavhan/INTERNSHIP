console.log("Hello World")
console.log("Internship Program")

// var x=20
let x=20
console.log(x)

// var y= 10                  // The value of y can be changed later        
let y=10                      // The value of y can not be changed later
console.log(y)

// var country="India"
let country="India"
console.log(country)

const a =null
console.log(a)

// The key should not be inside the inverted column in js 
const user={                  //When we code in js always use const forgot about var and let
    name:"Dheeraj",
    isLoggedIn:true,
    skills:["Python","Sql","Machine Learning"]
}

console.log("Hello", user.name)
console.log(user.skills.length)  //length of skills

if (user.isLoggedIn){
    console.log("Welcome Back")
}

function greet(student){
    // console.log("Welcome Home",student)
    console.log(`Welcome Home ${student}`)    // work as f strings in js
}
greet("Dheeraj")

// Normal Function with return value
// function sum(a,b){
//     c=a+b
//     return(`Sum of numbers is: ${c}`)
// }
// let res=sum(10,20)   // if we are returning the value we should store it in a variable and then print it 
// console.log(res)

// Arrow Function
const sum=(a,b)=>{
    c=a+b
    console.log(`Sum of numbers is: ${c}`)
}
sum(10,20)

// For Loop
for (let i=0; i<5; i++){
    console.log(i)
}

const numbers=[2,4,6,5,7,9,3]
for (let i = 0; i<=numbers.length;i++){
    console.log(numbers[i])
}