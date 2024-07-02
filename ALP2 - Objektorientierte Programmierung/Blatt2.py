import math
from random import randint

def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)

def odd(n):
    if n%2:
        return True
    else:
        return False

#Aufgabe 1
def pythTripelSmaller(n):
    Tripel=[]
    #wie lassen b bis n-1 durchlaufen
    for b in range(1, n-1):
        #und lassen dabei a nur bis b laufen, um Dopplungen zu vermeiden
        for a in range(1, b):
            #rootsqsum ist das c
            rootsqsum = math.sqrt((a**2 + b**2))
            #können uns den rechenaufwand der 2. for-Schleife spare, wenn wir mal bei nem a ankommen, das mit b berechnet schon größer als n ist
            if rootsqsum > n:
                break
            #wenn es eine ganze zahl ist, dann wird dieser Fall übersprungen und der else Fall trifft zu
            elif (rootsqsum % 1):
                pass
            #a,b,c sind ganze Zahlen, erfüllen die gleichung, werden als Tripel gespeichert
            else:
                Tripel.append((a,b, int(rootsqsum)))
    return Tripel

#Aufgabe 2
def apply_until(f,p, xs):
    #liste der Elemente auf die Funktion f angewand wurde wird vorher initialisiert
    applied=[]
    for x in xs:
        #schleife packt umgewandelte elemente aus der liste in die ergebnisliste
        if p(x):
            applied.append([f(x)])
        #erfüllt ein element zum ersten mal nicht die Bedingung p, wird der aktuelle Stand ausgegeben und die funktion stoppt
        else:
            return applied

#Aufgabe 3a
ergebnis=[]
def filter_rec(p,liste):
    #Anker der rekursiven Schleife, trifft in der letzten Verschachtelung zu
    if liste==[]:
        return ergebnis
    else:
        pass
    #passendes Element wird der Ergebnisliste hinzugefügt
    if p(liste[0]):
        ergebnis.append(liste[0])
    else:
        pass
    #erstes Element der eingegebenen Liste wird gelöscht
    del liste[0]
    #Funktion wird erneut aufgerufen, aber jetzt mit einem Element weniger in der Liste
    filter_rec(p,liste)
    #Ergebnis wird eine Verschachtelung weiter hoch gegeben, bzw am Ende normal ausgegeben
    return ergebnis

#Aufgabe 3b
def filter_iter(p,liste):
    ergebnis=[]
    #einfache for scheife über alle elemente unserer Liste
    for x in liste:
        #elemente kommen in die Ergebnisliste, wenn sie die Bedingung erfüllen
        if p(x):
            ergebnis.append(x)
        #sonst passiert nix
        else:
            pass
    #am Ende wird die Ergebnisliste ausgegeben
    return ergebnis

#Aufgabe 4
def repeat(a=1, b=1000000):
    #vorinitialisierung von Variablen
    zahlendict={}
    i=1
    #Endlosschleife, bis der return erreicht wird
    while 42:
        #zufällige Zahl wird produziert
        z= randint(a,b)
        #check ob wir diese Zahl schon mal produziert haben
        if z in zahlendict:
            #wenn ja, haben wir eine dopplung, und wir geben unsere gespeicherten Zahlen und ihre Anzahl i-1 aus
            return ((zahlendict, i-1))
        #ansonsten wird die Zahl nur eingespeichert in die Liste aller Zahlen, die wir schon produziert haben
        else:
            zahlendict.update({i : z})
        #Zähler für Anzahl der Zufallszahlen wird erhöht
        i+=1

#Aufgabe 5a)
#Fast der gleiche Code wie bei 4
def double_birthday():
    zahlendict={}
    i=1
    #Endlosschleife bis return erreicht wird
    while 42:
        #zufällige Geburtstage werden erstellt, gibt ja 366 verschiedene
        z= randint(1,366)
        if z in zahlendict:
            return i
        else:
            zahlendict.update({i : z})
        i+=1

#Aufgabe 5b)
def repeat_double_birthday():
    samples=[]
    i=0
    #wir erstellen eine Liste mit 10000 Einträgen, wobei jeder Eintrag schaut, wieviele zufällige Geburtstage wir betrachten müssen, bis eine Dopplung vorkommt
    for i in range(10000):
        samples.append(double_birthday())
    #dann wird die liste ausgegeben
    return samples

#Aufgabe 5c)
def birthday_paradox(n):
    #wir erstellen eine Liste wie in 5b beschrieben
    samples= repeat_double_birthday()
    #Zähler für Stichproben, wo wir bei weniger als n Personen (zufälligen Geburtstagsausgaben) bereits eine Dopplung haben
    passend = 0
    #Wir zählen wieviele der Stichproben weniger als n Leute gebraucht haben, um einen doppelten Geburtstag zu erzeugen
    for x in samples:
        if x<= n:
            passend+=1
        else:
            pass
    #Prozentualer Anteil wird ausgerechnet und ausgegeben
    prozente= passend/10000
    return prozente

print(pythTripelSmaller(15))
print(apply_until(factorial, odd, [3,5,7,3,4,5,7,6,8]))
print(filter_rec(odd, [1,2,3,4,5,6,7,8,9,10]))
print(filter_iter(odd, [1,2,3,4,5,10,11,12,13,14]))
print(repeat(1,1000000))
print(double_birthday())
print(repeat_double_birthday())
print(birthday_paradox(23))
