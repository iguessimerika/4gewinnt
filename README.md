Testfälle:

- Vertikal gewonnen?
    - Testfall-ID: VG-001
    - Testbeschreibung: Überprüfen, ob das System einen vertikalen Gewinn korrekt erkennt und anzeigt

    - Vorbedingungen:
        - Das Spiel ist gestartet
        - Zwei Spieler nehmen an dem Spiel teil
        - In Spalte 2 befinden sich bereits drei Spielsteine von Spieler 1 übereinander

    - Schritte:
        - Spieler 1 wirft einen weiteren Spielstein in Spalte 2

    - Erwartetes Ergebnis:
        - Das System erkennt vier senkrecht übereinanderliegende Spielsteine von Spieler 1
        - Das Spiel wird beendet
        - Es erscheint die Meldung: „Spieler 1 hat gewonnen!“

- Horizontal gewonnen?
    - Testfall-ID: VG-002
    - Testbeschreibung: Überprüfen, ob das System einen horizontalen Gewinn korrekt erkennt und anzeigt

    - Vorbedingungen:
        - Das Spiel ist gestartet
        - Zwei Spieler nehmen an dem Spiel teil
        - Spieler 1 hat bereits drei Spielsteine nebeneinander in der untersten Zeile (Spalten 1, 2 und 3)

    Schritte:
        - Spieler 1 wirft einen Spielstein in Spalte 4

    - Erwartetes Ergebnis:
        - Das System erkennt vier waagerecht angeordnete Spielsteine von Spieler 1
        - Das Spiel wird beendet
        - Es erscheint die Meldung: „Spieler 1 hat gewonnen!“

- Diagonal gewonnen?
    - Testfall-ID: VG-003
    - Testbeschreibung: Überprüfen, ob das System einen diagonalen Gewinn korrekt erkennt und anzeigt

    - Vorbedingungen:
        - Das Spiel ist gestartet
        - Zwei Spieler nehmen an dem Spiel teil
        - Spieler 1 hat bereits drei Spielsteine diagonal (von links unten nach rechts oben):
            -> Spalte 1, Zeile 1
            -> Spalte 2, Zeile 2
            -> Spalte 3, Zeile 3
        - Die darunterliegenden Felder sind besetzt, dass der Spielstein korrekt platziert werden kann

    Schritte:
        - Spieler 1 wirft einen Spielstein in Spalte 4

    - Erwartetes Ergebnis:
        - Das System erkennt vier diagonal angeordnete Spielsteine von Spieler 1
        - Das Spiel wird beendet
        - Es erscheint die Meldung: „Spieler 1 hat gewonnen!“
        
- Unentschieden?
    - Testfall-ID: VG-004
    - Testbeschreibung: Überprüfen, ob das System ein Unentschieden korrekt erkennt und anzeigt, wenn das Spielfeld vollständig gefüllt ist und kein Spieler gewonnen hat

    - Vorbedingungen:
        - Das Spiel ist gestartet
        - Zwei Spieler nehmen an dem Spiel teil
        - Das gesamte Spielfeld ist mit Spielsteinen gefüllt
        - Es liegen keine vier Spielsteine eines Spielers in einer Reihe (horizontal, vertikal oder diagonal)

    Schritte:
        - Der letzte mögliche Spielstein wird gesetzt

    - Erwartetes Ergebnis:
        - Das System erkennt, dass keine weiteren Züge möglich sind
        - Das Spiel wird beendet
        - Es erscheint die Meldung: „Spieler 1 hat gewonnen!“