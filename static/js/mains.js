$("#comment-form").submit(function(e) {

  var message = $('.contact__msg');
  
    
    e.preventDefault()
    $.ajax({
      url: "/contact_form",
      method:"post",
      data: {
        name: $("#name").val(),
        email: $("#email").val(),
        subject: $("#subject").val(),
        message: $("#contact__msg").val(),
        phone: $("#phone").val(),
        csrfmiddlewaretoken: "{{ csrf_token }}",
      },
      success: function (response) {

        console.log(response)
        message.fadeIn().removeClass('alert-danger').addClass('alert-success');
        message.text(response);
        setTimeout(function () {
            message.fadeOut();
        }, 2000);
        
        $(".message").val("")
        
      },
      error: function (response) {
        console.log(response)
      }
    });
  });