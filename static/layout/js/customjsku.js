var $backToTop = $(".backTop");
    $backToTop.hide();
    $(window).on('scroll', function() {
      if ($(this).scrollTop() > 100) {
        $backToTop.fadeIn();
      } else {
        $backToTop.fadeOut();
      }
    });

    $backToTop.on('click', function(e) {
      $("html, body").animate({scrollTop: 0}, 500);
    });
    
// dark mode

function darkLight(x = null) {
  /*DARK CLASS*/
  
  if (localStorage.toggled != 'dark' && Boolean(x) == true) {
    $('#navBar').toggleClass('indigo darken-2 z-depth-2', false);
    $('#navBar').toggleClass('dark', true);
    $('#foot').toggleClass('indigo', false);
    $('#foot').toggleClass('dark', true);
    $('#main').toggleClass('dark-2', true);
    $('#nav-mobile, #konten').toggleClass('konten', true);
    $('#isi, #teksJudul').toggleClass('white-text', true);
    localStorage.toggled = "dark";
     M.toast({html: 'Dark Mode is ON!', classes: 'rounded'});
     
  } else {
     $('#navBar').toggleClass('dark', false);
     $('#navBar').toggleClass('indigo darken-2 z-depth-2', true);
     $('#foot').toggleClass('indigo', true);
    $('#foot').toggleClass('dark', false);
    $('#main').toggleClass('dark-2', false);
    $('#nav-mobile, #konten').toggleClass('konten', false);
    $('#isi, #teksJudul').toggleClass('white-text', false);
    $('#isi, #teksJudul').toggleClass('black-text', true);

    localStorage.toggled = "";
     M.toast({html: 'Dark Mode is OFF!', classes: 'rounded'});
  }
}

/*Add 'checked' property to input if background == dark*/
if (localStorage.toggled == 'dark') {
  $( '#checkBox' ).prop( "checked", true )
  $( '#checkBox2' ).prop( "checked", true )
    console.log("aktif");
} else {
  $( '#checkBox' ).prop( "checked", false )
  $( '#checkBox2' ).prop( "checked", false )
    console.log(" tidak aktif");
}

// end dark mode

<!--// <script>-->
<!--//       self.addEventListener('fetch', (e) => {-->
<!--//   e.respondWith(-->
<!--//     caches.match(e.request).then((r) => {-->
<!--//           console.log('[Service Worker] Fetching resource: '+e.request.url);-->
<!--//       return r || fetch(e.request).then((response) => {-->
<!--//                 return caches.open(cacheName).then((cache) => {-->
<!--//           console.log('[Service Worker] Caching new resource: '+e.request.url);-->
<!--//           cache.put(e.request, response.clone());-->
<!--//           return response;-->
<!--//         });-->
<!--//       });-->
<!--//     })-->
<!--//   );-->
<!--// });-->
<!--//   </script>-->

// ads
function myFunction() {
  var x = document.getElementById("SC_TBlock_752939");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function myFunction2() {
  var x = document.getElementById("SC_TBlock_752956");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
// end ads