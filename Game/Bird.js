function Bird(){
  this.y = height/2;
    this.x = 65;
  
    this.gravity = 0.2;
    this.velocity = 7;
    this.lift = -7;
  
    this.show = function(){
      fill(255);
      ellipse(this.x,this.y,32,32);
    }

    this.up = function(){
      this.velocity += this.lift;
    }


    this.update = function(){
      // this.velocity += this.gravity;
      // this.y += this.velocity;   
      // if(this.y > height){
      //   this.y = height;   
      // }
      // if(this.y < 0){
      //   this.y = 0; 
      // }w
      this.velocity += this.gravity;
      this.y += this.velocity;
      if(this.y > height-16){
        this.y = height-16;
        this.velocity -= this.velocity;
      } 
      if(this.y < 16){
        this.y = 16;
        this.velocity -= this.velocity;
      } 
    }
}
