void setup(){
  size(500,500);
}
color rosa = color (255, 182, 193);
color preto = color (0);
color cinza = color (256/2);
color branco = color(255);
color amarelo = color (240, 255, 36);

void draw(){
  //Fundo e linhas do Rato
  background(branco);
  fill(255,0,0);
  stroke(0);
  strokeWeight(10);
  
  
  
  
  //Rato
  fill(rosa);
  circle(150,150,150);
  circle(350,150,150);
  
  fill(cinza);
  triangle(150, 150, 350, 150, 250, 400);
  
  fill(rosa);
  circle(250,400,55);
  fill(branco);
  circle(190,200,80);
  circle(310,200,80);
  fill(preto);
  circle(190,200,10);
  circle(310,200,10);
  
  line(283, 390, 300, 375);
  line(283, 400, 310, 400);
  line(283, 410, 300, 425);
  
  line(217, 390, 200, 375);
  line(217, 400, 190, 400);
  line(217, 410, 200, 425);
  
  
  
  
  
  //Queijo
  strokeWeight(4);
  fill(amarelo);
  triangle(350, 450, 400, 450, 375, 400);
  
  fill (preto);
  circle (365,440, 8);
  circle (377,420, 8);
  
}