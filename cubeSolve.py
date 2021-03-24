from cubeState import state 
import kociemba

state = state.replace(' ','').replace('y','U').replace('w','D').replace('r','F').replace('o','B').replace('g','R').replace('b','L')
print(state)
print(kociemba.solve(state))