 /*
*/

//q1
//1. Write a program to load a JS File in a browser using Promises. Use .then() to display an alert when the load is complete.

// function loadscript(src){
//        return new Promise((resolve,reject)=>{
//         let script = document.createElement("script")
//         script.src=src
//         script.onload=(()=>{
//             resolve("script load completed")
//         })

//         script.onerror=((error)=>{
//             reject(new Error("script coudn't load successfully"))
//         })
//         document.body.appendChild(script)
//     })
// }
// let p =loadscript("https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js")

// p.then((v)=>{
//     alert(v)
// }).catch((e)=>{
//     alert(e)
// })

//q2
//2. Write the same program from previous question and use async/await syntax.

// async function loadscript(src){
//            return new Promise((resolve,reject)=>{
//             let script = document.createElement("script")
//             script.src=src
//             script.onload=(()=>{
//                 resolve("script load completed")
//             })
    
//             script.onerror=((error)=>{
//                 reject(new Error("script coudn't load successfully"))
//             })
//             document.body.appendChild(script)
//         })
//     }

//     async function ms(){

//         let p = await loadscript("https://cdnnn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js")
//         console.log(p)
//     }

//     ms()

//q3
//3. Create a promise which rejects after 3 seconds. Use an async/await to get its value. Use a try catch to handle its error.

// async function rej(){
//     return new Promise((resolve,reject)=>{
//         setTimeout(()=>{
//             reject(new Error("error mila hai bhai"))
//         },3000)
//     })
// }
// async function mn(){
//     try {
//         console.log("hi")
//         let p = await rej()
//         console.log(p)
//     } catch (error) {
//         console.log(error)
//     }
// }
// mn()

//q4
//4. Write a program using Promise.all() inside an async/await to await 3 promises. Compare its results with the case where we await these promises one by one.

async function rej1(){
        return new Promise((resolve,reject)=>{
            setTimeout(()=>{
                resolve("good mila hai bhai 1")
            },1000)
        })
    }


    async function rej2(){
        return new Promise((resolve,reject)=>{
            setTimeout(()=>{
                resolve("good mila hai bhai 2")
            },2000)
        })
    }
    
async function rej3(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("good mila hai bhai 3")
        },3000)
    })
}

async function mn(){
    console.time("run")
    //it will take 6 sec
    // let p1 = await rej1()
    // let p2 = await rej2()
    // let p3 = await rej3()
    // console.log(p1,p2,p3)

    //it will take only 3 sec and runs parallel
    let p1 =  rej1()
    let p2 =  rej2()
    let p3 =  rej3()
    let pAll=await Promise.all([p1,p2,p3])
    console.log(pAll)
    console.timeEnd("run")
} 
mn()