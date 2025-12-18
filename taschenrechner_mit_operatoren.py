### einfacher Taschenrechner mit Operatoren + - / *

## Eingabe der Zahlen

zahl1 = input ("gib eine Zahl ein ")
zahl2 = input ("gib eine zweite zahl ein ")

## Umwandlung der Eingaben in Zahlen

try:
    zahl1 = float (zahl1)

except ValueError:
        print ("das ist keine gültige Zahl")
        exit ()

try:
    zahl2 = float (zahl2)
    
except ValueError:
    print ("das ist keine gültige Zahl")
    exit ()

## Eingabe des Operators

operator = input ("wähle +, -, /, :, * ")

## Berechnung je nach Operator

if operator == "+":
    ergebnis = zahl1 + zahl2

elif operator == "-":
    ergebnis = zahl1 - zahl2

elif operator == "/" or operator == ":":
    ergebnis = zahl1 / zahl2

elif operator == "*":
    ergebnis = zahl1 * zahl2

## bei ungültigem Operator 'else/sonst' ausführen

else:
    ergebnis = "das ist kein gültiger Operator"

## Ausgabe des Ergebnisses

print ("Ergebnis ist ", ergebnis)



# ich habe elif gewählt (else if *sonst wenn*) weil mehrere Bedingunggne möglich sind
# if *wenn der operator + ist, sonst wenn der Operator - ist*
# else würde bedeuten *in allen anderen Fällen, egal was eingegeben wurde*
# if: prüfe erste Möglichkeit
# elif: prüfe nächste Möglichkeit
# elif: prüfe nächste Möglichkeit
# else: alles andere

    
