function code() {
    var w = document.getElementById("name").value;
    var x = document.getElementById("email").value;
    var y = document.getElementById("username").value;
    var z = document.getElementById("rpassword").value;
    eel.userRegistration(w,x, y,z)(function(ret){
      var para = document.getElementById('res');
      para.innerHTML = ret;
    })
  }

