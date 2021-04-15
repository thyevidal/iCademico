
let swiper = new Swiper('.swiper-container', {
  slidesPerView: 3,
  spaceBetween: 40,
  loop: true,
  grabCursor: true,
  pagination: {
    el: '.swiper-pagination', 
    clickable: true,
    type: 'progressbar' 
  },
  navigation: {
    nextEl: '.button-next',
    prevEl: '.button-prev',
  }
});

