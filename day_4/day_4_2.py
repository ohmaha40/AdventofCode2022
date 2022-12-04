from time import perf_counter as pfc

def read_task(file):
    with open(file) as f:
        liste = []
        for ids in f.readlines():
            elve1 = ids.strip().split(',')[0].split('-')
            elve2 = ids.strip().split(',')[1].split('-')
            liste.append([elve1, elve2])
        return liste

def solve(task):
    a = 0
    for group in task:
        if (int(group[1][0]) <= int(group[0][0]) and int(group[1][1]) >= int(group[0][0])) \
        or (int(group[0][0]) <= int(group[1][0]) and int(group[0][1]) >= int(group[1][0]))\
        or (int(group[1][1]) <= int(group[0][1]) and int(group[1][1]) >= int(group[0][1]))\
        or (int(group[0][1]) <= int(group[1][1]) and int(group[0][1]) >= int(group[1][1])):
            a += 1
    return a

start=pfc()
print(solve(read_task('day_4.txt')))
print(pfc()-start)