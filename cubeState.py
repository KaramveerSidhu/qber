 #Cube Notation 
 #             |*U1**U2**U3*|
 #             |************|
 #             |*U4**U5**U6*|
 #             |************|
 #             |*U7**U8**U9*|
 #             |************|
 # ************|************|************|************
 # *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*
 # ************|************|************|************
 # *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*
 # ************|************|************|************
 # *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*
 # ************|************|************|************
 #             |************|
 #             |*D1**D2**D3*|
 #             |************|
 #             |*D4**D5**D6*|
 #             |************|
 #             |*D7**D8**D9*|
 #             |************|

#Order of Entering Faces (A fully solved cube) --> UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB

def getState():
	print('Enter the state of the Cube\nEnter r for Red, o for Orange, b for Blue and so on...')
	
	upper = input('Enter Upper Face ')
	right = input('Enter Right Face ')
	front = input('Enter Front Face ')
	down = input('Enter Downward Face ')
	left = input('Enter Left Face ')
	back = input('Enter Back Face ')

	state = upper+right+front+down+left+back
	state = state.replace(' ','').replace('y','U').replace('w','D').replace('r','F').replace('o','B').replace('g','R').replace('b','L')

	return state

