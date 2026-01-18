# Kitronik Simply Servos Board for Raspberry Pi Pico

A MicroPython class and example code to use the [Kitronik Simply Servos board for Raspberry Pi Pico](https://kitronik.co.uk/products/5339-simply-servos-for-raspberry-pi-pico) which uses the Programmable Input/Output (PIO) state machines to drive the servos.

As a servo-motors [HD-1370A servos](https://www.chd.hk/Product_Detail.aspx?id=30) can be used.

To use save SimpyServos.py file onto the Pico so it can be imported. This code is designed to be used as a module. See: "[A practical Guide to Modules, Micro Python and the Raspberry Pi Pico](https://kitronik.co.uk/blogs/resources/modules-micro-python-and-the-raspberry-pi-pico) for more information.

## Import SimplyServos.py and construct an instance:

```
import SimplyServos
board = SimplyServos.KitronikSimplyServos()
```

This will initialise the PIO and set them to drive the servo pins. It also set the initial position at 90 degrees.

## The three ways to drive a servo

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

### 3. Drive a Servo by pulse width:

`board.goToPeriod(servo, period)`

where:
* servo => 1 to 8
* period => 500 to 2500 (pulse width in microseconds)

## Examples

### Control one servo with a switch connected to GP0

* For movement with no delay use the `servo_x1-demo.py` file.

* For slow movement use the `servo_x1-slow-demo` file.

### Control five servos with five switches connected to GP0, GP1, GP26, GP27, and GP28

* For movement with no delay use the `control_servo_x5.py` file.

* For slow movement use the `control_servo_x5-slow.py` file.

## Diagrams

Below is a diagram for using two servos controlled by two SPST switches.

![Diagram](/Examples/images/Diagram.jpg)

## Troubleshooting

Exception rasied as - **ValueError: StateMachine claimed by external resource**
- Likely caused by using the wireless chip on the Pico W, as well as using all eight servos.
- Can be solved by using the Simply Servos library from the folder `Library Without PIO`.
