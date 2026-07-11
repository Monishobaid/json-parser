from json_parser.lexer import Lexer
from json_parser.tokens import TokenType



class Parser:

    def __init__(self,tokens):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[self.position]

    def increment(self):
        self.position += 1
        self.current_token = self.tokens[self.position]

    
    def parse(self):
        value = self.parse_value()

        if self.current_token.value != TokenType.EOF:
            raise Exception(f"unexpected token: {value}")

        return value

    
    def parse_value(self):
        token = self.current_token

        if token.type == TokenType.STRING:
            self.increment()
            return token.value

        elif token.type == TokenType.NUMBER:
            self.increment()
            return token.value

        elif token.type == TokenType.TRUE:
            self.increment()
            return token.value

        elif token.type == TokenType.FALSE:
            self.increment()
            return token.value

        elif token.type == TokenType.NULL:
            self.increment()
            return token.value

        raise Exception(f"Unexpected Token: {token}")


def parse(text):

    lexer = Lexer(text)
    tokens = lexer.tokenize()
    parser = Parser(tokens)

    return parser.parse_value()

