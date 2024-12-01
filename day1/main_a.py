print(
    sum(
        map(lambda i, j: abs(i-j), *map(
            sorted, zip(*[[int(l.split('   ')[0]), int(l.split('   ')[1])] for l in open('input/input').readlines()])
        ))
    )
)
