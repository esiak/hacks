import sys
import re

def swap(array, red, j):
	tmp = array[red]
	if not tmp == 'RED':
		print 'Illegal move'
		return
	array[red] = array[j]
	array[j] = tmp

def move_forward(array, position):
	if(array[position] == 'RED'):
		print 'Illegal move'
		return
	if re.match("[A-Za-z]", array[position]):
		swap(array, position + 1, position)
	elif re.match("[0-9]?", array[position]):
		swap(array, position - 1, position)

def jump_over(array, position):
	if(array[position] == 'RED'):
		print 'Illegal move'
		return
	if re.match("[A-Za-z]", array[position]):
		swap(array, position + 2, position)
	elif re.match("[0-9]?", array[position]):
		swap(array, position - 2, position)

def init_array(size):
	array = [None]*(2*size + 1)
	for i in range(0,size):
		array[i] = chr(65 + i)
	array[size] = 'RED'
	for i in range(0, size):
		array[i + size + 1] = str(i + 1)
	return array

if __name__ == '__main__':
	size = int(sys.argv[1])
	print 'Size of team:%d'%size
	jam = init_array(size)
	print 'Initial position:'
	print jam
	for i in range(1 , size + 1):
		index =  size + i if i %2 == 0 else size - i
		move_forward(jam, index)
		for j in range(0, i ):
			step =  -2 if index %2 == 0 else 2
			jump_index = index + (j+1)*step
			jump_over(jam, jump_index)
	for i in reversed(range(0 , size )):
		index =  size + i if i %2 == 0 else size - i
		move_forward(jam, index)
		for j in range(0, i ):
			step =  -2 if index %2 == 0 else 2
			jump_index = index + (j+1)*step
			jump_over(jam, jump_index)
	print jam







