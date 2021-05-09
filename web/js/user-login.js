function code() {
    var x = document.getElementById("username").value;
    var y = document.getElementById("upassword").value;
    eel.user(x, y)(function(ret){
      var para = document.getElementById('res');
      para.innerHTML = ret;
    })
  }

