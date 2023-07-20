/*
 */
const prompt=require("prompt-sync")({sigint:true}); 
//q1
//1. Create an array of numbers and take input from the user to add numbers to this array.
// let arr=[1,2,3]
// for(let i=0;i<3;i++){
// a = prompt("enter no  : ")
// a=Number.parseInt(a)
// arr.push(a)
// }
// for(let i of arr){
//     console.log(i)
// }

//q2
//2. Keep adding numbers to the array in question-1 until 0 is added the array.
// let arr=[1,2,3]
// let a =1
// while(a!=0){
// a = prompt("enter no  : ")
// a=Number.parseInt(a)
// arr.push(a)
// }
// for(let i of arr){
//     console.log(i)
// }


//q3
// 3. filter for numbers divisible by 10 from a given array.

// let arr=[10,20,23,11,54,62,60,42,88,80,4,19,40]
//  console.log(arr.filter(div_check))

// function div_check(num) {
//     return num%10==0
// }


//q4
// 4. Create an array of square of given numbers.

// let arr=[2,3,4,5,6,7,8,9,10]
// let b= arr.map((num)=>{        //arrow function
//    return num*num
// })
// console.log(b)


//q5
// 5. Use reduce to calculate factorial of a given number from an array of first n natural numbers (n being the number whose factorial needs to be calculated).

// let arr=[1,2,3,4,5]
// let c=arr.reduce((x,y)=>{
//     return x*y
// })
// console.log(c)