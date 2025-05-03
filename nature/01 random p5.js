// Simple p5.js animation with random moving shapes

let particles = [];
const numParticles = 50;

function setup() {
  createCanvas(600, 400);
  
  // Initialize particles with random properties
  for (let i = 0; i < numParticles; i++) {
    particles.push({
      x: random(width),
      y: random(height),
      size: random(5, 20),
      speedX: random(-2, 2),
      speedY: random(-2, 2),
      color: color(random(255), random(255), random(255), 180)
    });
  }
}

function draw() {
  background(30, 40, 50);
  
  // Update and display each particle
  for (let i = 0; i < particles.length; i++) {
    let p = particles[i];
    
    // Move the particle
    p.x += p.speedX;
    p.y += p.speedY;
    
    // Bounce off edges
    if (p.x < 0 || p.x > width) p.speedX *= -1;
    if (p.y < 0 || p.y > height) p.speedY *= -1;
    
    // Display the particle
    noStroke();
    fill(p.color);
    ellipse(p.x, p.y, p.size);
  }
  
  // Display frame rate for reference
  fill(255);
  text("Frame rate: " + floor(frameRate()), 10, 20);
}
