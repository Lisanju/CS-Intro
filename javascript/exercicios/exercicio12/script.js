$(document).ready(function(){
  $(".menu").on("click", function () {
    if ($(".l-site").hasClass("is-open")) {
      $(".menu").removeClass("is-active");
      $(".l-site").removeClass("is-open");
    } else {
      $(".menu").addClass("is-active");
      $(".l-site").addClass("is-open");
    }
  });
});
