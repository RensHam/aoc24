import re
from functools import reduce

print(
    reduce(lambda state, instr: {
        'add': instr.startswith('do(') and not instr.startswith('don') or (state['add'] and instr.startswith('mul')),
        'sum': state['sum'] + int(instr[4:-1].split(',')[0]) * int(instr[4:-1].split(',')[1]) if state['add'] and instr.startswith('mul') else state['sum']
    },
        re.findall(r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)', open('input/input').read()),
        {'add': True, 'sum': 0}
    )['sum']
)


