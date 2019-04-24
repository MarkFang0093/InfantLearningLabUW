import serial
port = "/dev/ttyACM0"#put your port here
baudrate = 1200
ser = serial.Serial(port, baudrate)
def tell(msg):
    msg = msg + '\n'
    x = msg.encode('ascii') # encode n send
    ser.write(x)

def hear():
    msg = ser.read_until() # read until a new line
    mystring = msg.decode('ascii')  # decode n return
    return mystring

while True:
    val = input() # take user input
    tell(val) # send it to arduino
    var = hear() # listen to arduino
    print(var) #print what arduino sent




#########Arduino Code##################
#
# /*
#  Stepper Motor Control - one revolution
#
#  This program drives a unipolar or bipolar stepper motor.
#  The motor is attached to digital pins 8 - 11 of the Arduino.
#
#  The motor should revolve one revolution in one direction, then
#  one revolution in the other direction.
#
#
#  Created 11 Mar. 2007
#  Modified 30 Nov. 2009
#  by Tom Igoe
#
#  */
#
# #include <Stepper.h>
#
# const int stepsPerRevolution = 600;  // change this to fit the number of steps per revolution
# // for your motor
#
# // initialize the stepper library on pins 8 through 11:
# Stepper myStepper1(stepsPerRevolution, 9, 10, 11, 12);
# Stepper myStepper2(stepsPerRevolution, 5, 6, 7, 8);
# Stepper myStepper3(stepsPerRevolution, 1, 2, 3, 4);
#
# void setup() {
#   // set the speed at 60 rpm:
#   Serial.begin(9600);
#   myStepper1.setSpeed(60);
#   myStepper2.setSpeed(60);
#   myStepper3.setSpeed(60);
#   // initialize the serial port:
#   Serial.begin(9600);
# }
#
# void loop() {


#   // step one revolution  in one direction:
#   Serial.println("clockwise");

#   //myStepper1.step(stepsPerRevolution);
#   myStepper2.step(stepsPerRevolution);
#   //myStepper3.step(stepsPerRevolution);
#
#   delay(1500);
#
#   //step one revolution in the other direction:
#   Serial.println("counterclockwise");
#   //myStepper1.step(-stepsPerRevolution);
#   myStepper2.step(-stepsPerRevolution);
#   //myStepper3.step(-stepsPerRevolution);
#
#   delay(1500);
# }
