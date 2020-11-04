class Interface{
  constructor(){
}
  loading(){
    //Active the loading frame

    var waitingLogo = '<img id="loading" src="/static/img/loading.png" width="20"></img>';
    var waitingLogo_html = document.createRange().createContextualFragment(waitingLogo);
    document.getElementById("waiting").appendChild(waitingLogo_html);
       }

  stop_loading(){
    //Stop the loading frame
    var stop = document.getElementById("waiting")
    stop.removeChild(stop.childNodes[0])
  }

  send_user_message(input){
    this.userLine = '<div class="UserLine">'+input+'</div>';
    this.userLine_html = document.createRange().createContextualFragment(this.userLine);
    document.getElementById('chatBox').appendChild(this.userLine_html);
  }

  send_pybot_message(json_output){
    console.log("envoi")
    this.pybotLine_html = document.createRange().createContextualFragment(
      '<div class="BotLine">'
        +json_output.intro
        +'</div><div class="BotLine">'
        +json_output.address
        +'</div><div class="BotLine"><iframe id="map" src="https://www.google.com/maps/embed/v1/place?key='
        +json_output.key
        +'&q=\''
        +json_output.address
        +'\'" width="100%""></iframe></div><div class="BotLine">D\'ailleurs je connais tout sur cet endroit: '
        +json_output.extract+'<br><a href="'
        +json_output.link+'" target="_blank">En savoir plus.</a></div>'
    );
    document.getElementById('chatBox').appendChild(this.pybotLine_html);

    }
}
//Creating an interface
var app = new Interface();
document.addEventListener("keypress", function(event){
  // If user presses "Enter" key :

  if (event.key == "Enter" ){
    console.log("entrée")
    var userInput = document.getElementById("u_input");
    app.send_user_message(userInput.value);
    app.loading();
    var request = new XMLHttpRequest();
    request.open('GET', '/request?u_input=' + userInput.value);
  	request.send(null);
    // Once the request is sent, we reset the User Input field
    userInput.value = '';
    request.onreadystatechange = function() {
      console.log(this.readyState)
      if (this.readyState == XMLHttpRequest.DONE){
        app.stop_loading();
      
        if (this.status == 200){
          console.log("positif")
          var response = JSON.parse(this.responseText);
          app.send_pybot_message(response);
        }
        if (this.status != 200){
          console.log("negatif")
          var pybotLine_html = document.createRange().createContextualFragment('<div class="BotLine">Désolé, je n\'ai pas compris.</div>');
          document.getElementById('chatBox').appendChild(pybotLine_html);
        }}
    };

  } // Endif
});
