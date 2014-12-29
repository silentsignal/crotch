import sys

# Based on: http://www.python-course.eu/finite_state_machine.php
class Crotch:
    def __init__(self,filename,lexer):
        """Initializes the Crotch class

        @param string filename  Name of the file to be parsed
        @param Lexer lexer      Pygments Lexer object with all required filters applied
        """
        self.handlers = {}
        self.startState = None
        self.tokens=lexer.get_tokens(open(filename,"r").read())
        self.currentState=None
        self.recording=False
        self.trace=[]
        self.endStates=set()

    def add_state(self, name, handler, endState=False):
        name = name.upper()
        self.handlers[name] = handler
        if endState:
            self.endStates.add(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self):
        try:
            handler = self.handlers[self.startState]
            self.currentState=self.startState
        except:
            raise InitializationError("must call .set_start() before .run()")

        oldState=None
        for ttype,tvalue in self.tokens:
            newState = handler(ttype,tvalue).upper()
            if self.currentState!=newState:
                self.recording=True
            if self.recording:
                self.trace.append(tvalue)
            if self.currentState in self.endStates:
                print ''.join(self.trace)
            if newState==self.startState:
                self.recording=False
                self.trace=[]
 
            self.currentState=newState
            handler = self.handlers[newState.upper()]

if __name__ == "__main__":
    print "This is my CROTCH"
