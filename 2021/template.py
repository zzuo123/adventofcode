# reading from input from text file
def read_file():
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file]
    return lines


