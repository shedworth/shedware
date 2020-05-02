#include <LiquidCrystal.h>

char serialdata[80];

String inString = "";

void setup(){
  Serial.begin(9600);
  
}

void loop(){
  while (Serial.available() > 0){
    //String inString = "";
    int inChar = Serial.read();
    if (isDigit(inChar)){
      inString +=(char)inChar;
    }
    if (inChar == '\n'){
      Serial.println(inString);
         
      String inFix = (String)inString[0];
      int inFixInt = inFix.toInt();
      Serial.println(inFixInt);
      
      String inFunc = (String)inString[1];
      int inFuncInt = inFunc.toInt();
      Serial.println(inFuncInt);
      
      String inCol1 = (String)inString.substring(2,11);
      uint32_t inCol1Int = inCol1.toInt();
      Serial.println(inCol1Int);
      int Col1R = inCol1Int / 1000000;
      Serial.println(Col1R);
      
      String inCol2 = (String)inString.substring(11,20);
      uint32_t inCol2Int = inCol2.toInt();
      Serial.println(inCol2Int);
      
      String inInter = (String)inString.substring(20,24);
      int inInterInt = inInter.toInt();
      Serial.println(inInterInt);
      
      
      
      inString = "";
    }
  }
}


