/*!
* Start Bootstrap - Clean Blog v6.0.7 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})


var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}

function getIds(filter) {
  const checkboxes = document.querySelectorAll(`.${filter} input:checked`);
  const ids = [...checkboxes].map((item) => item.id);

  return ids;
}

function submit() {
  const prep = getIds("prep-time");
  const ingredients = getIds("ingredients");
  const meals = getIds("meals");
  const food = getIds("food");

  const params = new URLSearchParams();
  params.set("prep", prep);
  params.set("ingredients", ingredients);
  params.set("meals", meals);
  params.set("food", food);

  fetch(`/home?${params.toString()}`);

  console.log({ prep, ingredients, meals, food, params: params.toString() });
}


document.getElementById("filter-apply").addEventListener("click", submit);