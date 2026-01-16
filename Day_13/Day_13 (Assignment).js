// Part 1: Basic Arithmetic and Type Conversion

//Q 1.
console.log( 11 % 3)
//Q 2. 
console.log(1 + "JS")
//Q 3.
console.log( 1 * "JS")
//Q 4.
console.log( 5 + true)
//Q 5.
console.log(6 - true)
//Q 6.
console.log( 7 - false)
//Q 7.
console.log( 1 + 2 * 3 / 4)
//Q 8.
console.log( 8 + false)
//Q 9.
console.log( true + true)

// Exponentiation

// Q10.
console.log( 7 ** 2)
// Q11.
console.log( 2 ** 3)

// String Operations

// Q12.
console.log( "hello" + " " + "world")
// Q13.
console.log( "hello" * 10)

// Type Conversion

// Q14.
console.log( true + false)
// Q15.
console.log( +true)
// Q16.
console.log( +"21")
// Q17.
console.log( +null)


// Part 2: Increment and Assignment Operations

let count = 46;

// Q1.
 console.log(count++)
// Q2.
 console.log(++count)
// Q3.
 console.log(count++)
// Q4.
 console.log(++count)
// Q5.
 console.log(count++ + 10) 
// Q6.
 console.log(++count + 5) 
// Q7.
 console.log(count++)
// Q8.
 console.log(count += 10)
// Q9.
 console.log(count *= 5)


//  Part 3: Operator Precedence

// Basic Precedence
// Q1.
console.log( 3 + 4 * 5)
// Q2.
console.log( (25 + 28) + 105)
// Q3.
console.log( 4 * 3 ** 2)

// Comma Operator
// Q4.
console.log( 4, 400 + 10)
// Q5.
console.log( (4, 400) + 10)

// Mixed Type Operations
// Q6.
console.log( 3 + "10" * 2)
// Q7.
console.log( 3 + 10 * "2")
// Q8.
console.log( "3" + 10 * 2)
// Q9.
console.log( 3 + 10 * 2)

// Parentheses Priority
// Q10.
console.log( 3 + (10 * 2))
// Q11.
console.log( (3 + 10) * 2)  

// Exponentiation Right-to-Left Associativity
// Q12.
console.log( 2 ** 3 ** 2)
// Q13.
console.log( 2 ** (3 ** 2))
// Q14.
console.log( (2 ** 3) ** 2)

// Type Conversion with Operations
// Q15.
console.log(+null + 10)
// Q16.
console.log(+"21" + (10, 20))