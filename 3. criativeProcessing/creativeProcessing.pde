void setup() {
  size(400, 400);
  background(30);

color vermelho = color(200, 30, 30);
color azul = color(30, 80, 200);
color preto = color(0,0,0);
color bege = color(230, 190, 150);
color branco = color(255,255,255);
color rosa = color(#FFB5C0);

  // orelhas
  fill(preto);
  ellipse(155, 130, 110, 110);
  ellipse(245, 130, 110, 110);
  
  // cabeça
  ellipse(200, 200, 180, 170);
  
  fill(rosa);
  ellipse(155, 130, 70, 70);
  ellipse(245, 130, 70, 70);

  // rosto
  fill(bege);
  ellipse(200, 210, 130, 120);

  // olhos
  fill(branco);
  noStroke();
  ellipse(175, 190, 25, 25);
  ellipse(225, 190, 25, 25);
  
  fill(preto);
  ellipse(177, 190, 12, 12);
  ellipse(227, 190, 12, 12);
  
  // nariz
  fill(preto);
  ellipse(200, 215, 22, 15);

  // sorriso
  noFill();
  stroke(0);
  strokeWeight(3);
  arc(200, 225, 60, 35, 0, PI);

  // pescoço
  noStroke();
  fill(preto);
  rect(185, 280, 30, 25);

  // corpo vermelho
  fill(vermelho);
  ellipse(200, 340, 130, 110);

  // calção azul
  fill(azul);
  ellipse(200, 370, 130, 60);

  // pernas
  fill(bege);
  rect(170, 385, 25, 45);
  rect(205, 385, 25, 45);

  // sapatos
  fill(preto);
  ellipse(183, 435, 50, 22);
  ellipse(218, 435, 50, 22);

  // braços
  fill(vermelho);
  ellipse(120, 330, 45, 25);
  ellipse(280, 330, 45, 25);

  // mãos
  fill(bege);
  ellipse(95, 335, 35, 30);
  ellipse(305, 335, 35, 30);
}

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