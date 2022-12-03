from time import perf_counter as pfc

def read_task(file):
    with open(file) as f:
        list = []
        for elve in f.read().split("\n\n"):
            calories = 0
            for cal in elve.split("\n"):
                calories += int(cal)
            list.append(calories)
    return list

def solve(task):
    most = 0
    for cal in task:
        if cal > most:
            most = cal
    return most
start=pfc()
print(solve(read_task('day_1.txt')))
print(pfc()-start)