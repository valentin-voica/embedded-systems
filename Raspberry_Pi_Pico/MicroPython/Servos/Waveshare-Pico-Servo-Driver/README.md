# Waveshare Pico Servo Driver

A MicroPython class and example code using the Programmable Input/Output (PIO) state machines to drive the servos, for the ["Waveshare Pico Servo Driver" board for Raspberry Pi Pico](https://www.waveshare.com/wiki/Pico-Servo-Driver). The servos are connected to GP0 to GP7. Even if the Waveshare board makes provisions for 16 servo motors to be connected, the Raspberry Pi Pico is limited to 8 state machines.

Save `ServoDriver.py` file onto the Pico so it can be imported. This code is designed to be used as a module (see [A practical Guide to Modules, Micro Python and the Raspberry Pi Pico](https://kitronik.co.uk/blogs/resources/modules-micro-python-and-the-raspberry-pi-pico) for more information).

## Import ServoDriver.py and construct an instance:

```
import ServoDriver
board = ServoDriver.WavesharePicoServoDriver()
```

Save it on the Pico as `initialisePIO.py` (or `main.py` if you want to autostart after powering up the board). This will initialise the PIO and set them to drive the servo pins. It also sets the initial position for all servos at 90 degrees.

## There are three ways to drive a servo

### 1. By degrees:

`board.goToPosition(servo, degrees)`

where:
* servo => 1 to 8
* degrees => 0 to 180

### 2. By radians:

`board.goToRadians(servo, radians)`

where:
* servo => 1 to 8
* radians => 0 to 3.1416 (Pi to four digits)

### 3. Drive the servo directly, by entering the pulse width:

`board.goToPeriod(servo, period)`

where:
* servo => 1 to 8
* period => 500 to 2500 (pulse width in microseconds)

## Examples

### Control one servo with a switch connected to GP16

* For movement with no delay use the `TBD` file.

* For slow movement use the `TBD` file.

### Control eight servos with eight switches

The switches are connected to GP8 to GP15 (even if these are designated for connecting servo motors, as the Pico has only 8 state machines, we can use these terminals for the switches).

* For movement with no delay use the `TBD` file.

* For slow movement use the `control_servo_x8-slow.py` file.

## Troubleshooting

Exception rasied as - **ValueError: StateMachine claimed by external resource**
- Likely caused by using the wireless chip on the Pico W, as well as using all sixteen servos.
- Can be solved by using the Simply Servos library from the folder `Library Without PIO`.
