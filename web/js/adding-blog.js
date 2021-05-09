function code() {
    var x = document.getElementById("title").value;
    var y = document.getElementById("content").value;
    eel.addblog(x, y)(function(ret){
      var para = document.getElementById('res');
      para.innerHTML = ret;
    })
  }
async function runer() {
    let n = await eel.addblogdetails()();
    console.log(n);
    addcall(n);
}
runer();

