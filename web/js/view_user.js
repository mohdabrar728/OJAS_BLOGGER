async function code() {

  eel.viewuser()(function (ret) {
    var para = document.getElementById('res');
    let select = Object.values(ret)
    para.innerHTML = select;
  });
}

async function fun1() {
  var user = document.getElementById('newinput').value;

  let n = await eel.selectuser(user)();
  addcall(n);

  function dyn(array, array1) {
    var array_key = [];
    for (var c = 0; c < array.length; c++) {
      array_key += c + 1
    }
    var arr_keys = array1;
    var array_value = array;
    console.log(arr_keys)
    console.log(array_value)

    let head = document.getElementById('txt');
    let txt = document.createTextNode('User Blogs')
    head.appendChild(txt)
    document.getElementById('bask2').innerHTML = '';
    var dynobj = document.getElementById('dynamic');
    for (var count = 0; count < array.length; count++) {
      var newRow = dynobj.insertRow();
      var newcell1 = newRow.insertCell(0);
      var newcell2 = newRow.insertCell(1);
      var newcell3 = newRow.insertCell(2);
      var newcell4 = newRow.insertCell(3);

      newcell1.innerHTML = array_key[count]
      newcell2.innerHTML = arr_keys[count]
      newcell3.innerHTML = array_value[count]
      newcell4.innerHTML = '06-05-2021'
    }
  }
  function addcall(n) {
    let array = Object.values(n);
    let array1 = Object.keys(n);
    dyn(Object.values(array), Object.values(array1));
    // for(i=0;i<array.length;i++){
    // addElement(array[i]);
    // dyn(Object.values(array));
  }
};

async function fun2() {
  var user = document.getElementById('input1').value;
  var title = document.getElementById('input2').value;
  // document.getElementById('viewoutput').innerHTML = '';
  // document.getElementById('head').innerHTML = '';
  // var head = document.getElementById('viewoutput');
  // var p = document.createElement('h2');
  // var t = document.createTextNode('User Blogs:')
  // p.appendChild(t)
  // head.appendChild(p)


  let x = await eel.deleteuser(user, title)();
  console.log(x);
  addcall(x);
}