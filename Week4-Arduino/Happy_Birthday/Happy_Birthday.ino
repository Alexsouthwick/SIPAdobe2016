int LEDPIN1 = 4;
int LEDPIN2 = 5;
int BUTTON = 7;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LEDPIN1, OUTPUT);
  pinMode(LEDPIN2, OUTPUT);
  pinMode(BUTTON, INPUT_PULLUP);
  Serial.print(HIGH);
  Serial.print(LOW);
 
}

void loop() {
  // put your main code here, to run repeatedly:
  boolean on = false;
//  Serial.print(on);
  if (digitalRead(BUTTON) == LOW){
    on = true;
    while (digitalRead(BUTTON) == HIGH);
      Serial.print(on);}
      if (digitalRead(BUTTON) == LOW){
        on = false;
        while (digitalRead(BUTTON) == HIGH);
    Serial.print(on);}
    //while (digitalRead(BUTTON) ==HIGH) {
      //if (digitalRead(BUTTON) == HIGH)
        //on =false;
        //digitalWrite(LEDPIN1, LOW);
        //digitalWrite(LEDPIN2, LOW);
        //Serial.print(on);
      
   while (on == true){
    if (digitalRead(BUTTON) == HIGH){
     digitalWrite(LEDPIN1, HIGH);
     delay(600);
     digitalWrite(LEDPIN1, LOW);
     delay(200);
      
      digitalWrite(LEDPIN2, HIGH);
      delay(200);
      digitalWrite(LEDPIN2, LOW);
      delay(200);
    
      digitalWrite(LEDPIN1, HIGH);
      delay(500);
      digitalWrite(LEDPIN1, LOW);
      delay(250);
    
      digitalWrite(LEDPIN2, HIGH);
      delay(500);
      digitalWrite(LEDPIN2, LOW);
      delay(250);
    
      digitalWrite(LEDPIN1, HIGH);
      delay(500);
      digitalWrite(LEDPIN1, LOW);
      delay(250);
    
      digitalWrite(LEDPIN2, HIGH);
      delay(1000);
      digitalWrite(LEDPIN2, LOW);
      delay(1000);
    }
    }
//   while (on== false){
//    if (digitalRead(BUTTON) == HIGH){
//      digitalWrite(LEDPIN1, LOW);
//      digitalWrite(LEDPIN2, LOW);
//      Serial.print(on);
    }
      
    
  
  
  //else if (digitalRead(BUTTON) == LOW){
    //digitalWrite(LEDPIN1, LOW);
    //digitalWrite(LEDPIN2, LOW);
  //}
}


