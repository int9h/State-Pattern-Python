class IllegalStateTransition(Exception):    
    pass

class StateInterface:    
    def open():    
        pass    
    
    def close():    
        pass    
    
    def move():    
        pass    
    
    def stop():    
        pass

class State(StateInterface):    
    
    def open(self):    
        raise IllegalStateTransition("Open")    
    
    def close(self):    
        raise IllegalStateTransition("Close")    
    
    def move(self):    
        raise IllegalStateTransition("Move")
    
    def stop(self):    
        raise IllegalStateTransition("Stop")

    def __str__(self):
        return self.__class__.__name__

class Elevator:

    def set_state(self, new_state):
        if isinstance(new_state, StateInterface):
            self.state = new_state
            print("state:", self.get_state()) 
        else:
            raise ValueError

    def get_state(self):
        return self.state

    def stop(self):
        self.set_state(self.state.stop())

    def move(self):
        self.set_state(self.state.move())

    def open(self):
        self.set_state(self.state.open())

    def close(self):
        self.set_state(self.state.close())

    def __init__(self, initial_state):
        self.state = initial_state
