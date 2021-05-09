function code() {
    var x = document.getElementById("username").value;
    var y = document.getElementById("pass").value;
    eel.admin(x, y)(function(ret){
      var para = document.getElementById('res');
      para.innerHTML = ret;
    })
  }

  