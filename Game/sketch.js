var bird;
var pipes = [];
function setup() {
  createCanvas(400,600);
  bird = new Bird();
  pipes.push(new Pipes());
}

function draw() {
  background(0);
  bird.show();
  bird.update();
  
  if(frameCount % 100 === 0){
    pipes.push(new Pipes());
  }
  
  for(var i = 0;i < pipes.length;i++){
    pipes[i].show();
    pipes[i].update();
  }
  
}

function keyPressed(){
  if(keyCode === 87){
    bird.up();
  }
}