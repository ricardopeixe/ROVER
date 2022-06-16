pagina_controlo='''
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<title>Rover</title>
<style>
#principal{
position:center;
width:1000px;
height:550px;
background-color:white;
border:20px solid;
border-radius:25px;
border-color:#000000;
margin:auto;
}

#principal_titulo{
position:center;
margin-top:10px;
margin-left:40px;
width:900px;
height:100px;
background-color:white;
border:10px dashed ;
border-radius:10px;
border-color:#000000;
}

#principal_botoes{
position:center;
margin-top:10px;
margin-left:40px;
width:450px;
height:380px;
background-color:white;
border:10px dashed ;
border-radius:10px;
border-color:#000000;
}

#principal_texto{
position:center;
margin-top:-400px;
margin-left:520px;
width:420px;
height:380px;
background-color:white;
border:10px dashed ;
border-radius:10px;
border-color:#000000;
}

#texto{
width:300px;
margin-top:60px;
margin-left: 60px;
font: normal 100% 'Eras Demi ITC', sans-serif;
text-align: justify;
}

#titulo{
position:absolute;
left:620px;
width:350px;
top:65px;
border:0px solid;
border-radius:43px;
font: normal 100% 'Eras Demi ITC', sans-serif;
} 

#servo{
position:absolute;
left:280px;
width:350px;
top:380px;	
font: normal 100% 'Eras Demi ITC', sans-serif;
}

#camara{
position:absolute;
left:280px;
width:350px;
top:450px;		
font: normal 100% 'Eras Demi ITC', sans-serif;
}

#botoes1{
position:absolute;
left:380px;
top:180px;
border:0px solid;
font: normal 100% 'Eras Demi ITC', sans-serif;
}

#botoes2{
position:absolute;
left:380px;
top:250px;
border:0px solid;
font: normal 100% 'Eras Demi ITC', sans-serif;
}

#botoes3{
position:absolute;
left:387px;
top:320px;
border:0px solid;
font: normal 100% 'Eras Demi ITC', sans-serif;
}

#ligar_luz{
position:absolute;
left:250px;
top:220px;
border:0px solid;
font: normal 100% 'Eras Demi ITC', sans-serif;
}

#desligar_luz{
position:absolute;
left:538px;
top:220px;
border:0px solid;
font: normal 100% 'Eras Demi ITC', sans-serif;
}

.slider {	  
	  appearance: none;
	  width: 100%; /* Full-width */
	  height: 10px; /* Specified height */
	  background: #d3d3d3; /* Grey background */
	  
	}
	
.slider_cam {	  
	  appearance: none;
	  width: 100%; /* Full-width */
	  height: 10px; /* Specified height */
	  background: #d3d3d3; /* Grey background */
	  
	}

.button {
  border: none;
  color: white;
  padding: 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  padding: 14px 40px;
  margin: 4px 2px;
}

.button_luzes {
  border: none;
  color: white;
  padding: 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 10px;
  padding: 14px 40px;
  margin: 4px 2px;
}

.button1 {
  border-radius: 100%;
  background-color: #000000;
}

.button2 {
  border-radius: 100%;
  background-color: #000000;
}

.button3 {
  border-radius: 50%;
  background-color: #8B0000;
}

.button4 {
  border-radius: 80%;
  background-color: #0B610B;
}

.button5 {
  border-radius: 80%;
  background-color: #424242;
}
</style>
</head>
<body>

<body bgcolor="#E8E8E8">
<div id="principal">
    <div id="principal_titulo">
    <div id="titulo">
        <h1>Consola</h1>
    </div>
    </div>
    <div id="principal_botoes">
    <div id="botoes1">
        <p><a href="/forward"><button class="button button1"> Frente (&#8593) </button></a></p>
    </div>
    <div id="botoes2">
        <p><a href="/stop"><button class="button button3"> &#171 STOP &#187   </button></a></p> 
    </div>
    <div id="botoes3">
        <p><a href="/backward"><button class="button button2"> Tras (&#8595) </button></a></p>
    </div>
    <div id="ligar_luz">
		<p><a href="/luz_on"><button class="button_luzes button4"> Luzes ON </button></a></p>
	</div>
	<div id="desligar_luz">
		<p><a href="/luz_off"><button class="button_luzes button5"> Luzes OFF </button></a></p>
	</div>
    
    <div id="servo">
        <h4>Controlo das rodas:  <span id="servoPos"></span></h4>
        <p> <input type="range" min="0" max="180" class="slider" id="servoSlider" onchange="servo(this.value)"/></p>
    </div>
    <div id="camara">
        <h4>Posicao da camara:  <span id="servoPos_cam"></span>  </h4>
        <input type="range" min="0" max="180" class="slider_cam" id="servoSlider_cam" onchange="servo_cam(this.value)"/>
    </div>
    </div>
    <div id="principal_texto">
        <div id="texto">
            <p>O projeto surge no ambito da unidade curricular de Programacao de Sistemas Inteligentes sob orientacao do professor Antonio Anjos, onde se pretende desenvolver um rover.<p>
            <p>Rover e um tipo de robo dentro da domotica, com uma estrutura terrestre todo-o-terreno, com o intuito de realizar exploracoes de areas via remota. </p>
            <p>Marlene Mateus e Ricardo Peixe</p>

        </div>
    </div>
</div>
<script>
var slider_cam = document.getElementById("servoSlider_cam");
var servoP_cam = document.getElementById("servoPos_cam");
servoP_cam.innerHTML = slider_cam.value;
slider_cam.oninput = function() {
  slider_cam.value = this.value;
  servoP_cam.innerHTML = this.value;
}

var slider = document.getElementById("servoSlider");
var servoP = document.getElementById("servoPos");
servoP.innerHTML = slider.value;
slider.oninput = function() {
  slider.value = this.value;
  servoP.innerHTML = this.value;
}
$.ajaxSetup({timeout:10000});
function servo(pos) {
  $.get("/?value=" + pos + "&");
  {Connection: close};
}

$.ajaxSetup({timeout:10000});
function servo_cam(pos) {
  $.get("/?values=_" + pos + "&");
  {Connection: close};
}

</script> 

</script> 
</body>
</html>'''
