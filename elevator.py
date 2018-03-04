import sys, os    

path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(path+"/elevator")
sys.path.append(path)

import Elevator, States

elevator = Elevator.Elevator(States.Open())
elevator.close()
elevator.move()
elevator.stop()
elevator.open()

try:
    elevator.move()
except Elevator.IllegalStateTransition as err:
    print("can't change to state "+str(err)+" from state", elevator.get_state())

elevator.close()
elevator.move()
