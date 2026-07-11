# from json_parser.lexer import Lexer

# text = '{"active": true, "delete": false,"data":null, "number": 21}'

# lexer = Lexer(text)
# tokens = lexer.tokenize()

# for i in tokens:
#     print(i)


from json_parser.parser import parse

result = parse('"Saif hello hi"')
result1 = parse("21")
result2 = parse("false hello")



print(result)
print(result1)
print(result2)
