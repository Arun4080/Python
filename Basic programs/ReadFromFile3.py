import random
def random_line(fname):
	lines=open("data/test.txt").read().split(".")
	return random.choice(lines)
print(random_line('data/test.txt')+".")
