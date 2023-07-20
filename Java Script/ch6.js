/*
 */


//note :- run it in browser

//q1
// 1.  Write a program using prompt function to take input of age as a value from the user and use alert to tell him if he can drive.
// a = prompt("enter your age")
// a=Number.parseInt(a)
// if(a<18){
//     alert("you can not drive")
// }else{
//     alert("you can drive")
// }
//q2
// 2.  In Q-1 use confirm to ask the user if he wants to see the prompt again.
// let again=true
// do{
// a = prompt("enter your age")
// a=Number.parseInt(a)
// again=confirm("you are confirm that your age is :"+a)
// if(again){
// if(a<18){
//     alert("you can not drive")
// }else{
//     alert("you can drive")
// }
// }
// }while(!again)
//q3
// 3.  In the previous question, use console.error to log the error if the age entered is negative.
//let again=true
// do{
// a = prompt("enter your age")
// a=Number.parseInt(a)
// again=confirm("you are confirm that your age is :"+a)
// if(again){
//     if(a<0){
//         console.error("negetive age in entered")
//         }else{
// if(a<18){
//     alert("you can not drive")
// }else{
//     alert("you can drive")
// }
// }
// }
// }while(!again)
//q4
// 4.  Write a program to change the url to google.com (Redirection) if user enters a number greater than 4.
//     a = prompt("enter a number")
// a=Number.parseInt(a)
// if(a>4){
//     location.replace("http://www.google.com")
// }

//q5
// 5.  Change the background of the page to yellow, red or any other color based on used input through prompt.
// a = prompt("which color you want to change the background")
// document.body.style.backgroundColor=a;