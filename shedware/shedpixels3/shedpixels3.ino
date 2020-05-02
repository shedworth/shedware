#include <Adafruit_NeoPixel.h>

// char receivedChar;
boolean newData = false;
String inString = "";
int inFixInt = 0;
int inFuncInt = 0;
uint32_t inCol1Int = 0;
uint32_t inCol2Int = 0;
int inInterInt = 0;

// Pattern types supported:
enum  pattern { NONE, RAINBOW_CYCLE, THEATER_CHASE, COLOR_WIPE, SCANNER, FADE };
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
                case FADE:
                    FadeUpdate();
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
    
    // Initialize for a Fade
    void Fade(uint32_t color1, uint32_t color2, uint16_t steps, uint8_t interval, direction dir = FORWARD)
    {
        ActivePattern = FADE;
        Interval = interval;
        TotalSteps = steps;
        Color1 = color1;
        Color2 = color2;
        Index = 0;
        Direction = dir;
    }
    
    // Update the Fade Pattern
    void FadeUpdate()
    {
        // Calculate linear interpolation between Color1 and Color2
        // Optimise order of operations to minimize truncation error
        uint8_t red = ((Red(Color1) * (TotalSteps - Index)) + (Red(Color2) * Index)) / TotalSteps;
        uint8_t green = ((Green(Color1) * (TotalSteps - Index)) + (Green(Color2) * Index)) / TotalSteps;
        uint8_t blue = ((Blue(Color1) * (TotalSteps - Index)) + (Blue(Color2) * Index)) / TotalSteps;
        
        ColorSet(Color(red, green, blue));
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
      
      String inCol1 = (String)inString.substring(2,11);
      inCol1Int = inCol1.toInt();
      Serial.println(inCol1Int);
      
      String inCol2 = (String)inString.substring(11,20);
      inCol2Int = inCol2.toInt();
      Serial.println(inCol2Int);
      
      String inInter = (String)inString.substring(20,24);
      inInterInt = inInter.toInt();
      Serial.println(inInterInt);
      
      
      
      inString = "";
      newData = true;
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
NeoPatterns Ring3(10, 2, NEO_GRB + NEO_KHZ800, &StickComplete);

Solenoid Solenoid1(5);

int tempo = 173;
float longperiod = ((tempo / 42)*2);
float shortperiod = (tempo / 9);

// Initialize everything and prepare to start
void setup()
{
  Serial.begin(115200);

    
    // Initialize all the pixelStrips
    Ring1.begin();
    Ring2.begin();
    Ring3.begin();
    
    // Kick off a pattern
    // Ring1.TheaterChase(Ring1.Color(255,0,0), Ring1.Color(0,0,255), (longperiod * 16));
    // Ring2.RainbowCycle(3);
  //  Ring2.Color1 = Ring1.Color1;
   // Ring3.Scanner(Ring1.Color(60,150,150), 55);
    //Ring1.ColorSet(Ring1.Color(150,0,200));
    //Ring2.ColorSet(Ring2.Color(150,0,200));
    
   // Ring1.Scanner(Ring1.Color(200,200,0),1000);
  //  Ring2.Scanner(Ring2.Color(200,200,0),(longperiod * 16));
   // Ring3.ColorSet(Ring3.Color(15,25,25));
   // Solenoid1.Fire(10000);
}

// Main loop
void loop()
{
  recvInfo();
  if (newData == true)
  {
    Serial.println(inFixInt);
    
    newData = false;
    
    if (inFixInt == 1)
    {
      Ring3.ColorSet(Ring3.Color(255,0,0));
    }
    if (inFixInt == 2)
    {
      Ring3.ColorSet(Ring3.Color(0,255,0));
    }
    if (inFixInt == 3)
    {
      Ring3.ColorSet(Ring3.Color(0,0,255));
    }
    if (inFixInt == 4)
    {
      Ring3.ColorSet(Ring3.Color(0,0,0));
    }
    if (inFixInt == 5)
    {
      Solenoid1.Fire(1000);
    }
    if (inFixInt == 0)
    {
      Ring1.Scanner(Ring1.Color(200,200,0),100);
      Ring2.Scanner(Ring2.Color(200,200,0),100);
    }
  }
  
  
    // Update the rings.
    Ring1.Update();
    Ring2.Update(); 
    Ring3.Update();   
    Solenoid1.Update();
    
   
}

//------------------------------------------------------------
//Completion Routines - get called on completion of a pattern
//------------------------------------------------------------

// Ring1 Completion Callback
void Ring1Complete()
{
    
}

// Ring 2 Completion Callback
void Ring2Complete()
{
    
}

// Stick Completion Callback
void StickComplete()
{
    // Random color change for next scan
   
}
