from json_parser.tokens import Token,TokenType

#dataclass import is not used here like it is used in tokens because like lexer we are storing information
#but also it has operations to do
class Lexer:
    def __init__(self,text):
        self.text = text
        self.position = 0

    def read_string(self):
        self.position += 1

        result = ""

        while self.position < len(self.text) and self.text[self.position] != '"':
            result += self.text[self.position]
            self.position += 1
        
        if self.position >= len(self.text):
            raise Exception("undetermined String")
        
        return result

    def read_word(self):
        result = ""
        # why we are using self.position < len(self.text) ? it's more like a safety check
        while self.position < len(self.text) and self.text[self.position].isalpha():
            result += self.text[self.position]
            self.position += 1
            
        # "suppose at the end of the we get at "true" at the end of the "true" we have "," which is not isalpha
        self.position -= 1
        return result

    def read_number(self):
        result = ""
        while self.position < len(self.text) and self.text[self.position].isdigit():
            result += self.text[self.position]
            self.position += 1
        
        self.position -= 1
        return int(result)
        

    
    def tokenize(self):
        tokens = []

        while self.position < len(self.text):

            current_char = self.text[self.position]

            if current_char == "{":
                tokens.append(Token(TokenType.LEFT_BRACE,current_char))
            elif current_char == "}":
                tokens.append(Token(TokenType.RIGHT_BRACE, current_char))
            elif current_char == "[":
                tokens.append(Token(TokenType.LEFT_BRACKET,current_char))
            elif current_char == "]":
                tokens.append(Token(TokenType.RIGHT_BRACKET, current_char))
            elif current_char == ":":
                tokens.append(Token(TokenType.COLON, current_char))
            elif current_char == ",":
                tokens.append(Token(TokenType.COMMA, current_char))
            elif current_char == '"':
                string_value = self.read_string()
                tokens.append(Token(TokenType.STRING, string_value))
            elif current_char.isalpha():
                word = self.read_word()

                if word == "true":
                    tokens.append(Token(TokenType.TRUE, True))
                elif word == "false":
                    tokens.append(Token(TokenType.FALSE, False))
                elif word == "null":
                    tokens.append(Token(TokenType.NULL, None))
                else:
                    raise Exception(f"unknown char:  {word}")
            
            elif current_char.isdigit():
                number = self.read_number()
                tokens.append(Token(TokenType.NUMBER, number))

            elif current_char in " \n\t\r":
                pass
            else:
                raise Exception(f"unknown char : {current_char}")
            
            self.position += 1
        
        tokens.append(Token(TokenType.EOF, None))

        return tokens
