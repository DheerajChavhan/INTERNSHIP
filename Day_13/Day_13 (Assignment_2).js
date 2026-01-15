// Q1 Write a program that asks the user for a number and checks if it's even or odd, displaying an appropriate message.

number=prompt("Enter the number")
if (number % 2 ==0){
    console.log("The number is Even");
}
else{
    console.log("The number is Odd");
}

// Q2 Write a program to accept two numbers from the user using prompt() and alert() the maximum value.

num1=prompt("Enter First number")
num2=prompt("Enter Second number")

if(num1>num2){
    alert("The Maximum value is " + num1);
}
else{
    alert("The Maximum value is " + num2);
}

// Q3 Write a program that asks the user for a house name and checks specific conditions:
// If house name is "stark", print "Winter is coming"
// If house name is "lannister", print "A lannister always pays his debt"
// Otherwise, print "All men must die"

let House_name=prompt("Enter the House Name:")
if (House_name==="stark"){
    console.log("Winter is coming");
}
else if(House_name==="lannister"){
    console.log("A lannister always pays his debt");
}
else{
    console.log("All men must die");
}

// Q4 Write a program that takes the user's salary using prompt() and alerts the in-hand amount after tax deduction:
// Salary <= 20000: tax is 10%
// Salary <= 40000: tax is 20%
// Salary > 50000: tax is 30%

Salary=prompt("Enter the Salary:")
if (Salary <= 20000){
    Salary=Salary-Salary*0.1
    alert("The in-hand Amount after Tax Deduction is " + Salary);
}
else if(Salary <= 40000){
    Salary=Salary-Salary*0.2
    alert("The in-hand Amount after Tax Deduction is " + Salary);
}
else{
    Salary=Salary-Salary*0.3
    alert("The in-hand Amount after Tax Deduction is " + Salary);
}

// Q5 Write a program that uses any loop structure to find and print the first 10 numbers in the Fibonacci sequence.

numbers=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

for(let i=0;i<11;i++){
    console.log(numbers[i]);
}