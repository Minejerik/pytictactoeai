from os import system, name
from random import randint
xvar = 'X'
yvar = 'O'
pos = {}
pos[1] = '1'
pos[2] = '2'
pos[3] = '3'
pos[4] = '4'
pos[5] = '5'
pos[6] = '6'
pos[7] = '7'
pos[8] = '8'
pos[9] = '9'
dle = 'X'
ai = True
times = 0
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def findnext(input):
	if input == 1:
		return [2,4,5]
	elif input == 2:
		return [1,5,3]
	elif input == 3:
		return [2,5,6]
	elif input == 4:
		return [1,5,7]
	elif input == 5:
		return [2,4,6,8]
	elif input == 6:
		return [3,5,9]
	elif input == 7:
		return [4,5,8]
	elif input == 8:
		return [5,7,9]
	elif input == 9:
		return [5,6,8]

def runai():
	tempa = []
	otherplayer = 'X'
	xpos = []
	aipos = []
	empty = []
	for i in range(1,9):
		if pos[int(i)] == otherplayer:
			xpos.append(i)
		elif pos[int(i)] == 'O':
			aipos.append(i)
		else:
			empty.append(i)
		
		return randint(1,9)

def check():
	if pos[1] == 'X' and pos[2] == "X" and pos[3] == 'X':
		return 'xwin'
	elif pos[4] == 'X' and pos[5] == 'X' and pos[6] == 'X':
		return 'xwin'
	elif pos[7] == 'X' and pos[8] == 'X' and pos[9] == 'X':
		return 'xwin'
	elif pos[1] == 'X' and pos[4] == 'X' and pos[7] == 'X':
		return 'xwin'
	elif pos[2] == 'X' and pos[5] == 'X' and pos[8] == 'X':
		return 'xwin'
	elif pos[3] == 'X' and pos[6] == 'X' and pos[9] == 'X':
		return 'xwin'
	elif pos[1] == 'X' and pos[5] == 'X' and pos[9] == 'X':
		return 'xwin'
	elif pos[7] == 'X' and pos[5] == 'X' and pos[3] == 'X':
		return 'xwin'
	elif pos[1] == 'O' and pos[2] == "O" and pos[3] == 'O':
		return 'ywin'
	elif pos[4] == 'O' and pos[5] == 'O' and pos[6] == 'O':
		return 'ywin'
	elif pos[7] == 'O' and pos[8] == 'O' and pos[9] == 'O':
		return 'ywin'
	elif pos[1] == 'O' and pos[4] == 'O' and pos[7] == 'O':
		return 'ywin'
	elif pos[2] == 'O' and pos[5] == 'O' and pos[8] == 'O':
		return 'ywin'
	elif pos[3] == 'O' and pos[6] == 'O' and pos[9] == 'O':
		return 'ywin'
	elif pos[1] == 'O' and pos[5] == 'O' and pos[9] == 'O':
		return 'ywin'
	elif pos[7] == 'O' and pos[5] == 'O' and pos[3] == 'O':
		return 'ywin'
	else:
		return True



def draw():
	clear()
	print(pos[1] + "  |  " + pos[2] + '  |  ' + pos[3])
	print("--------------")
	print(pos[4] + "  |  " + pos[5] + '  |  ' + pos[6])
	print("--------------")
	print(pos[7] + "  |  " + pos[8] + '  |  ' + pos[9])

def main():
	global dle
	draw()
	if dle == 'X':
		temp = input('X pos?:  ')
		if int(temp) > 9:
			main()
		if pos[int(temp)] != 'O' and pos[int(temp)] != 'X':
			pos[int(temp)] = xvar
			dle = 'O'
		else:
			main()
	elif dle == 'O':
		if ai != True:
			temp = input('O pos?:  ')
		else:
			temp = runai()
		if int(temp) > 9:
			main()
		if pos[int(temp)] != 'X' and pos[int(temp)] != 'O':
			pos[int(temp)] = yvar
			dle = 'X'
		else:
			main()


def loop():
	global times
	times = times +1
	main()
	temp = check()
	if temp == True:
		loop()
	else:
		if temp == 'xwin':
			draw()
			print('X wins')
		elif temp == 'ywin':
			draw()
			print('O wins')
		else:
			print(temp)

loop()