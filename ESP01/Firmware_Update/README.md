# ESP01 Wi-Fi Module

## Firmware Update Procedure

WHILE THE "ESP8266 DOWNLOAD TOOL" IS USED, THE PIN MUST BE CONNECTED TO GND

**before uploading the new firmware (between the steps) power off and power on the ESP01 board.**

[FT232RL USB TO TTL 3.3V/5V FTDI Serial Adapter Module](https://components101.com/modules/ft232rl-usb-to-ttl-converter-pinout-features-datasheet-working-application-alternative)

Max Current Draw for 3.3V: 50mA. Not enough to power the ESP01 board.

```
16:35:13.452 -> AT+GMR
16:35:13.452 -> AT version:1.7.4.0(May 11 2020 19:13:04)
16:35:13.452 -> SDK version:3.0.4(9532ceb)
16:35:13.452 -> compile time:May 27 2020 10:12:17
16:35:13.452 -> Bin version(Wroom 02):1.7.4
16:35:13.452 -> OK
```




```
16:35:51.031 -> AT+RST
16:35:51.031 -> 
16:35:51.031 -> OK
16:35:51.108 -> 
16:35:51.108 ->  ets Jan  8 2013,rst cause:2, boot mode:(3,0)
16:35:51.108 -> 
16:35:51.141 -> load 0x40100000, len 2592, room 16 
16:35:51.141 -> tail 0
16:35:51.141 -> chksum 0xf3
16:35:51.141 -> load 0x3ffe8000, len 764, room 8 
16:35:51.141 -> tail 4
16:35:51.141 -> chksum 0x92
16:35:51.141 -> load 0x3ffe82fc, len 676, room 4 
16:35:51.141 -> tail 0
16:35:51.141 -> chksum 0x22
16:35:51.141 -> csum 0x22
16:35:51.141 -> 
16:35:51.141 -> 2nd boot version : 1.7(5d6f877)
16:35:51.141 -> SPI Speed : 40MHz
16:35:51.141 -> SPI Mode : QIO
16:35:51.141 -> SPI Flash Size & Map: 8Mbit(512KB+512KB)
16:35:51.141 -> jump to run user1 @ 1000
16:35:51.141 -> 
16:35:51.178 -> correct flash map
16:35:51.178 -> �bl`r�olph����n�s��o|��l�pslb��|s�l�n��n�l`��r�l�l�l`��r�l�l�l`��r�l���ll`sl��rl���b�b�c�c|���bc��o�on�ll������l�������l�o����clll��c���cl�bslrl
16:35:51.244 -> ready
```
