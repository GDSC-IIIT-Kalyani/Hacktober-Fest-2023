function faq() {
  var arrows = document.querySelectorAll('.arrow');
  var answers=document.querySelectorAll('.answer')
      for (let answer of answers){
      answer.style.display = 'none';
      }
  for (let arrow of arrows) {
    arrow.addEventListener('click', function () {
      
      var faqContainer = arrow.closest('.faq');
      
      var answer = faqContainer.querySelector('.answer');
      
      if (answer.style.display === 'none' || answer.style.display === '') {
        answer.style.display = 'block';
      } else {
        answer.style.display = 'none';
      }
      arrow.classList.toggle('rotate180');
    });
  }
}
document.addEventListener('DOMContentLoaded', faq);
function ontogggleMenu(e) {
    console.log(e)
}