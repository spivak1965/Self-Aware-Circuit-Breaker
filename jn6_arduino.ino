const int lightPin = 8; // pin connected to the light/relay

void setup() {
  pinMode(lightPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    if (cmd == "ON") digitalWrite(lightPin, HIGH);
    else if (cmd == "OFF") digitalWrite(lightPin, LOW);
  }
}
