# ============================================================
# TASCHENRECHNER – Kommentiert
# ============================================================


while True:  #while = solange True = immer wahr: absichtliche Endlosschleife, 
            #läuft bis break kommt

    eingabe1 = input("Gib die erste Zahl ein: ")  #input() stoppt das Programm, wartet auf Eingabe, Ergebnis
							                        #ist IMMER Text (String)

    try:  #try = versuche den folgenden Code auszuführen

        zahl1 = float(eingabe1)  # float(eingabe1) wandelt Text in Zahl um
                                # "3.5" in 3.5  "abc" → ValueError

        break  #break beendet die Endlosschleife SOFORT  wenn eine gültige Zahl
                #eingegeben wurde

    except ValueError:  #except fängt den Fehler ab, 
                        #der bei ungültiger Zahl entsteht (z. B. Buchstaben)

        print("Das war keine gültige Zahl. Bitte erneut eingeben.")  
        #Fehlermeldung, danach beginnt while True wieder von vorne


while True:  #zweite Endlosschleife für die zweite Zahl (gleiches Prinzip wie oben)

    eingabe2 = input("Gib die zweite Zahl ein: ")  
    #wieder: Programm wartet, Ergebnis ist Text

    try:  #erneuter Versuch der Umwandlung

        zahl2 = float(eingabe2)  #Text ist Zahl, nur wenn das klappt, geht es weiter

        break  #schleife verlassen, weil jetzt eine gültige zweite Zahl existiert

    except ValueError:  #Fehler wenn: keine Zahl eingegeben

        print("Das war keine gültige Zahl. Bitte erneut eingeben.")  
        #Meldung:neue Eingabe


ergebnis = zahl1 + zahl2  
#Addition zweier floats → mathematische Operation ist möglich


print("Ergebnis:", ergebnis)  #Ausgabe des Ergebnisses im Terminal

