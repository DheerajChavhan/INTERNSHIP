const user={
    name:"Rohit",
    age:21,
    city:"Pune"
}
user.Occupation="Engineer"
user.name="Dheeraj"
console.log(user.name)
console.log(user)

// nested Object
const student={
    name:"Dheeraj",
    marks:{
        Science:89,
        Maths:100
    },
    Skills:["Python","React","JS"]
}
//Maths Marks
console.log(student.marks.Maths)
// React
console.log(student.Skills[1])

// Array Of Object
const users=[
    {id:1,Name:"Dheeraj",City:"Pune"},
    {id:2,Name:"Prem",City:"Sambhajinagar"}
];
console.log(users[0].Name)       //Dheeraj

// Object Destructuring
const User={NAME:"Dheeraj",AGE:21}
const {NAME,AGE}=User
console.log(NAME,AGE)

const person={name:"Dheeraj",Language:"Python",Country:"US"}
const{name,Language:Lang,Country="India"}=person    //Rename the Language Key and default value of Country
console.log(name,Lang,Country)

function printinfo(user_info){
const {name,location,language}=user_info    
console.log(`I am ${name} from ${location} and familiar with ${language}`)
}
const user_info={
    name:"Dheeraj",
    location:"India",
    language:"Python"
}
printinfo(user_info)

const book={title:"The Alchemist",author:"Paulo Coelho"};
const {title:bookTitle,author:Writer}=book
console.log(bookTitle,Writer)

// Named Import and Export
import {addition,multiply} from './math.js'         // import the addition multiply and divide function
addition(1,2,3)
multiply(4,5)                         

// Default import
import divide from './math.js'                      // Default function does not need brackets 
divide(4,2)

// For Loop
const arr1=[10,20,30,40,50]
const arr2=[]
for (let i=0;i<arr1.length;i++){ 
    arr2.push(arr1[i]*2)
}
console.log(arr2)

// Map Function(element,index,array)
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
const output=numbers.map(function(el){
    return (el*2)
})
console.log(output)

const Users=[
    {name:"John",age:25},
    {name:"Jane",age:30},
    {name:"Mike",age:20},
]
const out=Users.map(function(el){
    return (el.name)
})
console.log(out)

// Filter Function
// const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  Since it is already declared
const even=numbers.filter(function(el){
        return el%2==0
})
console.log(even)

const words = ['apple', 'banana', 'kiwi', 'mango']
const word=words.filter(function(el){
    return el.length>5
})
console.log(word)