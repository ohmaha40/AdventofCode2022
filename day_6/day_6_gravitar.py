from time import perf_counter as pfc

def read_task(file):
    with open(file) as f:
        return f.read()

def solve(task, l):
   for i in range(len(task)-l):
       if len(set(task[i:i+l])) == l:
           return i+l

#solve(read_task('day_6.txt'))
start=pfc()
print(solve(read_task('day_6.txt'), 4))
print(solve(read_task('day_6.txt'), 14))
print(pfc()-start)