int piezo_pin = 5;

// One octave of notes between A4 and A5
int note_A4 = 440;
float note_As4 = 466.16; float note_Bb4 = note_As4;
int note_B4 = 494;
int note_C5 = 523;
int note_Cs5 = 554; int note_Db5 = note_Cs5;
int note_D5 = 587;
float note_Ds5 = 622.25; float note_Eb5 = note_Ds5;
int note_E5 = 659;
int note_F5 = 698;
int note_Fs5 = 740; int note_Gb5 = note_Fs5;
int note_G5 = 784;
float note_Gs5 = 830.61; float note_Ab5 = note_Gs5;
float note_Ab4 = 415.30;
int note_G4 = 392;
float note_F4 = 349.23;
float note_Eb4 = 311.13;
float note_D4 = 293.66;
int note_A5 = note_A4 * 2;
int note_As5 = note_As4 * 2; int note_Bb5 = note_As5;
int note_B5 = note_B4 * 2;

int note_rest = -1;

// note lengths defined here
long whole_note = 1600; // change tempo by changing duration of one measure
long half_note = whole_note / 2;
long quarter_note = whole_note / 4;
long eighth_note = whole_note / 8;
long sixteenth_note = whole_note / 16;
long dotted_quarter = quarter_note + eighth_note; 

// WRITE YOUR SONG HERE
// if you want there to be silence between notes,
//   staccato should be true
bool staccato = true;

void setup() {
  pinMode(piezo_pin, OUTPUT);
//    int verse_1[17][2]= {{note_Bb4, dotted_quarter}, {note_Ab4, eighth_note},{note_G4, quarter_note},
//    {note_F4, quarter_note},{note_Eb4, quarter_note}, {note_F4, quarter_note},
//    {note_G4, quarter_note},{note_Eb4, quarter_note}, {note_F4, eighth_note},
//    {note_G4, eighth_note},{note_Ab4, eighth_note},{note_F4, eighth_note},{note_G4, dotted_quarter},
//    {note_F4, eighth_note},{note_Eb4, quarter_note},{note_D4, quarter_note},{note_Eb4, half_note}};
//
//    int verse_2[17][2]= {{ note_F4, dotted_quarter},{note_G4, eighth_note},{note_Ab4, quarter_note},{note_F4, quarter_note},
//    {note_G4, dotted_quarter},{note_Ab4, eighth_note},{note_Bb4, quarter_note},{note_F4, quarter_note},{note_G4, eighth_note}, 
//    {note_A4, eighth_note},{note_Bb4, quarter_note},{note_C5, eighth_note},{note_D5, eighth_note},{note_Eb5, quarter_note},
//    {note_D5, quarter_note},{note_C5, quarter_note},{note_Bb4, half_note}};
// 
//    int verse_3[18][2]= {{note_Bb4, dotted_quarter}, {note_Ab4, eighth_note},{note_G4, quarter_note},
//    {note_F4, quarter_note},{note_Eb4, quarter_note}, {note_F4, quarter_note},
//    {note_G4, quarter_note},{note_Eb4, quarter_note}, {note_C5, eighth_note},{note_C5, eighth_note},{note_C5, eighth_note},
//    {note_C5, eighth_note},{note_Bb4, dotted_quarter},{ note_Ab4, eighth_note},
//    {note_G4, quarter_note},{note_F4, quarter_note},{note_Eb4, half_note}};
  Serial.begin(9600);
}



void loop() {
//  int verse_1[17][2]= {{note_Bb4, dotted_quarter}, {note_Ab4, eighth_note},{note_G4, quarter_note},
//  {note_F4, quarter_note},{note_Eb4, quarter_note}, {note_F4, quarter_note},
//  {note_G4, quarter_note},{note_Eb4, quarter_note}, {note_F4, eighth_note},
//  {note_G4, eighth_note},{note_Ab4, eighth_note},{note_F4, eighth_note},{note_G4, dotted_quarter},
//  {note_F4, eighth_note},{note_Eb4, quarter_note},{note_D4, quarter_note},{note_Eb4, half_note}};
//
//  int verse_2[17][2]= {{ note_F4, dotted_quarter},{note_G4, eighth_note},{note_Ab4, quarter_note},{note_F4, quarter_note},
//  {note_G4, dotted_quarter},{note_Ab4, eighth_note},{note_Bb4, quarter_note},{note_F4, quarter_note},{note_G4, eighth_note},
//  {note_A4, eighth_note},{note_Bb4, quarter_note},{note_C5, eighth_note},{note_D5, eighth_note},{note_Eb5, quarter_note},
//  {note_D5, quarter_note},{note_C5, quarter_note},{note_Bb4, half_note}};
//
//  int verse_3[18][2]= {{note_Bb4, dotted_quarter}, {note_Ab4, eighth_note},{note_G4, quarter_note},
//  {note_F4, quarter_note},{note_Eb4, quarter_note}, {note_F4, quarter_note},
//  {note_G4, quarter_note},{note_Eb4, quarter_note}, {note_C5, eighth_note},{note_C5, eighth_note},{note_C5, eighth_note},
//  {note_C5, eighth_note},{note_Bb4, dotted_quarter},{ note_Ab4, eighth_note},
//  {note_G4, quarter_note},{note_F4, quarter_note},{note_Eb4, half_note}};
//  
//  for (int i=0; i<3; i++){
//    Serial.print("First Loop");
//    Serial.println(i);
//    
//    for (int note=0; note< sizeof(verse_1)-1; note++){
//      int frequency= verse_1[note][0];
//      int duration= verse_1[note][1];
//      Serial.print("note: ");
//      Serial.println(note);
//      tone(piezo_pin, frequency, duration);
//      delay(duration);
//     }
//   }
//
//   for (int note=0; note< sizeof(verse_2)-1; note++){
//      int frequency2= verse_2[note][0];
//      int duration2= verse_2[note][1];
//      tone(piezo_pin, frequency2, duration2);
//      delay(duration2);}
//
//   for (int note=0; note< sizeof(verse_3)-1; note++){
//      int frequency3= verse_3[note][0];
//      int duration3= verse_3[note][1];
//      tone(piezo_pin, frequency3, duration3);
//      delay(duration3);}
  //verse1
  tone(piezo_pin, note_Bb4, dotted_quarter);
  delay(600);
  tone(piezo_pin, note_Ab4, eighth_note);
  delay(200);
  tone(piezo_pin, note_G4, quarter_note);
  delay(400);
  tone(piezo_pin, note_F4, quarter_note);
  delay(400);
  tone(piezo_pin, note_Eb4, quarter_note);
  delay(400);
  tone(piezo_pin, note_F4, quarter_note);
  delay(400);
  tone(piezo_pin, note_G4, quarter_note);
  delay(400);
  tone(piezo_pin, note_Eb4, quarter_note);
  delay(400);
  tone(piezo_pin, note_F4, eighth_note);
  delay(200);
  tone(piezo_pin, note_G4, eighth_note);
  delay(200);
  tone(piezo_pin, note_Ab4, eighth_note);
  delay(200);
  tone(piezo_pin, note_F4, eighth_note);
  delay(200);
  tone(piezo_pin, note_G4, dotted_quarter);
  delay(600);
  tone(piezo_pin, note_F4, eighth_note);
  delay(200);
  tone(piezo_pin, note_Eb4, quarter_note);
  delay(400);
  tone(piezo_pin, note_D4, quarter_note);
  delay(400);
  tone(piezo_pin, note_Eb4, half_note);
  delay(800);

  tone(piezo_pin, note_Bb4, dotted_quarter);
  delay(600);
  tone(piezo_pin, note_Ab4, eighth_note);
  delay(200);
  tone(piezo_pin, note_G4, quarter_note);
  delay(400);
  tone(piezo_pin, note_F4, quarter_note);
  delay(400);
  tone(piezo_pin, note_Eb4, quarter_note);
  delay(400);
  tone(piezo_pin, note_F4, quarter_note);
  delay(400);
  tone(piezo_pin, note_G4, quarter_note);
  delay(400);
  tone(piezo_pin, note_Eb4, quarter_note);
  delay(400);
  tone(piezo_pin, note_F4, eighth_note);
  delay(200);
  tone(piezo_pin, note_G4, eighth_note);
  delay(200);
  tone(piezo_pin, note_Ab4, eighth_note);
  delay(200);
  tone(piezo_pin, note_F4, eighth_note);
  delay(200);
  tone(piezo_pin, note_G4, dotted_quarter);
  delay(600);
  tone(piezo_pin, note_F4, eighth_note);
  delay(200);
  tone(piezo_pin, note_Eb4, quarter_note);
  delay(400);
  tone(piezo_pin, note_D4, quarter_note);
  delay(400);
  tone(piezo_pin, note_Eb4, half_note);
  delay(800);


//  //verse2
  tone(piezo_pin, note_F4, dotted_quarter);
  delay(600);
  tone(piezo_pin, note_G4, eighth_note);
  delay(200);
  tone(piezo_pin, note_Ab4, quarter_note);
  delay(400);
  tone(piezo_pin, note_F4, quarter_note);
  delay(400);
  tone(piezo_pin, note_G4, dotted_quarter);
  delay(600);
  tone(piezo_pin, note_Ab4, eighth_note);
  delay(200);
  tone(piezo_pin, note_Bb4, quarter_note);
  delay(400); 
  tone(piezo_pin, note_F4, quarter_note);
  delay(400);
  tone(piezo_pin, note_G4, eighth_note);
  delay(200);
  tone(piezo_pin, note_A4, eighth_note);
  delay(200); 
  tone(piezo_pin, note_Bb4, quarter_note);
  delay(400);  
  tone(piezo_pin, note_C5, eighth_note);
  delay(200);
  tone(piezo_pin, note_D5, eighth_note); 
  delay(200); 
  tone(piezo_pin, note_Eb5, quarter_note);
  delay(400); 
  tone(piezo_pin, note_D5, quarter_note);
  delay(400);
  tone(piezo_pin, note_C5, quarter_note);
  delay(400);
  tone(piezo_pin, note_Bb4, half_note);
  delay(800);



  
//  //verse3
    tone(piezo_pin, note_Bb4, dotted_quarter);
    delay(600);
    tone(piezo_pin, note_Ab4, eighth_note);
    delay(200);
    tone(piezo_pin, note_G4, quarter_note);
    delay(400);
    tone(piezo_pin, note_F4, quarter_note);
    delay(400);
    tone(piezo_pin, note_Eb4, quarter_note);
    delay(400);
    tone(piezo_pin, note_F4, quarter_note);
    delay(400);
    tone(piezo_pin, note_G4, quarter_note);
    delay(400);
    tone(piezo_pin, note_Eb4, quarter_note);
    delay(400);
    tone(piezo_pin, note_C5, eighth_note);
    delay(200);
    tone(piezo_pin, note_C5, eighth_note);
    delay(200);
    tone(piezo_pin, note_C5, eighth_note); 
    delay(200);
    tone(piezo_pin, note_C5, eighth_note);
    delay(200);
    tone(piezo_pin, note_Bb4, dotted_quarter);
    delay(600);
    tone(piezo_pin, note_Ab4, eighth_note); 
    delay(200);  
    tone(piezo_pin, note_G4, quarter_note);
    delay(400);
    tone(piezo_pin, note_F4, quarter_note);
    delay(400);
    tone(piezo_pin, note_Eb4, half_note);  
    delay(3000);

  
 
  //PLAY YOUR SONG HERE
}
