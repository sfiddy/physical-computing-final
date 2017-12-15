# Final Project - Physical Computing and the Internet of Things

*Name:*  Stephanie Fiddy  

*Date:* 12/14/17

## Project:  Chitech / Esp32 Thing

![Chitech Logo](images/logo.png)

Chitech is a psychometric IoT device that monitors your dog’s shaking patterns. Chitech is accompanied with the Chitech webapp in which gives you a better insight into the psychology of your pet. 


### Detailed Project Description

Wearable technology in today's consumer market  has expanded to include products tailored to our closest companions, our pets. These devices have given pet owners the ability to closely monitor their furry companions with the hopes of using  the data gathered to improve their pets health and wellness. As a proud owner of a four year old Chihuahua (named Chloe), wearable technology for animals inspired me to construct my own. 

Small dogs, especially Chihuahuas are known to respond to excitement by shaking. From my interest in discovering what excites Chloe the most, my idea for Chitech was born. My product is a non-invasive wearable device tailored for small dogs. This device detects vibrations and transmits that data to the accompanying webapp where pet owners can get a better understanding of their dog's behavioral patterns. 

When the Chitech device detects that the dog is shaking, it transmits that data to the webapp. The webapp then prompts the user to record the nature of the event that triggered the excitable response. Through time, the user is able to analyze the data collected in order to get a deeper understanding of their dog's motivations and preferences. 

There is both a utilitarian and an analytical component to Chitech. My prototype explores how the data collected from our beloved pets is being protected and disseminated by the companies selling these wearable devices. 

### Technical Description

For my project, size was of the upmost importance. Because I needed a device that would comfortably fit on my small dog, I decided to go with the Esp32 thing for various reasons. For one, the 'thing' is one of the smallest microcontrollers on the market. The Esp32 also has wifi compatibility and features a lithium-polymer (LiPo) battery port making it a compact and easily transportable device. Further explanation on the hardware used in and development of this project can be found in the "Hardware Wiring Diagram" sub-section below. 

I also developed a full stack website to support the Chitech product. The website consists of a bootstrap frontend, a flask backend and a sqlite3 database. This webapp provides the user with an interface to log the nature of the event that excited your dog.  I decided to produce a web application because it was the most suitable platform to couple with the physical device. The web's portability and multi-platform use made it the ideal interface for the on-the-go dog owner. 

![POST Request Confirmation](images/post-request.png)

The Esp32 thing connects with the webapp by sending an HTTP POST request to the flaskapp. The web app receives the post request and is intended to prompt the user to submit the "excitable event" that caused the dog to shake.  I was able to establish the connectivity between the Esp32 thing and the flask web app with very limited success. The arduino device confirms that the "shake value" is posting to the app, but unfortunately the web app does not appear to receive the value. This is likely due to the fact that the libraries for the Esp32 thing is still under development (as noted on the Sparkfun website). However, each individual component works independently and this was the missing piece to my project. 


#### Hardware Wiring Diagram

![Fritzing](images/fritzing.png)
![Esp32 Thing Wiring](images/wiring.png)
![Piezo Vibration Sensor](images/piezo-vibration-sensor.png)

I chose to use the Esp32 thing because it is small enough to comfortably be attached to my five pound dog, Chloe. There was some prepping involved for getting the esp32 thing ready for use. First of all, I decided to solder some headers onto the microcontroller for easy connection. 

I faced two challenges when working on the hardware. First of all, finding a sensor that accurately and consistenly detected vibrations was extremely challenging. At first I attempted to use an uncovered and covered Piezo Element, running multiple trials and comparing the results from each sensor. Despite countless trials, the piezo element continued to give variable and unrealiable vibration readings. 

The Piezo Vibration Sensor proved to the most adequate sensor for Chitech since it accurately detected vibrations when the device was shaken. However the Piezo Vibration Sensor proved to only accurately detect a standard "shake" when it had a weight attached to it. As a solution to this problem, I chose to tape two nails onto the sensor since the nails were compact and heavy enough to product consistent results. I chose to tape the nails instead of gluing them for fear that the latter would potentially ruin the sensor. 

#### Code

< Explain your code.  You might include code snippets, either `inline` or
```c++
//Multiline
bool photon_fun = TRUE;
```
You should link to your full code, either included in the repository (e.g. [my_code.ino](code/my_code.ino)  or to the Shared Revision in your Particle IDE. >


### Design / Form

< Explain the device's form, the aesthetic choices made and how they relate to the concept/function the device is intended to engage >

< include photos of your device >

### Evaluation / Reflection

< What is your own evaluation of your project?   What did you learn through this project?  What would you do differently in the future? >
