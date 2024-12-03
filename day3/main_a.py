import re

print(
    sum(
        map(
            lambda instr: int(instr[4:-1].split(',')[0]) * int(instr[4:-1].split(',')[1]),
            re.findall(r'mul\(\d+,\d+\)', open('input/input').read())
        )
    )
)


