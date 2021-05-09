function code() {
    var x = document.getElementById("username").value;
    var y = document.getElementById("otp").value;
    var z = document.getElementById("upassword").value;
    eel.fpass(x, y, z)(function(ret){
      var para = document.getElementById('res');
      para.innerHTML = ret;
    })
  }

