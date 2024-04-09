

import time
import lcddriver
display = lcddriver.lcd()



class ADO:
    def __init__(self):
        pass

    def GDisplay(self, Line1, Line2, Line3, Line4):
        display.lcd_clear()
        display.lcd_display_string(Line1, 1)
        display.lcd_display_string(Line2, 2)
        display.lcd_display_string(Line3, 3)
        display.lcd_display_string(Line4, 4)

    def GDisplay_Cnt(self, Line3):
        display.lcd_display_string(Line3, 3)
    def GDisplay_CLR(self):
        display.lcd_clear()
    def GScroll(self, text='', num_line=1, num_cols=20):
        if D_OLED == 1:
            if (len(text) > num_cols):
                display2.lcd2_display_string(text[:num_cols], num_line)
                time.sleep(1)
                for i in range(len(text) - num_cols + 1):
                    text_to_print = text[i:i + num_cols]
                    display2.lcd2_display_string(text_to_print, num_line)
                    time.sleep(0.1)
                time.sleep(1)
            else:
                display2.lcd2_display_string(text, num_line)
        else:
            if (len(text) > num_cols):
                display.lcd_display_string(text[:num_cols], num_line)
                time.sleep(1)
                for i in range(len(text) - num_cols + 1):
                    text_to_print = text[i:i + num_cols]
                    display.lcd_display_string(text_to_print, num_line)
                    time.sleep(0.2)
                time.sleep(1)
            else:
                display.lcd_display_string(text, num_line)


ado = ADO()

