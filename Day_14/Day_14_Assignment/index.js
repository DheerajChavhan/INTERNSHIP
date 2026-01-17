// Q1 (Spread Operator): Merge and Update Cart

const cart = ["Shoes", "T-Shirt"];
const newItems = ["Cap", "Socks"];

const updatedCart=["wallet",...cart, ...newItems];
console.log(updatedCart)

// Q2 (Spread Operator): Copy Object + Add Discount

const product = {
  name: "Laptop",
  price: 60000
};

const discountedProduct={...product,discount:10};
discountedProduct.price= discountedProduct.price - (discountedProduct.price * discountedProduct.discount / 100);
console.log(product)
console.log(discountedProduct)

// Q3 (Destructuring): Extract Values from an Object

const user = {
  id: 101,
  name: "Chandra",
  city: "Hyderabad",
  skills: ["JS", "React", "Node"]
};

const{id,name,city,skills:[skill1,skill2,skill3]}=user
console.log(name,city)
console.log(skill1,skill2)
console.log(`${name} lives in ${city} and knows ${skill1} and ${skill2}`)

// Q4 (Destructuring + Function): Student Report

const students = [
  { name: "Akhil", marks: [80, 75, 90] },
  { name: "Priya", marks: [60, 70, 65] }
];

function printStudentAverage(students) {
  for (const student of students) {
    
    const { name, marks } = student;

    let sum = 0;
    for (let i = 0; i < marks.length; i++) {
      sum += marks[i];
    }
    const average = sum / marks.length;

    console.log(`${name} average: ${average}`);
  }
}
printStudentAverage(students);

// Q5 (Modules in JS): Create and Use a Utility Module

import {add,multiply} from "./mathUtils.js"
console.log(`Sum: ${add(12,8)}`)
console.log(`Product: ${multiply(12,8)}`)