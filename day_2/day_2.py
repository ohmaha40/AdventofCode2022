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
        if play[1] == "X" and play[0] == "C":
            punkte += stein + sieg
        elif play[1] == "Z" and play[0] == "B":
            punkte += schere + sieg
        elif play[1] == "Y" and play[0] == "A":
            punkte += papier + sieg
        elif play[0] == "A" and play[1] == "Z":
            punkte += schere
        elif play[0] == "C" and play[1] == "Y":
            punkte += papier
        elif play[0] == "B" and play[1] == "X":
            punkte += stein
        else:
            if play[1] == "X": punkte += unentschieden + stein
            elif play[1] == "Y": punkte += unentschieden + papier
            elif play[1] == "Z": punkte += unentschieden + schere

        gesamtpunkte += punkte
    print(gesamtpunkte)
    #return gesamtpunkte

start=pfc()
solve(read_task('day_2.txt'))
print(pfc()-start)