$(document).ready(function () {
    $('div.top').click(function() {
    $('html, body').animate({
      scrollTop: $("div.mid1").offset().top
    }, 1000)
  }), 
    $('div.mid1').click(function (){
      $('html, body').animate({
        scrollTop: $("div.mid2").offset().top
      }, 1000)
    }),
    $('div.mid2').click(function (){
      $('html, body').animate({
        scrollTop: $("div.mid3").offset().top
      }, 1000)
    }),
    $('div.mid3').click(function (){
      $('html, body').animate({
        scrollTop: $("div.bottom2").offset().top
      }, 1000)
    }),
    $('div.bottom2').click(function (){
      $('html, body').animate({
        scrollTop: $("div.bottom3").offset().top
      }, 1000)
    }),
    $('div.bottom3').click(function (){
      $('html, body').animate({
        scrollTop: $("div.bottom4").offset().top
      }, 1000)
    }),
    $('div.bottom4').click(function (){
      $('html, body').animate({
        scrollTop: $("div.bottom4").offset().top
      }, 1000)
    }),
    $('div.final').click(function (){
      $( "#form_id" )[0].submit();  
    })
  });