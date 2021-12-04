with open('14.txt', 'r') as file:
	input = [line.strip() for line in file]


def part1():
	mask = ''
	memory = {}  # dict of addr:value pair
	for line in input:
		if line[:4] == 'mask':
			mask = line[7:]
		else:
			index = int(line[line.index('[')+1:line.index(']')])
			curr_num = list(bin(int(line[line.index('=')+2:]))[2:].rjust(36, '0'))
			for i in range(36):
				if mask[i] != 'X':
					curr_num[i] = mask[i]
			memory[index] = int(''.join(curr_num), 2)
	print(sum(memory.values()))
		

def part2():
	mask = ''
	memory = {}  # dict of addr:value pair
	for line in input:
		if line[:4] == 'mask':
			mask = line[7:]
		else:
			psudo_addr = list(bin(int(line[line.index('[')+1:line.index(']')]))[2:].rjust(36, '0'))
			value = int(line[line.index('=')+2:])
			for i in range(36):
				if mask[i] != '0':
					psudo_addr[i] = mask[i]
			addr_list = []
			for c in psudo_addr:
				length = len(addr_list)
				if c == 'X':
					for i in range(length):
						addr_list.append(addr_list[i]+'1')
						addr_list[i] += '0'
					if length == 0:
						addr_list.extend(['0', '1'])
				else:
					for i in range(length):
						addr_list[i] += c
					if length == 0:
						addr_list.append(c)
			addr_list = [int(''.join(curr_addr), 2) for curr_addr in addr_list]
			for addr in addr_list:
				memory[addr] = value
	print(sum(memory.values()))

part1()
part2()