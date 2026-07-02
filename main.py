from json_parser.lexer import Lexer

text = '{"name": "Saif"}'

lexer = Lexer(text)
tokens = lexer.tokenize()

for i in tokens:
    print(i)