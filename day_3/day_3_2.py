import string
import sys
from time import perf_counter as pfc

def read_task(file):
    with open(file) as f:
        listeg = []
        for row in f:
            liste = []
            liste.append(row[:-(int(len(row)/2+1))])
            liste.append(row[(int(len(row)/2)):].strip("\n"))
            listeg.append(liste)
        return listeg
def solve(task):
    punkte = 0
    werte = list(string.ascii_letters[:52])
    for liste in task:
        for i in liste[0]:
            if i in liste[1]:
                punkte += werte.index(i) +1
                break
    return punkte

start=pfc()
print(solve(read_task('day_3.txt')))
print(pfc()-start)

#werte = list(string.ascii_letters[:52])
#werte.append(list(string.ascii_uppercase[:25]))
#print(werte[51])
#print(werte[int(len(werte)/2)])
#print(werte.index("A"))
#read_task("day_3.txt")