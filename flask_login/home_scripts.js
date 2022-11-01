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

  fetch(`/recipes?${params.toString()}`);

  console.log({ prep, ingredients, meals, food, params: params.toString() });
}


document.getElementById("filter-apply").addEventListener("click", submit);