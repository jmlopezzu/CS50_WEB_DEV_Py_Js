let counter = 0;

function count() {
  counter++;
  document.querySelector('h1').innerHTML = counter;
}

// Get an alert each 10 seconds
  //if(counter % 10 === 0){
    //alert(`Count is now ${counter}`);
  //}
//}

document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('button').onclick = count;

  setInterval(count, 1000);
});
