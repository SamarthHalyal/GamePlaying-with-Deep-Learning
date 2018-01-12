function Pipes(){
  this.y1 = random(100,height*0.7);
  this.x = width;
  this.y2 = height - this.y1 - 100;
  this.w = 20;
  this.speed = 2;
  
  this.show = function(){
    fill(255);
    rect(this.x,0,this.w,this.y1);
    rect(this.x,height-this.y2,this.w,this.y2);
  }
  
  this.update = function(){
    this.x -= this.speed;
  }
}