var request = new XMLHttpRequest();

function check(form)
{



request.open('GET', 'http://127.0.0.1:5000/login', true,form.userid.value );
request.onload = function () {

  // Begin accessing JSON data here
  var data = JSON.parse(this.response);

  if (request.status >= 200 && request.status < 400) {
   
      console.log(data);
   
  } else {
    console.log('error');
  }
}

request.send();
}