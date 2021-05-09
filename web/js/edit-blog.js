function code() {
  var x = document.getElementById("stitle").value;
  eel.tcame(x)(function(ret) {
    let para = document.getElementById('title1');
    let para1 = document.getElementById('content');
    result1 = Object.keys(ret)
    result2 = Object.values(ret)
    para.innerHTML = result1;
    para1.innerHTML = result2;
    console.log(result);
  })
}
function coder(){
    var x = document.getElementById("title1").value;
    var y = document.getElementById("content").value;
    eel.edit_update(x, y)(function(ret){
      var para = document.getElementById('res');
      para.innerHTML = ret;
    })
}