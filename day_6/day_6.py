from time import perf_counter as pfc

def read_task(file):
    with open(file) as f:
        list = f.read()
    return list

def solve(task):
    speicher = []
    help = []
    for signal in task:
        speicher.append(signal)
        if signal in help:
            help = []
        else: help.append(signal)
        if len(help) == 4:
            break
    return len(speicher)-1


#solve(read_task('day_6.txt'))
start=pfc()
print(solve(read_task('day_6.txt')))
print(pfc()-start)