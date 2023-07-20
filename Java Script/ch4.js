//q1
// 1.    What will the following print in JavaScript?
//        console.log(“har\””.length)
// console.log("har\"".length ) //4

//q2
//2.    Explore the includes, startsWith and endsWith functions of a string.

// let a = "rupesh"
// console.log(a.startsWith("re"))
// console.log(a.endsWith("sh"))

//q3
//3.    Write a program to convert a given string to lowercase.

// let b = "RUPESH"
// console.log(b.toLowerCase())
//q4
// 4.    Extract the amount out of this string
//        “Please give Rs 1000”
// let pr = "please give Rs 1000" 
// let am=Number.parseInt(pr.slice(15))//length of sting till 1000
// console.log(am)
// console.log(typeof(am))

//q5
//5.    Try to change the 4th character of a given string. Were you able to do it?

// let name = "rupesh"
// name[4]="j"

// console.log(name) //name will not change because string is immutable