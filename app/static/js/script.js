var userInput = document.getElementById("u_input");
var waitingLogo = document.getElementByID("waiting");

class Interface{

  function loading(){
    //Active the loading frame
    waitingLogo.innerHTML= '<img id="loading" src="/static/img/loading.png" width="20"></img>';
       }

  function stop_loading(){
    //Stop the loading frame
    waitingLogo.innerHTML='';
  }

  function send_user_message(input){
    this.messageLine = '<div class="UserLine">'+input+'</div>';
    document.getElementById('chatBox').appendChild(this.messageLine);
  }

  function send_pybot_message(json_output){
    this.messageLine = ('<div class="BotLine">'
      +json_output.intro
      +'</div><div class="BotLine">'
      +json_output.address
      +'</div><div class="BotLine">D\'ailleur je connais tout sur cet endroit:'
      +json_output.extract+'<a href="'
      +json_output.link'">En savoir plus.</a></div>');
    document.getElementById('chatBox').appendChild(this.messageLine)
  }
}

document.addEventListener("keypress", function(event){
  // If user presses "Enter" key :
  var app = new Interface();
  if (event.keyCode == 13 ){
    app.send_user_message(userInput.value)
    app.loading();
    request = new XMLHttpRequest();
    request.open('GET', '/request?u_input=' + userInput.value );
  	request.send();
    // Once the request is sent, we reset the User Input field
    userInput.value = '';
    request.onreadystatechange = function() {
    if (this.readyState == XMLHttpRequest.DONE){
      app.stop_loading();
    }
    if (this.status == 200){
      var response = JSON.parse(this.responseText);
    }
    };
    app.send_pybot_message(response);
  } // Endif
});
