/**
 * Exemple de code pour un servomoteur, il fait faire des va-et-vient à la tête du servomoteur.
 */

 /* Inclut la lib Servo pour manipuler le servomoteur */
#include <Servo.h>

/* Créer un objet Servo pour contrôler le servomoteur */
Servo monServomoteur;

/** Numéro de broche pour le bouton */
const byte PIN_BUTTON = A0;

void setup() {
  
    Serial.begin(9600);
  // Attache le servomoteur à la broche D9
  monServomoteur.attach(9);

  /* Met la broche du bouton en entrée */
  pinMode(PIN_BUTTON, INPUT);
}

void loop() {
  
  // Fait bouger le bras de 180° à 10°
//  for (int position = 180; position >= 0; position--) {
//    monServomoteur.write(position);
//    delay(15);
//  }
handleSerial();
//monServomoteur.write(5);

/* Lit l'état du bouton poussoir */
  if (digitalRead(PIN_BUTTON) == LOW) {
Serial.println("zoro arrive");
monServomoteur.write(90);
  delay(2000);
  }
 
   monServomoteur.write(90);
}

void handleSerial() {
 while (Serial.available() > 0) {
   char incomingCharacter = Serial.read();
   switch (incomingCharacter) {
     case '+':
     monServomoteur.write(97);
     delay(6000);
      break;
 
     case '-':
      monServomoteur.write(78);
      delay(4000);
      break;
    }
 }
}
