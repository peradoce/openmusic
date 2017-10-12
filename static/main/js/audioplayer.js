function audioPlayer(){
          var currentSong = 0;
          var get_song = $("current-song a").text();
          $("#audioPlayer")[0].src = $("#playlist li a")[0];
          $("#audioPlayer")[0].play();
          $("#playlist li a").click(function(e){
             e.preventDefault();
             $("#audioPlayer")[0].src = this;
             $("#audioPlayer")[0].play();
             $("#playlist li").removeClass("current-song blue white-text");
              currentSong = $(this).parent().index();
              $(this).parent().addClass("current-song blue white-text");
          });

          $("#audioPlayer")[0].addEventListener("ended", function(){
             currentSong++;
              if(currentSong == $("#playlist li a").length)
                  currentSong = 0;
              $("#playlist li").removeClass("current-song blue");
              $("#playlist li:eq("+currentSong+")").addClass("current-song blue");
              $("#current-playing").text(get_song);
              $("#audioPlayer")[0].src = $("#playlist li a")[currentSong].href;
              $("#audioPlayer")[0].play();
          });
      }
