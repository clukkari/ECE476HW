#ECE476HW3 Connor Lukkari
#GP0 = 0, GP1 = 1, GP2 = 2, GP3 = 3, GP14 = Enter, GP15 = Clear, GP13 = Buzzer,
#GP16 = YesLED, GP17 = NoLED
from machine import Pin
from time import sleep_ms

CLR = Pin(15, Pin.IN, Pin.PULL_UP)
ENT = Pin(14, Pin.IN, Pin.PULL_UP)
Num0 = Pin(0, Pin.IN, Pin.PULL_UP)
Num1 = Pin(1, Pin.IN, Pin.PULL_UP)
Num2 = Pin(2, Pin.IN, Pin.PULL_UP)
Num3 = Pin(3, Pin.IN, Pin.PULL_UP)
Buzzer = Pin(13, Pin.OUT)
YesLED = Pin(16, Pin.OUT)
NoLED = Pin(17, Pin.OUT)

#Init
YesLED.value(0)
NoLED.value(0)
Buzzer.value(0)
Guess = 0
Len = 0
Wrong = 0

CODE = 1313  
print(f"Secret Code: {CODE:04d}")

while(1):
    if CLR.value() == 0:
        Guess = 0
        Len = 0
        print("Cleared, Guess = 0")
        sleep_ms(200)

    if Len < 4:
        if Num0.value() == 0:
            Len += 1
            Guess = (Guess * 10)
            print(f"Guess: {Guess} (Length: {Len})")
            sleep_ms(200)

        if Num1.value() == 0:
            Len += 1
            Guess = (Guess * 10) + 1
            print(f"Guess: {Guess} (Length: {Len})")
            sleep_ms(200)

        if Num2.value() == 0:
            Len += 1
            Guess = (Guess * 10) + 2
            print(f"Guess: {Guess} (Length: {Len})")
            sleep_ms(200)

        if Num3.value() == 0:
            Len += 1
            Guess = (Guess * 10) + 3
            print(f"Guess: {Guess} (Length: {Len})")
            sleep_ms(200)

    if ENT.value() == 0:
        print(f"Submitted Code: {Guess}")
        
        if Guess == CODE:
            print("State: Unlocked")
            YesLED.value(1)
            sleep_ms(1000)
            YesLED.value(0)
            Wrong = 0
        else:
            Wrong += 1
            print(f"State: Locked (Incorrect Attempts: {Wrong})")
            NoLED.value(1)
            sleep_ms(1000)
            NoLED.value(0)

            if Wrong >= 3:
                print("3 Incorrect Attempts")
                Buzzer.value(1)
                sleep_ms(1000)
                Buzzer.value(0)
                Wrong = 0  
        
        #Reset after each guess
        Guess = 0
        Len = 0
        print(f"Enter Combination: (Incorrect Attempts: {Wrong})")
        sleep_ms(200)