import string
import sys
from time import perf_counter as pfc

def read_task(file):
    with open(file) as f:
        listeg = []
        group= []
        count = 0
        for row in f:
            if count < 3:
                count += 1
                group.append(row.strip("\n"))
                if count == 3:
                    listeg.append(group)
                    group = []
                    count = 0

        return listeg
def solve(task):
    punkte = 0
    werte = list(string.ascii_letters[:52])
    for liste in task:
        for i in liste[0]:
            if i in liste[1] and i in liste[2]:
                punkte += werte.index(i)+1
                break
    return punkte

start=pfc()
print(solve(read_task("day_3.txt")))
print(pfc()-start)
