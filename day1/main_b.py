a, b = list(zip(*[[int(l.split('   ')[0]), int(l.split('   ')[1])] for l in open('input/input').readlines()]))

print(
    sum([b.count(i) * i for i in a])
)
