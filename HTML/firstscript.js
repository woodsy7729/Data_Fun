function init(){
  var h1tags = document.getElementsByTagName("h1");
  h1tags[1].onclick = react;
}

function react(){
  this.innerHTML = "Clicked";
  this.style.colour = "blue";
}
onload=init;
