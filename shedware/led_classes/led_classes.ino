#include <Adafruit_NeoPixel.h>

enum pattern { NONE, PATTERN_1, PATTERN_2 };
enum direction { FORWARD, REVERSE };

//Define neopattern class

class NeoPatterns : public Adafruit_NeoPixel{
  public:
  
  pattern ActivePattern;  // which pattern is running
  direction Direction;    //  direction to run the pattern
  
  unsigned long Interval; // milliseconds between updates
  unsigned long lastUpdate;    // last update of position
  
  uint32_t Colour1, Colour2;  // What colours are in use?
  uint16_t TotalSteps;        // total number of steps in the pattern
  uint16_t Index;    // current step within the pattern
  
  void (*OnComplete)();    // callback on completion of the pattern
  
  // Constructor
  
  NeoPatterns(uint16_t pixels, uint8_t pin, uint8_t type, void (*callback)())
  :Adafruit_NeoPixel(pixels, pin, type){
    OnComplete = callback;
  }
  
  //Update the pattern
  void Update(){
    if((millis() - lastUpdate) > Interval){
      lastUpdate = millis();
      switch(ActivePattern){
        case PATTERN_1:
          Pattern_1Update();
          break;
        case PATTERN_2:
          Pattern_2Update();
          break;
        default:
          break;
      }
    }
  }
  
  //Increment the index and reset at the end
  void Increment(){
    if (Direction == FORWARD){
      Index++;
      if (Index >= TotalSteps){
        Index = 0;
        if (OnComplete != NULL){
          OnComplete();  // call the completion callback, pattern has ended
        }
      }
    }
    else {
      --Index;
      if (Index <= 0){
        Index = TotalSteps-1;
        if (OnComplete != NULL){
          OnComplete();
        }
      }
    }
  }
  
  //Reverse pattern direction
  void Reverse(){
    if (Direction == FORWARD){
      Direction = REVERSE;
      Index = TotalSteps-1;
    }
    else{
      Direction = FORWARD;
      Index = 0;
    }
  }
  
  // Set all pixels to solid colour
  void ColourSet(uint32_t colour){
    for(int i = 0; i < numPixels(); i++){
      setPixelColor(i, colour);
    }
    show();
  }
  
  // Pattern 1
  // Initialise pattern
  void Pattern_1(uint32_t colour1, uint32_t colour2, uint8_t interval, direction dir = FORWARD){
    ActivePattern = PATTERN_1;
    Interval = interval;
    TotalSteps = numPixels();
    Colour1 = colour1;
    Colour2 = colour2;
    Index = 0;
    Direction = dir;
  }
  
  // Update pattern
  void Pattern_1Update(){
    for(int i=0; i< numPixels(); i++){
      if ((i + Index) % 3 == 0){
        setPixelColor(i, Colour1);
      }
      else{
        setPixelColor(i, Colour2);
      }
    }
    show();
    Increment();
  }
  
  // Pattern 2
  // Initialise pattern
  void Pattern_2(uint32_t colour, uint8_t interval, direction dir = FORWARD){
    ActivePattern = PATTERN_2;
    Interval = interval;
    TotalSteps = numPixels();
    Colour1 = colour;
    Index = 0;
    Direction = dir;
  }
  
  // Update pattern
  void Pattern_2Update(){
    setPixelColor(Index, Colour1);
    show();
    Increment();
  }
  
  uint32_t Wheel(byte WheelPos)
    {
        WheelPos = 255 - WheelPos;
        if(WheelPos < 85)
        {
            return Color(255 - WheelPos * 3, 0, WheelPos * 3);
        }
        else if(WheelPos < 170)
        {
            WheelPos -= 85;
            return Color(0, WheelPos * 3, 255 - WheelPos * 3);
        }
        else
        {
            WheelPos -= 170;
            return Color(WheelPos * 3, 255 - WheelPos * 3, 0);
        }
    }
};

void StickComplete();

NeoPatterns Stick1(60, 4, NEO_GRB + NEO_KHZ800, &StickComplete);

void setup(){
  Serial.begin(115200);
  
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  
  Stick1.begin();
  
  Stick1.ColourSet(Stick1.Color(255,0,0));
}

void loop(){
  Stick1.Update();
  
  if (digitalRead(11) == HIGH){
    Stick1.ActivePattern = PATTERN_1;
    Stick1.Interval = 20;
  }
  
    else if (digitalRead(10) == HIGH){
    Stick1.ActivePattern = PATTERN_2;
  }
}

    
    
void StickComplete(){
  Stick1.Colour1 = Stick1.Wheel(random(255));
}

  
  


//class Flamethrower  
