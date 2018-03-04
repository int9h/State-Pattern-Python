from Elevator import State

class Close(State):
    def close(self):
        return Close()
    
    def move(self):
        return Move()
    
    def open(self):
        return Open()

class Move(State):

    def move(self):
        return Move()

    def stop(self):
        return Stop()

class Open(State):    
    
    def open(self): 
        return Open()
    
    def close(self):
        return Close()

class Stop(State):

    def stop(self):
        return Stop()

    def open(self):
        return Open()

    def move(self):
        return Move()
