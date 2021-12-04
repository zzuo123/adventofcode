import time


def play_game(input, turns):
	# spoken = {number: turn(index+1)}
	spoken = {number: index+1 for index, number in enumerate(input[:-1])}
	turn = len(input)+1
	last_spoke = input[len(input)-1]

	while turn <= turns:
		if last_spoke in spoken:
			speaking = (turn-1) - spoken[last_spoke]
		else:
			speaking = 0
		spoken[last_spoke] = turn-1  # record last spoken number
		last_spoke = speaking
		turn += 1
	
	print(f'Final answer: turn: {turns}, speaking: {last_spoke}')


if __name__ == '__main__':
	# sample (0.000 s)
	start_time = time.time()
	play_game([0,3,6], 10)
	print(f"--- example completed in {time.time() - start_time} seconds ---")

	# part 1 (0.001 s)
	start_time = time.time()
	play_game([1,0,18,10,19,6], 2020)
	print(f"--- part 1 completed in {time.time() - start_time} seconds ---")

	# part 2 (14.133 s with python3, 4.232 s with pypy3)
	start_time = time.time()
	play_game([1,0,18,10,19,6], 30000000)
	print(f"--- part 2 completed in {time.time() - start_time} seconds ---")