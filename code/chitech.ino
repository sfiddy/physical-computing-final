#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiServer.h>
#include <WiFiUdp.h>

#include <ArduinoHttpClient.h>



// Wifi Authentication
const char* ssid = "DukeOpen";
const char* password =  "";

// Wifi Client initialization
char serverAddress[] = "10.194.6.14";  // server address
int port = 5000;
WiFiClient wifi;
HttpClient client = HttpClient(wifi, serverAddress, port);
int status = WL_IDLE_STATUS;
String response;
int statusCode = 0;

// Shake Sensor
const int PIEZO_PIN = 36; // Piezo output
int shakeValue;
 
String PostData; 

void setup() {
 
  Serial.begin(115200);
  delay(4000);   //Delay needed before calling the WiFi.begin
 
 
  shakeValue = 0;
  
  while (WiFi.status() != WL_CONNECTED) { //Check for the connection
    delay(1000);
    Serial.println("Connecting to WiFi..");
    WiFi.begin(ssid, password); 
  }

  Serial.println("Connected to the WiFi network");
 
}

void loop() {
  int piezoADC = analogRead(PIEZO_PIN);
  float piezoV = piezoADC / 1023.0 * 5.0;

  if (piezoV > 0.00 ) {
      Serial.println("Shake detected. Commencing Post...");
      PostData = "{\"id\": \"2\", \"shakeValue\": \"1\"}";
      Serial.println("making POST request");
    
      client.beginRequest();
      client.post("/postjson");
      client.sendHeader("Content-Type", "application/json");
      client.sendHeader("Content-Length", PostData.length());
      client.sendHeader("X-Custom-Header", "custom-header-value");
      client.beginBody();
      client.print(PostData);
      client.endRequest();
      Serial.println("Post Request Made");
      // read the status code and body of the response
      statusCode = client.responseStatusCode();
      response = client.responseBody();
    
      Serial.print("Status code: ");
      Serial.println(statusCode);
      Serial.print("Response: ");
      Serial.println(response);
    
      Serial.println("Wait five seconds");
      delay(5000);
  } else {
    Serial.println("waiting for shake...");
  }


}
