from pyparsing import *

def parse(file):
  glow = open(file,"r")
  
  # Functions
  FUNC = Keyword("function")
  CREATE = Keyword("create")
  
  # Print
  PRINT = Keyword("print")
  
  # Output
  OUT = Keyword("out")
  
  LBRACE,RBRACE,LPAREN,RPAREN,SEMI,EQUAL,COL,DOT = map(Suppress,"{}();=:.")
  
  real = Regex(r"[+-]?\d+\.\d*").setParseAction(lambda t:float(t[0]))
  integer = Regex(r"[+-]?\d+").setParseAction(lambda t:int(t[0]))
  
  string = QuotedString('"')
  
  printi = Group(OUT + DOT + PRINT + COL + string("data"))

  func = Forward()
  func << Group(FUNC + COL + CREATE + LPAREN + string("function") + RPAREN + LBRACE + Group(ZeroOrMore(printi))("body") + RBRACE)
