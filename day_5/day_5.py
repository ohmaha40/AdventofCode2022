from time import perf_counter as pfc
tanker = [["D","M","S","Z","R","F","W","N",],
          ["W","P","Q","G","S",],
          ["W","R","V","Q","F","N","J","C",],
          ["F","Z","P","C","G","D","L",],
          ["T","P","S",],
          ["H","D","F","W","R","L",],
          ["Z","N","D","C",],
          ["W","N","R","F","V","S","J","Q",],
          ["R","M","S","G","Z","W","V",]]
def read_task(file):
    with open(file) as f:
        list = []
        for row in f.readlines(): list.append(row.strip().split(" "))
    return list

def solve(task):
    for schritt in task:
        for i in range(int(schritt[1])):
            tanker[(int(schritt[5])-1)].append(tanker[(int(schritt[3])-1)].pop())
    ergebnis = ""
    for i in range(len(tanker)):
        ergebnis += tanker[i][len(tanker[i])-1]
    return ergebnis
start=pfc()
print(solve(read_task('day_5.txt')))
print(pfc()-start)