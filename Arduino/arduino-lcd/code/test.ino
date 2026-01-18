#include <Wire.h>
#include <hd44780.h>
#include <hd44780ioClass/hd44780_I2Cexp.h>

hd44780_I2Cexp lcd; // declare lcd object: auto locate & auto config expander chip
const int LCD_COLS = 16;
const int LCD_ROWS = 2;

void setup() {
  // put your setup code here, to run once:
  lcd.begin(LCD_COLS, LCD_ROWS);
  lcd.clear();
  lcd.setBacklight(HIGH);
  //Initial Display
  lcd.setCursor(0, 0);
  lcd.print("Hello, World!");
  delay(3000); 
}

void loop() {
  // put your main code here, to run repeatedly:
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("hd44780 Library");
  lcd.setCursor(0, 1);
  lcd.print("...working here");
  delay(3000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Columns: ");
  lcd.print(LCD_COLS);
  lcd.setCursor(0, 1);
  lcd.print("Rows: ");
  lcd.print(LCD_ROWS);
  delay(3000);
}
