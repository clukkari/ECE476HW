#ECE476 HW2 Connor Lukkari
#1
from random import randint
d12 = randint(1,12)
d8 = randint(1,8)
W = T = L = 0
for i in range(0,10000):
    A = B = 0
    for j in range(0,3):
        A += randint(1,12)
    for j in range(0,4):
        B += randint(1,8)
    if(A>B):
        W += 1
    elif(A == B):
        T += 1
        W += 1
    else:
        L += 1
print("#1","W =", W, "T =", T, "L =", L)

#2
W2 = T2 = L2 = 0
for match in range(0,10000):
    W0 = T0 = L0 = 0
    for i in range(0,5):
        A = B = 0
        for j in range(0,3):
            A += randint(1,12)
        for j in range(0,4):
            B += randint(1,8)
        if(A>B):
            W0 += 1
        elif(A == B):
            T0 += 1
        else:
            L0 += 1
    if(W0 > L0):
        W2 += 1
    elif(W0 == L0):
        T2 += 1
    else:
        L2 += 1
print("#2","W =", W2, "T =", T2, "L =", L2)

#3
W3 = T3 = L3 = 0
for match in range(0,10000):
    W0 = T0 = L0 = 0
    while(abs(W0-L0) < 2 or (W0 < 5 and L0 < 5)):
        A = B = 0
        for j in range(0,3):
            A += randint(1,12)
        for j in range(0,4):
            B += randint(1,8)
        if(A>B):
            W0 += 1
        elif(A == B):
            T0 += 1
        else:
            L0 += 1
    if(W0 > L0):
        W3 += 1
    elif(W0 == L0):
        T3 += 1
    else:
        L3 += 1
print("#3","W =", W3, "T =", T3, "L =", L3)
#4
def Series(R1, R2):
    R3 = R1 + R2
    return(R3)
def Para(R1, R2):
    R3 = (R1 * R2) / (R1 + R2)
    return(R3)

Rq = Para(250, 300)
Rw = Series(50, Rq)
Re = Para(Rw, 150)
Rr = Series(200, 150)
Rt = Para(Rr, 75)
Ry = Series(Rt, Re)
Rab = Para(350, Ry)
print("#4 Rab =", Rab)

#5
Zq = Para(250, -300j)
Zw = Series(Zq, 30j)
Ze = Para(Zw, 150j)
Zr = Series(200j, 150)
Zt = Para(Zr, 75)
Zy = Series(Zt, Ze)
Zab = Para(350, Zy)
print("#5 Zab =", Zab)

#6
from machine import Pin
from time import sleep

LED1 = Pin(16, Pin.OUT)
LED2 = Pin(17, Pin.OUT)
LEDE = Pin(18, Pin.OUT)

while(1):
    LED1.value(1)
    sleep(1)
    LED1.value(0)
    LED2.value(1)
    sleep(1)
    LED2.value(0)
    LEDE.value(1)
    sleep(1)
    LEDE.value(0)
    
#7
from machine import Pin
from time import sleep

IN1 = Pin(17, Pin.OUT)
IN2 = Pin(16, Pin.OUT)

while(1):
    IN1.value(1)
    IN2.value(0)
    sleep(1)
    IN1.value(1)
    IN2.value(1)
    sleep(1)
    IN1.value(0)
    IN2.value(1)
    sleep(1)
    IN1.value(0)
    IN2.value(0)
    sleep(1)


