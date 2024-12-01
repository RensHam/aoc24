print(
    sum([abs(i-j) for i, j in zip(
        *list(map(sorted, list(zip(*[[int(l.split('   ')[0]), int(l.split('   ')[1])] for l in open('input/input').readlines()])))))
         ])
)
