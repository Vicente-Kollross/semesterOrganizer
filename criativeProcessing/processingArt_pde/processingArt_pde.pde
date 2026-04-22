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
