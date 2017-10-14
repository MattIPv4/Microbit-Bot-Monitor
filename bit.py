from microbit import *

alertOn = False
def alert():
    alertOn = True
    full = Image("99999:" "99999:" "99999:" "99999:" "99999")
    none = Image("00000:" "00000:" "00000:" "00000:" "00000")
    while alertOn:
        display.show(full)
        sleep(0.1)
        display.show(none)
        sleep(0.1)

alert()