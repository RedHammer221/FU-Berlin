'''Übungszettel Nr. 2
Abgabe von Simeon Vasilev(Tut. bei Maximillian Glinka) und Ulyana Kharabrova(Tut. bei Robin Niclas Hofmann)'''

#Aufgabe 1

def mersenne(n):        # die Formel aus der Aufgabe
    return (2**n) - 1

def isPrime(zahl):      #überprüft, ob die gegebene Zahl ein Primzahl ist
    if zahl == 1:
        return False

    for fact in range(2, zahl):
        if zahl % fact == 0:
            return False

    return True

def getPrimes(n_start, n_end): #hier bekommen wir eine Liste mit Primzahlen
    primeList = []
    for zahl in range(n_start, n_end+1):
        if isPrime(zahl):
            primeList.append(zahl)
    return primeList

def returnMersenne():   #das ist eigentlich die Funktion, worum es in der Aufgabe geht, zumindest denken wir so
    mersenneList = []
    primesList = getPrimes(4, 20) # das hier dient als unser "input"
    for zahl in primesList:
        mersenneList.append(mersenne(zahl))
    return mersenneList

print(returnMersenne())

def returnMersenne_test():
    print (returnMersenne(10))

#Aufgabe 2a

#Variant1

import random

def random(n, m):
    m = (m or random.randint(2, n)) - 1 #here we define the number of repeats
    a = random.sample(range(1, n), m) + [0, n]
    list.sort(a)
    return [a[i+1] - a[i] for i in range(len(a) - 1)]

print(random(20, 5))
print(random(129, 25))

#Variant 2

from random import randint

def repeat(x, y):

    rand_dict = {}
    iteration = 0
    while True:
        iteration += 1
        gen_int = randint(x, y)

        if len(rand_dict) == 0:
            rand_dict[iteration] = gen_int
        else:
            for x in range(len(rand_dict)):
                if gen_int == rand_dict[x + 1]:
                    output_tuple = ([rand_dict[x + 1] for x in range(len(rand_dict))], iteration)
                    return output_tuple
                else:
                    rand_dict[iteration] = gen_int  # same as above

print(repeat(10,100))

def random_test():
    print(random(10, 30))

#Aufgabe 4

def apply_if(f, p, xs):
    #Wir haben einfach das Haskell-Beispiel aus dem Blatt ins Python "übersetzt"
    null = []
    for x in xs:
        if p(x):
            null.append(f(x))
        else:
            null.append(x)
    return null

def factorial(n):
    # Funktion aus der VL
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def odd(n):
    #aus VL
    return n % 2 == 1

print(apply_if(factorial, odd, [2, 5, 7, 4, 9, 6]))

def apply_if_test ():
    print(apply_if(factorial, odd, [4, 7, 5, 10, 3, 6]))
    


#Aufgabe 5

#ab
import turtle
import random as ra


window = turtle.Screen() # öffnet ein neues Fenster
turtle.bgcolor ("white") # background color
turtle.speed(0) # the speed with which stars are drawn

""" diese Funktion zeichnet unser Stern (ich weiß nicht, warum es mit Positionseingabe nicht
funktioniert, aber in der Theorie brauchen wir das nicht"""
def paint_star(size):
    angle = 120
    r,g,b = ra.random(), ra.random(), ra.random()
    turtle.fillcolor(r,g,b)
    turtle.begin_fill()

    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()
    return

""" Diese Funktion zeichnet Sterne an zufälligen Stellen am Bildschirm
(nicht genau, was die Aufgabe will, aber das ist was ich geschafft habe, vllt Teilpunkte? :3)
Wenn ich das als funktion "sky" zu definieren probiere, Python meckert irgendwarum"""

num_stars = 0
while num_stars < 20:  # anstatt input
    x = ra.randint (-300, 300) 
    y = ra.randint (-300, 300)
    paint_star(ra.randint(10,50))
    turtle.penup()
    turtle.goto(x,y) 
    turtle.pendown()
    num_stars = num_stars + 1

window.exitonclick() # closes the window when clicked

#c

import turtle 
import random

def drawCentSq(t, center,side): # Hilfsfunktion für den zentralen Quadrat
    ## calculate top left corner
    xPt=center[0]-side/2
    yPt=center[1]+side/2
    t.up()
    t.goto(xPt, yPt)
    t.down()
    for i in range(4):
        t.forward(side)
        t.right(90)

def squares(t, center, side):
    if side<1:
        return # das dient in dem Fall anstatt von else

    drawCentSq(t,center,side)
    squares(t,center,side-10)
    

mad=turtle.Turtle() 
wn=mad.getscreen() 
squares(mad,[0,0],180)


#Aufgabe 6

def revDigits(n):
#mit Rekursion
    if len(n) == 0:
        return n
    else:
        return revDigits(n[1:]) + n[0]

first_number = "15"
second_number = "136997"
third_number = "67568261"

print(revDigits(first_number))
print(revDigits(second_number))
print(revDigits(third_number))

def revDigits2 (n):
#ohne Rekursion
    print(n[::-1])

first_number = "7"
second_number = "8345298"
third_number = "2465874534523"

revDigits2(first_number)
revDigits2(second_number)
revDigits2(third_number)

def revDigits_test():
    print(revDigits(first_number))


#Aufgabe 7

#Die Python Version von den foldr und foldl aus der Haskell
def foldr(f,i,seq):
    if not seq:
        return i
    else:
        return f(seq[0], foldr(f, i, seq[1:]))


def foldl(f,i,seq):
    if not seq:
        return i
    else:
        return foldl(f, f(i, seq[0]), seq[1:])
