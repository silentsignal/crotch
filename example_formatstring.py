from pygments.lexers import CLexer
from pygments.token import *
from crotch import Crotch
import sys

def start(ttype,tvalue):
    if ttype is Token.Name and tvalue=="printf":
        return "printf_nopunct"
    return "start"

def printf_nopunct(ttype,tvalue):
    if ttype is Token.Punctuation and tvalue=="(":
        return "in_printf"
    return "printf_nopunct"

def in_printf(ttype,tvalue):
    if ttype is Token.String:
        return "start"
    if ttype is Token.Name:
        return "end"
    return "in_printf"

def end(ttype,tvalue):
    return "start"

lexer=CLexer()
# Add your lexer filters here...

c=Crotch(sys.argv[1],lexer)
c.add_state("start",start)
c.set_start("start")
c.add_state("printf_nopunct",printf_nopunct)
c.add_state("in_printf",in_printf)
c.add_state("end",end,True)
c.run()
