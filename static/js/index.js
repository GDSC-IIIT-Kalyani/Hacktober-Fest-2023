function faq() {
  var quess = document.querySelectorAll('.ques');
  var questions = document.querySelectorAll('.abc');
  var answers=document.querySelectorAll('.answer')
      for (let answer of answers){
      answer.style.display = 'none';
      }
  for (let ques of questions) {
    ques.addEventListener('click', function () {
      
      var faqContainer = ques.closest('.faq');
      
      var answer = faqContainer.querySelector('.answer');
      
      if (answer.style.display === 'none' || answer.style.display === '') {
        answer.style.display = 'block';
      } else {
        answer.style.display = 'none';
      }
      ques.children[1].children[0].classList.toggle('rotate180');
    });
  }
}
document.addEventListener('DOMContentLoaded', faq);
const navLinks = document.querySelector('.nav-links')
function onToggleMenu(e){
    e.name = e.name === 'menu' ? 'close' : 'menu'
    navLinks.classList.toggle('top-[9%]')
}