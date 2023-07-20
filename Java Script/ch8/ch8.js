/*
*/

//q1
// 1. Write a program to show different alerts when different buttons are clicked.
// let a = document.getElementById("btn1")
// let b = document.getElementById("btn2")
// let c = document.getElementById("btn3")
// let d = document.getElementById("btn4")

// a.onclick=()=>{
//     document.body.style.background="red"
//     alert('background is red')
// }
// b.onclick=()=>{
//     document.body.style.background="green"
//     alert('background is green')
// }
// c.onclick=()=>{
//     document.body.style.background="blue"
//     alert('background is blue')
// }
// d.onclick=()=>{
//     document.body.style.background="yellow"
//     alert('background is yellow')
// }

//q2
//2. Create a website which is capable of storing bookmarks of your favorite websites using href.
 //it is html based question where we have to give anchor tag and save or explore websites using href
//q3
//3. Repeat Q.2 using event listeners.
// let a = document.getElementById("google")
// a.addEventListener('click',function () {
//     window.location="https://www.google.com"
// })

// document.getElementById("fb").addEventListener('click',function () {
//     window.location="https://fb.com"
// })
// document.getElementById("twitter").addEventListener('click',function () {
//     window.location="https://twitter.com"
// })
// document.getElementById("github").addEventListener('click',function () {
//     window.location="https://github.com"
// })

//q4
//4. Write a JS program to keep fetching contents of a website (every 5 seconds).
// async function fetching(){
    
//     var p = await fetch('https://reqres.in/api/users?page=1');
//     var k= await p.json();
//     return k   
// }
// const refresh=fetching();
// setInterval(()=>{
// refresh.then((data)=>{
//         console.log(data.data);
//     })},5000)
//q5
//5. Create a glowing bulb effect using classlist toggle method in JS.

// let a = document.getElementById("bulb")
// setInterval(()=>{a.classList.toggle("bulb")},500)


