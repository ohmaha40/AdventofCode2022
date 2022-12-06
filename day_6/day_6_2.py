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
            a = 0
            helpa = []
            for i in help:
                if a == 1:
                    helpa.append(i)
                if i == signal:
                    a= 1
            help = helpa
            help.append(signal)
        else: help.append(signal)
        if len(help) == 14:
            break
    return len(speicher)
start=pfc()
print(solve(read_task('day_6.txt')))
print(pfc()-start)