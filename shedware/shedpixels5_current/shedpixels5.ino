#include <Adafruit_NeoPixel.h>

// char receivedChar;
boolean newData = false;
String inString = "";
int inFixInt = 0;
int inFuncInt = 0;
uint32_t inCol1Int = 0;
uint32_t inCol2Int = 0;
uint8_t inInterInt = 0;

// Pattern types supported:
enum  pattern { NONE, RAINBOW_CYCLE, THEATER_CHASE, COLOR_WIPE, SCANNER, CHOP, SOLID };
// Patern directions supported:
enum  direction { FORWARD, REVERSE };


// NeoPattern Class - derived from the Adafruit_NeoPixel class
class NeoPatterns : public Adafruit_NeoPixel
{
    public:

    // Member Variables:  
    pattern  ActivePattern;  // which pattern is running
    direction Direction;     // direction to run the pattern
    
    unsigned long Interval;   // milliseconds between updates
    unsigned long lastUpdate; // last update of position
    
    uint32_t Color1, Color2;  // What colors are in use
    uint16_t TotalSteps;  // total number of steps in the pattern
    uint16_t Index;  // current step within the pattern
    
    void (*OnComplete)();  // Callback on completion of pattern
    
    // Constructor - calls base-class constructor to initialize strip
    NeoPatterns(uint16_t pixels, uint8_t pin, uint8_t type, void (*callback)())
    :Adafruit_NeoPixel(pixels, pin, type)
    {
        OnComplete = callback;
    }
    
    // Update the pattern
    void Update()
    {
        if((millis() - lastUpdate) > Interval) // time to update
        {
            lastUpdate = millis();
            switch(ActivePattern)
            {
                case RAINBOW_CYCLE:
                    RainbowCycleUpdate();
                    break;
                case THEATER_CHASE:
                    TheaterChaseUpdate();
                    break;
                case COLOR_WIPE:
                    ColorWipeUpdate();
                    break;
                case SCANNER:
                    ScannerUpdate();
                    break;
                case CHOP:
                    ChopUpdate();
                    break;
                case SOLID:
                    SolidUpdate();
                    break;
                default:
                    break;
            }
        }
    }
  
    // Increment the Index and reset at the end
    void Increment()
    {
        if (Direction == FORWARD)
        {
           Index++;
           if (Index >= TotalSteps)
            {
                Index = 0;
                if (OnComplete != NULL)
                {
                    OnComplete(); // call the comlpetion callback
                }
            }
        }
        else // Direction == REVERSE
        {
            --Index;
            if (Index <= 0)
            {
                Index = TotalSteps-1;
                if (OnComplete != NULL)
                {
                    OnComplete(); // call the comlpetion callback
                }
            }
        }
    }
    
    // Reverse pattern direction
    void Reverse()
    {
        if (Direction == FORWARD)
        {
            Direction = REVERSE;
            Index = TotalSteps-1;
        }
        else
        {
            Direction = FORWARD;
            Index = 0;
        }
    }
    
    // Initialize for a RainbowCycle
    void RainbowCycle(uint8_t interval, direction dir = FORWARD)
    {
        ActivePattern = RAINBOW_CYCLE;
        Interval = interval;
        lastUpdate = millis();
        TotalSteps = 255;
        Index = 0;
        Direction = dir;
    }
    
    // Update the Rainbow Cycle Pattern
    void RainbowCycleUpdate()
    {
        for(int i=0; i< numPixels(); i++)
        {
            setPixelColor(i, Wheel(((i * 256 / numPixels()) + Index) & 255));
        }
        show();
        Increment();
    }

    // Initialize for a Theater Chase
    void TheaterChase(uint32_t color1, uint32_t color2, uint8_t interval, direction dir = FORWARD)
    {
        ActivePattern = THEATER_CHASE;
        Interval = interval;
        lastUpdate = millis();
        TotalSteps = numPixels();
        Color1 = color1;
        Color2 = color2;
        Index = 0;
        Direction = dir;
   }
    
    // Update the Theater Chase Pattern
    void TheaterChaseUpdate()
    {
        for(int i=0; i< numPixels(); i++)
        {
            if ((i + Index) % 3 == 0)
            {
                setPixelColor(i, Color1);
            }
            else
            {
                setPixelColor(i, Color2);
            }
        }
        show();
        Increment();
    }

    // Initialize for a ColorWipe
    void ColorWipe(uint32_t color, uint8_t interval, direction dir = FORWARD)
    {
        ActivePattern = COLOR_WIPE;
        Interval = interval;
        lastUpdate = millis();
        TotalSteps = numPixels();
        Color1 = color;
        Index = 0;
        Direction = dir;
    }
    
    // Update the Color Wipe Pattern
    void ColorWipeUpdate()
    {
        setPixelColor(Index, Color1);
        show();
        Increment();
    }
    
    // Initialize for a SCANNNER
    void Scanner(uint32_t color1, uint8_t interval)
    {
        ActivePattern = SCANNER;
        Interval = interval;
        lastUpdate = millis();
        TotalSteps = (numPixels() - 1) * 2;
        Color1 = color1;
        Index = 0;
    }

    // Update the Scanner Pattern
    void ScannerUpdate()
    { 
        for (int i = 0; i < numPixels(); i++)
        {
            if (i == Index)  // Scan Pixel to the right
            {
                 setPixelColor(i, Color1);
            }
            else if (i == TotalSteps - Index) // Scan Pixel to the left
            {
                 setPixelColor(i, Color1);
            }
            else // Fading tail
            {
                 setPixelColor(i, DimColor(getPixelColor(i)));
            }
        }
        show();
        Increment();
    }
    
    // Initialize for a Chop
    void Chop(uint32_t color1, uint32_t color2, uint8_t interval, direction dir = FORWARD)
    {
        ActivePattern = CHOP;
        Interval = (interval*2);
        lastUpdate = millis();
        TotalSteps = 2;
        Color1 = color1;
        Color2 = color2;
        Index = 0;
        Direction = dir;
    }
    
    // Update the Chop Pattern
    void ChopUpdate()
    {
        if (Index == 0){
          ColorSet(Color1);
        }
        if (Index == 1){
          ColorSet(Color2);
        }
        show();
        Increment();
    }
   
    // Calculate 50% dimmed version of a color (used by ScannerUpdate)
    uint32_t DimColor(uint32_t color)
    {
        // Shift R, G and B components one bit to the right
        uint32_t dimColor = Color(Red(color) >> 1, Green(color) >> 1, Blue(color) >> 1);
        return dimColor;
    }

    // Set all pixels to a color (synchronously)
    void ColorSet(uint32_t color)
    {
        for (int i = 0; i < numPixels(); i++)
        {
            setPixelColor(i, color);
        }
        show();
    }
    
    void Solid(uint32_t color1, direction dir = FORWARD)
    {
      ActivePattern = SOLID;
      Color1 = color1;
      Interval = 10;
      lastUpdate = millis();
      TotalSteps = numPixels();
      Index = 0;
      Direction = dir;
    }
    
    void SolidUpdate()
    {
      ColorSet(Color1);
     // show();
      Increment();
    }
     
      

    // Returns the Red component of a 32-bit color
    uint8_t Red(uint32_t color)
    {
        return (color >> 16) & 0xFF;
    }

    // Returns the Green component of a 32-bit color
    uint8_t Green(uint32_t color)
    {
        return (color >> 8) & 0xFF;
    }

    // Returns the Blue component of a 32-bit color
    uint8_t Blue(uint32_t color)
    {
        return color & 0xFF;
    }
    
    // Input a value 0 to 255 to get a color value.
    // The colours are a transition r - g - b - back to r.
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



class Solenoid
{
	// Class Member Variables
	// These are initialized at startup
	int solPin;      // the number of the solenoid pin
	long length;     // length of burst

	// These maintain the current state
	int solState;             		// solState used to set the solenoid
	unsigned long previousMillis;  	// will store last time solenoid was updated

  // Constructor - creates a Solenoid 
  // and initializes the member variables and state
  public:
  Solenoid(int pin)
  {
	solPin = pin;
	pinMode(solPin, OUTPUT);     	
	solState = LOW; 
	previousMillis = 0;
  }

  void Fire(long Length)
  {
    length = Length;
    previousMillis = millis();
    solState = HIGH;
    digitalWrite(solPin, solState);
  }

  void Update()
  {
    // check to see if it's time to change the state of the LED
    unsigned long currentMillis = millis();
     
    if((solState == HIGH) && (currentMillis - previousMillis >= length))
    {
    	solState = LOW;  // Turn it off
      previousMillis = currentMillis;  // Remember the time
      digitalWrite(solPin, solState);  // Update the actual LED
    }
  }
};

void recvInfo()
{
  //inString = "";
  //newData = false;
  //inFixInt = 0;
  //inFuncInt = 0;
  //inCol1Int = 0;
  //inCol2Int = 0;
  //inInterInt = 0;
  while (Serial.available() > 0){
    int inChar = Serial.read();
    
    
    
    if (isDigit(inChar)){
      inString +=(char)inChar;
    }
    if (inChar == '\n'){
      Serial.println(inString);
         
      String inFix = (String)inString[0];
      inFixInt = inFix.toInt();
      Serial.println(inFixInt);
      
      String inFunc = (String)inString[1];
      inFuncInt = inFunc.toInt();
      Serial.println(inFuncInt);
      
      String inCol1 = (String)inString.substring(2,10);
      inCol1Int = inCol1.toInt();
      Serial.println(inCol1Int);
      
      String inCol2 = (String)inString.substring(10,18);
      inCol2Int = inCol2.toInt();
      Serial.println(inCol2Int);
      
      String inInter = (String)inString.substring(18,21);
      inInterInt = inInter.toInt();
      Serial.println(inInterInt);
      
      
      
      inString = "";
      newData = true;
      break;
    }
  }
}


void Ring1Complete();
void Ring2Complete();
void Ring3Complete();

// Define some NeoPatterns for the two rings and the stick
//  as well as some completion routines
NeoPatterns Ring1(22, 3, NEO_GRB + NEO_KHZ800, &Ring1Complete);
NeoPatterns Ring2(22, 4, NEO_GRB + NEO_KHZ800, &Ring2Complete);
NeoPatterns Ring3(10, 2, NEO_GRB + NEO_KHZ800, &Ring3Complete);

Solenoid Solenoid1(5);


// Initialize everything and prepare to start
void setup()
{
  Serial.begin(19200);

    
    // Initialize all the pixelStrips
    Ring1.begin();
    Ring2.begin();
    Ring3.begin();
    
    Ring1.ColorSet(Ring1.Color(0,0,0));
    Ring2.ColorSet(Ring2.Color(0,0,0));
    Ring3.ColorSet(Ring3.Color(0,0,0));
   
}

// Main loop
void loop()
{
  recvInfo();
  if (newData == true)
  {
    Serial.println(inFixInt);
    
    newData = false;
    
    
    switch(inFixInt){
      case 1:{              // LH roof LED strip chosen
        switch(inFuncInt){
          case 1:{            // Solid colour chosen
            Ring1.Solid(inCol1Int);
            break;
          }
          case 2:{            // Scanner chosen
            Ring1.Scanner(inCol1Int, inInterInt);
            break;
          }
          case 3:{            // Rainbow chosen
            Ring1.RainbowCycle(inInterInt);
            break;
          }
          case 4:{            // Theatre chase chosen
            Ring1.TheaterChase(inCol1Int, inCol2Int, inInterInt);
            break;
          }
          case 5:{            // Colour wipe chosen
            Ring1.ColorWipe(inCol1Int, inInterInt);
            break;
          }
          case 6:{            // Chop chosen
            Ring1.Chop(inCol1Int, inCol2Int, inInterInt);
            break;
          }
        }
        break;
      }
      
      case 2:{              // RH roof LED strip chosen
        switch(inFuncInt){
          case 1:{            // Solid colour chosen
            Ring2.Solid(inCol1Int);
            break;
          }
          case 2:{            // Scanner chosen
            Ring2.Scanner(inCol1Int, inInterInt);
            break;
          }
          case 3:{            // Rainbow chosen
            Ring2.RainbowCycle(inInterInt);
            break;
          }
          case 4:{            // Theatre chase chosen
            Ring2.TheaterChase(inCol1Int, inCol2Int, inInterInt);
            break;
          }
          case 5:{            // Colour wipe chosen
            Ring2.ColorWipe(inCol1Int, inInterInt);
            break;
          }
          case 6:{            // Chop chosen
            Ring2.Chop(inCol1Int, inCol2Int, inInterInt);
            break;
          }
        }
        break;
      }
      
      case 3:{              // Window LED strip chosen
        switch(inFuncInt){
          case 1:{            // Solid colour chosen
            Ring3.Solid(inCol1Int);
            break;
          }
          case 2:{            // Scanner chosen
            Ring3.Scanner(inCol1Int, inInterInt);
            break;
          }
          case 3:{            // Rainbow chosen
            Ring3.RainbowCycle(inInterInt);
            break;
          }
          case 4:{            // Theatre chase chosen
            Ring3.TheaterChase(inCol1Int, inCol2Int, inInterInt);
            break;
          }
          case 5:{            // Colour wipe chosen
            Ring3.ColorWipe(inCol1Int, inInterInt);
            break;
          }
          case 6:{            // Chop chosen
            Ring3.Chop(inCol1Int, inCol2Int, inInterInt);
            break;
          }
        }
        break;
      }
      
      case 4:{
        Solenoid1.Fire(inInterInt * 10);
        Serial.println("solenoid 1");
        break;
      }
    }
  }
  
      
    
   
  
  
    // Update the rings.
    Ring1.Update();
    Ring2.Update(); 
    Ring3.Update();   
    Solenoid1.Update();
   // Serial.println(Ring1.ActivePattern);
   
}

//------------------------------------------------------------
//Completion Routines - get called on completion of a pattern
//------------------------------------------------------------

// Ring1 Completion Callback
void Ring1Complete()
{
   // Ring1.ColorSet(inCol1Int);
  // Serial.println("Pattern complete 1");
}

// Ring 2 Completion Callback
void Ring2Complete()
{
    
}

// Stick Completion Callback
void Ring3Complete()
{
    // Random color change for next scan
   
}
