$(document).ready(function(e) {
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
  $(".addMusicForm").submit(function(e){

    e.preventDefault();
    $.ajax({
      type:"POST",
      url:"/addmusicajax/",
      data:$(this).serialize(),
      dataType: "json",
      success: function(data) {
        $.each(data, function(i, row){
          $("#displayMsg").append(row);
        });

        $(".addMusicForm").trigger("reset");
      },
      error: function() {
          alert('error handing here');
      }
    });
  });
});
