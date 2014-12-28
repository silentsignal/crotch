from pygments.token import *
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

    def add_state(self, name, handler):
        name = name.upper()
        self.handlers[name] = handler

    def set_start(self, name):
        self.startState = name.upper()

    def run(self):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("must call .set_start() before .run()")
    
        for ttype,tvalue in self.tokens:
            newState = handler(ttype,tvalue)
            handler = self.handlers[newState.upper()]

if __name__ == "__main__":
    print "This is CROTCH"
