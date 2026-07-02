from json_parser.lexer import Lexer

text = '{"active": true, "delete": false,"data":null}'

lexer = Lexer(text)
tokens = lexer.tokenize()

for i in tokens:
    print(i)