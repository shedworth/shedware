// Solenoid Class - operates flamethrower
class Solenoid
{
  public:
  
  // Member variables:
  boolean IsOpen;  // true when solenoid open
  unsigned long Interval;
  unsigned long lastUpdate;
  
  void (*OnComplete)();  // Callback on completion of pattern
  void Fire();
  
  // Constructor:
  
  Solenoid(uint8_t pin, void (*callback)())
  {
    uint8_t _pin = pin;
    OnComplete = callback;
  }
  
  void Update(){
    if((millis() - lastUpdate) > Interval)
    {
      lastUpdate = millis();
      FireUpdate();
    }
  }
  
  
  
  
  void Solenoid ::Fire(uint8_t interval){
    Interval = interval;
  }
  
  void Solenoid::FireUpdate(){
    if (IsOpen == 1) {
      digitalWrite(_pin, LOW);
    }
    if (IsOpen == 0) {
      digitalWrite(_pin, HIGH);
    }
  }
  
  
}
