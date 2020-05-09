#include <Servo.h>

//int Read_Voltage  = A0;
//int Read_Current  = A1;
int analogInput = 0;
float vout = 0.0;
float vin = 0.0;
float R1 = 100000.0; // resistance of R1 (100K) -see text!
float R2 = 10000.0;  // resistance of R2 (10K) - see text!

Servo monServomoteur;
int speed = 90;

int count = 0;
int maxCount = 100;
float sumVolt = 0;
float sumCurr = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(analogInput, INPUT);
  monServomoteur.attach(9);
  //    lcd.begin(16, 2);
  //    lcd.print("DC VOLTMETER");
}
void loop()
{
  // Mesure la tension sur la broche A0
  float tension = analogRead(A0);
  float courant = analogRead(A1);

  vout = (tension * 5.0) / 1024.0; // see text
  vin = vout / (R2 / (R1 + R2));
  // Mesure courant sur la broche A1
  courant = courant * (5.0 / 1023.0) * 0.08;
  //Vs = Vin * (R2 / (R1 + R2))
  // Transforme la mesure (nombre entier) en tension via un produit en croix
  // vin = value * (5.0 / 1023.0);
  if (vin < 0.09)
  {
    vin = 0.0; //statement to quash undesired reading !
  }
  else
  {
    count++;
    sumVolt += vin;
    sumCurr += courant;
    if (count == maxCount) {
      // compute average
      float avgTens = sumVolt / count;
      float avgCurr = sumCurr / count;
      float puissance = avgTens*avgCurr;

      // Envoi la mesure au PC pour affichage
      Serial.print(avgCurr);
      Serial.print("A ");
      Serial.print(avgTens);
      Serial.print("V => ");
      Serial.print(puissance);
      Serial.println("W");
      
      // reset values
      count = 0;
      sumVolt = 0;
      sumCurr = 0;
    }
  }


  handleSerial();
  monServomoteur.write(speed);

  delay(10);
}


void handleSerial()
{
  while (Serial.available() > 0)
  {
    char incomingCharacter = Serial.read();
    switch (incomingCharacter)
    {
      case '=':
        speed += 5;
        break;

      case '-':
        speed -= 5;
        break;
      case ' ':
        speed = 90;
        break;
    }
    Serial.println(speed);
  }
}