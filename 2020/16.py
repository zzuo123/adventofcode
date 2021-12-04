ranges = []
my_ticket = []
tickets = []
with open('16.txt', 'r') as file:
	line = file.readline()
	while line != '\n':
		ranges.append([int(s) for s in line[line.index(':')+2:line.index(' or ')].split('-')])
		ranges.append([int(s) for s in line[line.index(' or ')+4:-1].split('-')])
		line = file.readline()
	file.readline()
	my_ticket.extend([int(s) for s in file.readline().split(',')])
	file.readline()
	file.readline()
	line = file.readline()
	while line != '':
		tickets.append([int(s) for s in line.split(',')])
		line = file.readline()


def number_is_valid(number):
	for range in ranges:
		if number >= range[0] and number <= range[1]:
			return True
	return False


def part1():
	sum = 0
	for numbers in tickets:
		for num in numbers:
			if not number_is_valid(num):
				sum += num
	print("Part1 answer is", sum)


def validate_ticket(t):
	for number in t:
		if not number_is_valid(number):
			return False
	return True


valid_tickets = []
for ticket in tickets:
	if validate_ticket(ticket):
		valid_tickets.append(ticket)

# print(valid_tickets)


def in_range(range, number):
	return number>=range[0] and number<=range[1]


def part2():
	# valid_fields = {index of field : [valid fields]}
	valid_fields = {}
	for i in range(len(my_ticket)):
		valid_fields[i] = [j for j in range(len(my_ticket))]
	for ticket in valid_tickets:
		for field_number in range(len(ticket)):
			index = 0
			for range1, range2 in zip(ranges[0::2], ranges[1::2]):
				if (not in_range(range1, ticket[field_number]) and not in_range(range2, ticket[field_number])) and field_number in valid_fields[index]:
					valid_fields[index].remove(field_number)
				index += 1
	i = 0
	found = set()
	while i < len(valid_fields):
		if len(valid_fields[i]) == 1 and i not in found:
			found.add(i)
			for ind in range(len(valid_fields)):
				if ind != i and valid_fields[i][0] in valid_fields[ind]:
					valid_fields[ind].remove(valid_fields[i][0])
			i = 0
		i += 1
	print(valid_fields)  # it is not completely clean, but it's enough to solve the problem
	prod = 1
	for i in range(6):
		prod *= my_ticket[valid_fields[i][0]]
	print("Part2 answer is", prod)

part1()
part2()