$(function() {
    // Initialize form validation on the registration form.
    // It has the name attribute "registration"
    $("form[name='TablaAlumnos']").validate({
      //Reglas de validacion
      rules: {

        correo: {
            required: true,
            correo: true
        },

        contrasenia: {
            required: true
        },
       
      },
      // Mensajes especificos de error de validacion
      messages: {

        correo: {
          required:"Por favor, introduzca una dirección de correo",
        },

        contrasenia: {
            required: "Por favor, introduzca la contraseña",
        },
      },
      submitHandler: function(form) {
        form.submit();
      }
    });
  });