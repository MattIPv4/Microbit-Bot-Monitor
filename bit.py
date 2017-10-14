from microbit import *

full = Image("99999:" "99999:" "99999:" "99999:" "99999")
none = Image("00000:" "00000:" "00000:" "00000:" "00000")

alertOn = False
def alert():
    alertOn = True
    outer = Image("99999:" "90009:" "90009:" "90009:" "99999")
    middle = Image("00000:" "09990:" "09090:" "09990:" "00000")
    inner = Image("00000:" "00000:" "00900:" "00000:" "00000")
    while alertOn:
        for _ in range(0, 5):
            display.show(full)
            sleep(200)
            display.show(none)
            sleep(200)
        for _ in range(0, 2):
            display.show(outer)
            sleep(200)
            display.show(middle)
            sleep(200)
            display.show(inner)
            sleep(200)
            display.show(middle)
            sleep(200)
            display.show(outer)
            sleep(200)
        for _ in range(0, 5):
            display.show(full)
            sleep(200)
            display.show(none)
            sleep(200)
        alertOn = False
        
def whirl():
    images = [
        Image(  "00000:"
                "00000:"
                "00000:"
                "00000:"
                "90000"
        ),
        Image(  "00000:"
                "00000:"
                "00000:"
                "90000:"
                "90000"
        ),
        Image(  "00000:"
                "00000:"
                "90000:"
                "90000:"
                "00000"
        ),
        Image(  "00000:"
                "90000:"
                "90000:"
                "00000:"
                "00000"
        ),
        Image(  "90000:"
                "90000:"
                "00000:"
                "00000:"
                "00000"
        ),
        Image(  "99000:"
                "00000:"
                "00000:"
                "00000:"
                "00000"
        ),
        Image(  "09900:"
                "00000:"
                "00000:"
                "00000:"
                "00000"
        ),
        Image(  "00990:"
                "00000:"
                "00000:"
                "00000:"
                "00000"
        ),
        Image(  "00099:"
                "00000:"
                "00000:"
                "00000:"
                "00000"
        ),
        Image(  "00009:"
                "00009:"
                "00000:"
                "00000:"
                "00000"
        ),
        Image(  "00000:"
                "00009:"
                "00009:"
                "00000:"
                "00000"
        ),
        Image(  "00000:"
                "00000:"
                "00009:"
                "00009:"
                "00000"
        ),
        Image(  "00000:"
                "00000:"
                "00000:"
                "00009:"
                "00009"
        ),
        Image(  "00000:"
                "00000:"
                "00000:"
                "00000:"
                "00099"
        ),
        Image(  "00000:"
                "00000:"
                "00000:"
                "00000:"
                "00990"
        ),
        Image(  "00000:"
                "00000:"
                "00000:"
                "00000:"
                "09900"
        ),
        Image(  "00000:"
                "00000:"
                "00000:"
                "09000:"
                "09000"
        ),
        Image(  "00000:"
                "00000:"
                "09000:"
                "09000:"
                "00000"
        ),
        Image(  "00000:"
                "09000:"
                "09000:"
                "00000:"
                "00000"
        ),
        Image(  "00000:"
                "09900:"
                "00000:"
                "00000:"
                "00000"
        ),
        Image(  "00000:"
                "00990:"
                "00000:"
                "00000:"
                "00000"
        ),
        Image(  "00000:"
                "00090:"
                "00090:"
                "00000:"
                "00000"
        ),
        Image(  "00000:"
                "00000:"
                "00090:"
                "00090:"
                "00000"
        ),
        Image(  "00000:"
                "00000:"
                "00000:"
                "00990:"
                "00000"
        ),
        Image(  "00000:"
                "00000:"
                "00900:"
                "00900:"
                "00000"
        ),
        Image(  "00000:"
                "00000:"
                "00900:"
                "00000:"
                "00000"
        ),
    ]
    for image in images:
        display.show(image)
        sleep(200)
        
def doReset():
    while button_a.is_pressed() and button_b.is_pressed():
        display.show(full)
    display.show(none)
    sleep(150)
    display.show(full)
    sleep(150)
    display.show(none)
    sleep(150)
    display.show(full)
    sleep(150)
    display.show(none)

while True:
    if button_a.is_pressed():
        sleep(100)
        if button_a.is_pressed() and button_b.is_pressed():
            doReset()
            continue
        if not alertOn:
            alert()
            
    if button_b.is_pressed():
        sleep(100)
        if button_a.is_pressed() and button_b.is_pressed():
            doReset()
            continue
        whirl()