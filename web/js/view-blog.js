// function code() {
//   var x = document.getElementById("stitle").value;
//   let head = document.getElementById('btn1')
//   let btn = document.createElement('button');
//   let cli = document.createTextNode('Enter Again')
//   btn.setAttribute('onclick', 'fun()');
//   btn.appendChild(cli)
//   head.appendChild(btn)
//   eel.viewtb(x)

// }

function code() {
  var x = document.getElementById("stitle").value;
  eel.viewtb(x)(function(ret) {
    let para = document.getElementById('title1');
    let para1 = document.getElementById('content');
    result1 = Object.keys(ret)
    result2 = Object.values(ret)
    para.innerHTML = result1;
    para1.innerHTML = result2;
    console.log(result);
  })
}



// eel.selectuser(user)(function (ret) {
//   var para = document.getElementById('res');
//   var reselt = Object.entries(ret)
//   para.innerHTML = reselt;
// })
  // testtb();


// async function code() {
//     let n = await eel.viewtb1()(function (ret){
//     var para=document.getElementById('title');
//     result = Object.entries(ret);
//     para.innerHTMl=result;
//     })
//     console.log(result);
//     console.log(n);
//     addcall(n);
// }



