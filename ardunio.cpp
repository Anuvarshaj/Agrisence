#define BLYNK_PRINT Serial

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
#include <DHT.h>

// ---------------- BLYNK CREDENTIALS ----------------
char auth[] = "YOUR_BLYNK_AUTH_TOKEN";
char ssid[] = "YOUR_WIFI_NAME";
char pass[] = "YOUR_WIFI_PASSWORD";

// ---------------- DHT SETUP ----------------
#define DHTPIN D4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// ---------------- SENSOR PINS ----------------
#define SOIL_MOISTURE_PIN A0
#define PH_SENSOR_PIN A0   // Using same analog (use multiplexer if multiple analog sensors)

// ---------------- TIMER ----------------
BlynkTimer timer;

// ---------------- FUNCTION TO READ SENSORS ----------------
void sendSensorData()
{
  // 🌡 Read DHT11
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // 🌱 Read Soil Moisture
  int soilValue = analogRead(SOIL_MOISTURE_PIN);

  // Convert to percentage
  int soilMoisture = map(soilValue, 1023, 300, 0, 100);

  // 🧪 Read pH sensor (basic conversion)
  float phValue = analogRead(PH_SENSOR_PIN);
  float voltage = phValue * (3.3 / 1023.0);
  float ph = 7 + ((2.5 - voltage) / 0.18);  // Approx formula

  // ---------------- SERIAL MONITOR ----------------
  Serial.println("---- AgriSense Data ----");
  Serial.print("Temperature: ");
  Serial.println(temperature);

  Serial.print("Humidity: ");
  Serial.println(humidity);

  Serial.print("Soil Moisture: ");
  Serial.println(soilMoisture);

  Serial.print("pH Value: ");
  Serial.println(ph);

  // ---------------- SEND TO BLYNK ----------------
  Blynk.virtualWrite(V0, temperature);
  Blynk.virtualWrite(V1, humidity);
  Blynk.virtualWrite(V2, soilMoisture);
  Blynk.virtualWrite(V3, ph);
}

// ---------------- SETUP ----------------
void setup()
{
  Serial.begin(9600);

  Blynk.begin(auth, ssid, pass);

  dht.begin();

  // Read sensor every 2 seconds
  timer.setInterval(2000L, sendSensorData);
}

// ---------------- LOOP ----------------
void loop()
{
  Blynk.run();
  timer.run();
}
