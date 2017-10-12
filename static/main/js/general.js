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

  $(".generatePlaylist").submit(function(e){
    e.preventDefault();
    $.ajax({
      type:"POST",
      url:"/playlist-form-ajax/",
      data:$(this).serialize(),
      dataType: "json",
      success: function(data) {
        $('#displayMsg').empty();
        $('#displayKey').empty();
        if (data.final_key != '')
        {
          $("#displayMsg").append(data.success_msg + '<br>');
        }
        else{
          $.each(data, function(i, row){
            $("#displayMsg").append(row + '<br>');
          });
        }

        $("#displayKey").append('<h5>Your key is: </h5>');
        $("#displayKey").append('<h5>' + data.final_key + '</h5><br>');
        $(".generatePlaylist").trigger("reset");
      },
      error: function() {
          alert('error handing here');
      }
    });
  });

  $( ".music-code" ).click(function() {
    var ytcode = $(".music-code").val();

  });

});
