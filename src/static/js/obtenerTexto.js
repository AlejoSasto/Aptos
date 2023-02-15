function ShowSelected() { /* Para obtener el valor */
  var cod = document.getElementById("pago").value;
  var txt = document.getElementById("tex").value;  
  /* Para obtener el texto */
  var combo = document.getElementById("pago");
  var selected = combo.options[combo.selectedIndex].value;  
  if (selected == "1") {
    document.getElementById('tex').innerText = 'Pago';
  } else {
    document.getElementById('tex').innerText = 'No Pago';
  }
}