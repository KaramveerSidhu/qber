from cubeState import getState 
import kociemba

currentState = getState()
print(currentState)
print(kociemba.solve(currentState))