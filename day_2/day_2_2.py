from time import perf_counter as pfc

def read_task(file):
    with open(file) as f:
        list = []
        for row in f.read().lstrip().split("\n"):
            play = []
            for i in row.split():
                play.append(i)
            list.append(play)
    return list

def solve(task):
    gesamtpunkte = 0
    stein = 1
    papier = 2
    schere = 3
    sieg = 6
    unentschieden = 3
    for play in task:
        punkte = 0
        ergebnis = play[1]
        if ergebnis == "Z":
            if play[0] == "A": punkte += papier + sieg
            elif play[0] == "B": punkte += schere + sieg
            elif play[0] == "C": punkte += stein + sieg
        if ergebnis == "X":
            if play[0] == "A": punkte += schere
            elif play[0] == "B": punkte += stein
            elif play[0] == "C": punkte += papier
        if ergebnis == "Y":
            if play[0] == "A": punkte += stein + unentschieden
            elif play[0] == "B": punkte += papier + unentschieden
            elif play[0] == "C": punkte += schere + unentschieden
        gesamtpunkte += punkte
    return gesamtpunkte

start=pfc()
print(solve(read_task('day_2.txt')))
print(pfc()-start)