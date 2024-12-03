print(
    len(
        list(
            filter(
                lambda l: all(0 > x > -4 for x in l) or all(0 < x < 4 for x in l), [
                    [i-j for i, j in zip(
                        [int(c) for c in line.split(' ')][1:],
                        [int(c) for c in line.split(' ')][:-1]
                    )] for line in open('input/input').readlines() if line.strip()
                ]
            )
        )
    )
)
