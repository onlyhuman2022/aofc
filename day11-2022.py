import re
from math import floor


class Monkey:
    def __init__(self):
        self.starting_items = []
        self.operator = ''
        self.the_num = ''
        self.test = ''
        self.true_monkey = ''
        self.false_monkey = ''
        self.num_of_times = 0


with open('input.txt') as f:
    notes = [note.strip() for note in f.readlines()]

monkeys = [Monkey() for i in range(8)]

actual_monkey = 0

for i in notes:
    if 'Monkey' in i:
        actual_monkey = int(i[7])
    if 'Starting' in i:
        monkeys[actual_monkey].starting_items.extend([int(x) for x in re.split(': |, ', i)[1:]])
    if 'Operation' in i:
        monkeys[actual_monkey].operator = re.split('Operation: new = old ', i)[1][0]
        monkeys[actual_monkey].the_num = re.split('Operation: new = old ', i)[1][2:]
    if 'Test' in i:
        monkeys[actual_monkey].test = re.split('Test: divisible by ', i)[1]
    if 'true' in i:
        monkeys[actual_monkey].true_monkey = re.split('If true: throw to monkey ', i)[1]
    if 'false' in i:
        monkeys[actual_monkey].false_monkey = re.split('If false: throw to monkey ', i)[1]

for i in range(20):
    # round number i
    for j in range(8):
        # monkey number j
        while monkeys[j].starting_items:
            monkeys[j].num_of_times += 1
            if monkeys[j].operator == '*':
                if monkeys[j].the_num.isnumeric():
                    monkeys[j].starting_items[0] *= int(monkeys[j].the_num)
                else:
                    monkeys[j].starting_items[0] *= monkeys[j].starting_items[0]
            else:
                monkeys[j].starting_items[0] += int(monkeys[j].the_num)

            monkeys[j].starting_items[0] = floor(monkeys[j].starting_items[0] / 3)

            if monkeys[j].starting_items[0] % int(monkeys[j].test) == '0':
                monkeys[int(monkeys[j].true_monkey)].starting_items.append(monkeys[j].starting_items[0])
            else:
                monkeys[int(monkeys[j].false_monkey)].starting_items.append(monkeys[j].starting_items[0])

            monkeys[j].starting_items.pop(0)

maxs = [0, 0]

for i in monkeys:
    if i.num_of_times > maxs[0] or i.num_of_times > maxs[1]:
        if maxs[0] <= maxs[1]:
            maxs[0] = i.num_of_times
        else:
            maxs[1] = i.num_of_times

monkey_business = maxs[0]*maxs[1]

print(monkey_business)
