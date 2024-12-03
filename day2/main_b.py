print(
    len(
        list(
            filter(
                lambda l: all(0 > x > -4 for x in l) or
                          all(0 < x < 4 for x in l) or
                          len(list(filter(lambda x: 0 > x > -4, l))) == len(l) - 1 and ([i for i, v in enumerate(l) if v >= 0 or v <= -4][0] == 0 or [i for i, v in enumerate(l) if v >= 0 or v <= -4][0] == len(l) - 1) or
                          len(list(filter(lambda x: 0 < x < 4, l))) == len(l) - 1 and ([i for i, v in enumerate(l) if v <= 0 or v >= 4][0] == 0 or [i for i, v in enumerate(l) if v <= 0 or v >= 4][0] == len(l) - 1) or
                          len(list(filter(lambda x: 0 > x > -4, l))) == len(l) - 1 and len(list(filter(lambda v: v==0, l))) == 1 or
                          len(list(filter(lambda x: 0 < x < 4, l))) == len(l) - 1 and len(list(filter(lambda v: v==0, l))) == 1 or
                          len(list(filter(lambda x: 0 > x > -4, l))) >= len(l) - 2 and not ([i for i, v in enumerate(l) if v >= 0 or v <= -4][0] == 0 or [i for i, v in enumerate(l) if v >= 0 or v <= -4][-1] == len(l) - 1) and not len(list(filter(lambda v: v==0, l))) == 1 and (0 > l[[i for i, v in enumerate(l) if v >= 0 or v <= -4][0]] + l[[i for i, v in enumerate(l) if v >= 0 or v <= -4][0] + 1] > -4) or
                          len(list(filter(lambda x: 0 < x < 4, l))) >= len(l) - 2 and not ([i for i, v in enumerate(l) if v <= 0 or v >= 4][0] == 0 or [i for i, v in enumerate(l) if v <= 0 or v >= 4][-1] == len(l) - 1) and not len(list(filter(lambda v: v==0, l))) == 1 and (0 < l[[i for i, v in enumerate(l) if v <= 0 or v >= 4][0]] + l[[i for i, v in enumerate(l) if v <= 0 or v >= 4][0] + 1] < 4)
                , [
                    [i - j for i, j in zip(
                        [int(c) for c in line.split(' ')][1:],
                        [int(c) for c in line.split(' ')][:-1]
                    )] for line in open('input/input').readlines() if line.strip()
                ]
            )
        )
    )
)