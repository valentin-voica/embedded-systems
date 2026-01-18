# DIY Arduino Uno

Build your own Arduino Uno board

## Hardware

[DIY Arduino UNO | How to Make Your Own Arduino Uno Board](https://www.instructables.com/DIY-Arduino-UNO-How-to-Make-Your-Own-Arduino-Uno-B/)

If 3.3V is not needed, then exclude the following components:

* U2 = LM317
* C4 = 100nF
* C5 = 100µF
* R2 = 240Ω
* R3 = 390Ω

## Programmer

[Pololu USB AVR Programmer v2.1](https://www.pololu.com/product/3172)

Install the ["Pololu USB AVR Programmer v2 Software for Linux](https://www.pololu.com/docs/0J67/4.2").

Using a USB to micro-USB cable connect the programmer to the laptop and check if it is recognized, by running the command:

`$ pavr2cmd --list`

The output will show the programmer's serial number and name.

`00328037,         Pololu USB AVR Programmer v2.1 `

Run the graphic interface:

`$ pavr2gui`

Leave the default settings, and make a note of the "Programming" and "TTL" ports; identical or similar to: `/dev/ttyACM0` and `/dev/ttyACM1`.

## Install and configure Arduino IDE

Follow the instructions [here](https://docs.arduino.cc/software/ide-v1/tutorials/Linux). Do not skip the ["Please Read" section](https://docs.arduino.cc/software/ide-v1/tutorials/Linux#please-read). And make sure you restart the laptop, rather than just logging out and back in.

### Add the "MiniCore" package

[YouTube tutorial](https://www.youtube.com/watch?v=ZscDJ-xO4tA)

Open the app and navigate to "File" -> "Preferences". In the "Additional Boards Manager URLs:" field paste the link:

`https://mcudude.github.io/MiniCore/package_MCUdude_MiniCore_index.json`

Click "OK" to close the "Preferences" window.

Navigate to "Tools" -> "Board: "{current_board_name}" -> "Boards Manager...". In the "Filter your search..." field tipe: "minicore".

In the "MiniCore" section, click the "Install" button. Wait for the package to install, then click the "Close" button.

Navigate to "Tools" -> "Board: "{current_board_name}" -> ""MiniCore" and select "ATmega328". Verify in the "Tools" menu the selected variant is "328P / 328PA". For the "Port:" select the ports shown earlier for "Programming port" (`/dev/ttyACM0`).

### Select the programmer

Navigate to "Tools" -> "Programmer" and select "STK500 as ISP (MiniCore)" option.

### Burn the bootloader

Connect the DIY Arduino UNO board to an external power supply (6 - 15Vcc, central "+") and, using the flat cable, to the programmer's ISP interface. The red LED on the programmer should stop flashing.

Navigate to "Tools" and select "Burn Bootloader". Wait a couple of seconds for the bootloader to be uploaded to the ATmega328P chip.

### Upload a test sketch

Navigate to "Tools" -> "Board: "ATmega328" -> "Arduino AVR Boards", and select "Arduino UNO".

Navigate to "Tools" -> "Programmer", and select "Atmel STK500 development board".

Navigate to "File" -> "Examples" -> "01.Basics", and select "Blink". Go to "Sketch" and select "Upload Using Programmer". The sketch should be uploaded and the LED starts blinking every two seconds.

---
