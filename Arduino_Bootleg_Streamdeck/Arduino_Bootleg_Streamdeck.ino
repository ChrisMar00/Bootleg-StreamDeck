/*
  Bootleg StreamDeck 1.0
  Created by Christian Marotta
*/

#define CMD_LENGTH 32//This is the max length of the command, change it if a bigger command string is needed
#define CMD_START '['//Start point of the command, can be customized, but still use brackets
#define CMD_END ']'//End point of the command

char cmd[CMD_LENGTH];//Command string
bool newData = false;//Used to indicate if there's new data or not
bool isReceiving = false;//Controls that newData is being received. Turned true if the first incoming char is the CMD_START one

void setup() {
  while (!Serial);
  Serial.begin(9600);
  Serial.println("Bootleg StreamDeck ON!");
}

void loop() {
  getData();//Reads data from the serial bus 
  showData();//Shows the command entered
}

//Input control from python script
void getData() {
  static byte nc = 0;
  char rc;
  while (Serial.available() > 0 and newData == false) {//If there're bytes coming in and newData is false we read from Serial
    rc = Serial.read();
    if (isReceiving == true) {//isReceiving is true only if the first char is the CMD_START character
      if (rc != CMD_END) {
        cmd[nc++] = rc;//If the char incoming isn't the CMD_END character, then it's stored in the cmd array
        if (nc >= CMD_LENGTH) {
          nc = CMD_LENGTH - 1;
        }
      } else {
        newData = true;//If the char incoming is the CMD_END character, the last char is set to '\0' and the receiving is stopped
        isReceiving = false;
        cmd[nc] = '\0';
        nc = 0;
      }
    } else if (rc == CMD_START) {//If the incoming char is the CMD_START character, start receiving
      isReceiving = true;
    }
  }
}

void showData() {
  if (newData == true) {
    Serial.println(cmd);
    newData = false;
  }
}
