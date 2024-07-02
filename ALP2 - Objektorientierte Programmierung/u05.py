"""Übungszettel 5.
Abgabe von Ulyana Kharabrova(Tut. bei Robin Niclas Hoffmann) und Simeon Vasilev(Tut. bei Maximillian Glinka)


Aufgabe 1

{P} ≡ {P'} ≡ {P''}
Zuweisungsaxiome
{P''} -> {R1} 
{R1} -> {R2}
{R2} -> {R3} 
{R3} ≡ {R3'}
{R3'} -> {Q}

Sequenzregel
{P} -> {Q}

{P} ≡ { a>0 ∧ b>0 ∧ c<0 }
{P'} ≡ { a>0 ∧ b>0 ∧ c<0 ∧ True }
{P''} ≡ { a>0 ∧ b>0 ∧ c<0 ∧ a+b-2c-d=a+b-2c-d }
    a = a+b-c
{R1} ≡ { a>0 ∧ b>0 ∧ c<0 ∧ a-d-c=a-d-c }
    d = b
{R2} ≡ { a>0 ∧ b>0 ∧ c<0 ∧ a-b-c=a-d-c }
    b = a-b-c
{R3} ≡ { a>0 ∧ b>0 ∧ c<0 ∧ b=a-d-c }
{R3'} ≡ { a>0 ∧ b>0 ∧ -c>0 ∧ b=a-d-c }
    c = -c
{Q} ≡ { a>0 ∧ b>0 ∧ c>0 ∧ b=a-d+c }

Aufgabe 2

{P} ≡ {x ≥ 0 ∧ (x * y + z) == c}
if x%2==0:
    y = y + y
    x = x//2
else:
    z = z + y
    x = x - 1
{Q} ≡ {x ≥ 0 ∧ (x * y + z) == c}       (1)

Beweis:

{x ≥ 0 ∧ (x * y + z) == c} = Q[x ≥ 0 ∧ (x * y + z) == c]

nach Bedingungsregel:

P∧B = {x ≥ 0 ∧ (x * y + z) == c} Bedingung==True
y = y + y
x = x//2
{x ≥ 0 ∧ (x * y + z) == c}

P!=B = {x > 0 ∧ (x *  y + z) == c} Bedingung==False
z = z + y
x = x - 1
{x ≥ 0 ∧ (x * y + z) == c}

Aus dem Zuweisungsaxiom:
{x ≥ 0 ∧ (x//2 * y + y + z)==c }    y = y + y    {x ≥ 0 ∧ (x * y + z) == c}
                                    x = x//2
{x ≥ 0 ∧ (2xy//2+z) == c}                        {x ≥ 0 ∧ (x * y + z) == c}
{x ≥ 0 ∧ (xy+z) == c}                            {x ≥ 0 ∧ (x * y + z) == c}


wegen der zweiten Konsequenz-Regel die Gültigkeit von True Bedingung bewiesen.

{x ≥ 0 ∧ ((x-1)*y+z+y)==c }         z = z + y    {x ≥ 0 ∧ (x * y + z) == c}
                                    x = x - 1
{x ≥ 0 ∧ (xy-y+z+y) == c}                        {x ≥ 0 ∧ (x * y + z) == c}
{x ≥ 0 ∧ (xy+z) == c}                            {x ≥ 0 ∧ (x * y + z) == c}

wegen der zweiten Konsequenz-Regel die Gültigkeit von True Bedingung bewiesen.

P == Q
Zum Schluss, aus der zwei bewiesenen Gültigkeiten Bedingungen, folgt dann die Gültigkeit von (1)(formel ist gültig)


Aufgabe 3

{P ≡ b > 0 ∧ a > 0}
 counter = 1
 power = b
{INV ≡ (b > 0) ∧ (power == b **counter) ∧ (a ≥ counter ≥ 0)}
 while counter<a:
    power = power * b
    counter = counter + 1
{Q ≡ power == b **a}

Beweis:

{INV ∧ B} = {INV}

{(b > 0) ∧ (power == b **counter) ∧ (a ≥ counter ≥ 0) ∧ counter<a}

    power = power * b            P1
    counter = counter + 1        P2

nach P1 und P2:

{(b > 0) ∧ (power*b == b **counter+1) ∧ (a > counter+1 ≥ 0)} INV

{(b > 0) ∧ (power*b == b **counter+1) ∧ (a ≥ counter+1 ≥ 0)} not INV

Mit der Zuweisungsaxiom erhalten wir:

{P ≡ b > 0 ∧ a > 0}
 counter = 1
 power = b
{INV ≡ (b > 0) ∧ (b == b **1) ∧ (a > 1 ≥ 0)}


nach der Sequenz und while Regel:
while counter<a:
    power = power * b
    counter = counter + 1

(b > 0) ∧ (b == b ** 2) ∧ (a > 2 > 0) daraus folgt:

-> Q = b == b ** 2 ->> b > 0 und a > 0

P = b > 0, a > 0
P ∧ B && P = Q

Die Formel gilt

Aufgabe 4

{P} ≡ {Zahl ≥ 0}
hilf = Zahl
bits = 1
while hilf>1:
   hilf = hilf//2
   bits = bits+1
{Q} ≡ {bits == BinaryDigits(Zahl)}

a) Dafür müssen wir alle Variante nach Zuweisungs und Sequnzregeln prüfen.
  1) hilf ≥ 0 ∧ (BinaryDigits(hilf) + bits == BinaryDigits(Zahl) + 1)
     hilf//2 ≥ 0 ∧ (BinaryDigits(hilf//2) + bits +1 == BinaryDigits(hilf) + bits)
     hilf//2 ≥ 0 ∧ (BinaryDigits(hilf//2) + bits +1 == BinaryDigits(hilf//2) + bits +1)      True

  2) hilf ≥ 0 ∧ (BinaryDigits(hilf) + 1 == BinaryDigits(Zahl) + bits)
     hilf//2 ≥ 0 ∧ (BinaryDigits(hilf//2) + 1 == BinaryDigits(hilf) + bits)
     hilf//2 ≥ 0 ∧ (BinaryDigits(hilf//2) + 1 != BinaryDigits(hilf//2) + bits)                False

  3) hilf ≥ 0 ∧ (BinaryDigits(hilf) + bits == BinaryDigits(Zahl) + bits)
     hilf//2 ≥ 0 ∧ (BinaryDigits(hilf//2) + bits +1  == BinaryDigits(hilf) + bits)
     hilf//2 ≥ 0 ∧ (BinaryDigits(hilf//2) + bits +1  == BinaryDigits(hilf//2) + bits)          False


b) hier müssen wir INV beweisen:

Beweis:

{INV ≡ hilf ≥ 0 ∧ (BinaryDigits(hilf) + bits == BinaryDigits(Zahl) + 1)}

while hilf>1:
   hilf = hilf//2
   bits = bits+1

{INV ∧ (hilf ≤ 1)}


nach while-Regel:

{INV ∧ (hilf > 1)}
   hilf = hilf//2
   bits = bits+1
{INV}

nach Konsequenz- II, while Regel und Zuweisungsaxiom :

{hilf > 1 ∧ (BinaryDigits(hilf) + bits == BinaryDigits(Zahl) + 1)}
{hilf > 1 ∧ (BinaryDigits(hilf / /2) + 1+ bits == BinaryDigits(Zahl) + 1)}
{hilf ≥ 0 ∧ (BinaryDigits(hilf / /2) + bits == BinaryDigits(Zahl))}
{hilf ≥ 0 ∧ (BinaryDigits(hilf) + bits == BinaryDigits(Zahl))}
{hilf ≥ 0 ∧ (BinaryDigits(hilf) + bits == BinaryDigits(Zahl) + 1)}


{INV ≡ hilf ≥ 0 ∧ (BinaryDigits(hilf) + bits == BinaryDigits(Zahl) + 1)}
Invariante Eigenschaft ist bewiesen

Aufgabe 5
"""

def invariantA(seq):
    assert (seq == seq)

def invariantB(seq, i):
    for j in range(0, i - 1):
        assert (seq[j + 1] >= seq[j])


def insertsort(seq):
    # Insertsort aus Übung 3
    k = 1
    i = 0
    #Invariante, was nur Elemente aus einer Liste "seq" enthält
    invariantA(seq)
    while i < len(seq):
        j = i
        key = seq[j]
    # zweite Invariante, wo alle Elemente von seq[0] bis seq[i - 1] sortiert sind
        invariantB(seq, i)
        while j >= k and seq[j - k] > key:
            seq[j] = seq[j - k]
            j = j - k
        seq[j] = key
        i = i + 1
    return seq

print(insertsort([3,2,5,2,6,1,6,5,42,5,1,9]))

"""
Aufgabe 6
Die wichtigste Invariante der Schleife innerhalb partition-Funktion ist die for-schleife
A[k] ≤ A[r] für k = l, . . . , i und A[k] > A[r] für k = i + 1, . . . , j. (∗∗)

def partition( A, low, high ):
 pivot = A[low]
 i = low
 for j in range(low+1,high+1):
 if ( A[j] < pivot ):
 i=i+1
 A[i], A[j] = A[j], A[i]
 A[i], A[low] = A[low], A[i]
 return i
 
Nach Ende der for-Schleife low+1 <= j < high+1 ist, garantiert die Vertauschung von A[i + 1] und A[high] 
die Korrektheit von Partition
 
Beweisen könnten wir es, wenn wir die for schleife mit z.B while-Schleife ersetzen würden.

"""