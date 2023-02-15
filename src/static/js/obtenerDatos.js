function obtenerDatos(id){
  document.getElementById('formulario').action = '/editar_usuario/'+id
  document.getElementById('boton_form').innerHTML = 'Actualizar'
  nombreactualp = document.getElementById('tabla_apellido'+id).innerHTML
  valoractualp = document.getElementById('tabla_correo'+id).innerHTML
  cantactualp = document.getElementById('tabla_usuario'+id).innerHTML
  apartamentoact = document.getElementById('tabla_apartamento'+id).innerHTML
  torreact = document.getElementById('tabla_torre'+id).innerHTML
  document.getElementById('apellido').value = nombreactualp
  document.getElementById('correo').value = valoractualp
  document.getElementById('usuario').value = cantactualp
  document.getElementById('apartamento').value = apartamentoact
  document.getElementById('torre').value = torreact
}

