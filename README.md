Code Review On The Cheap
========================

This is a simple example of using [Pygments](http://pygments.org) along with a simple state machine to facilitate code review. The basic idea is to use the lexers of Pygments to tokenize source code and then build partial "parsers" which recognize desirable code patterns.

The `crotch` module is mostly just a general purpose state machine modified to handle basic file operations and `(type,value)` tuples returned by Pygments lexers. To use this class you implement handlers (representing states), which are basically callable functions which expect two arguments (token type, token value) and return the name of the next state (handler) to traverse to. You add these handlers to the state machine with the `add_state()` method, and also specify the start state and every "end state", which should result in a traceback report. 

Examples are provided along with the core module.

