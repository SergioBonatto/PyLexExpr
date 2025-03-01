# Token types
#
# EOF (end-of-file) token is used to indicate that
INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, EOF = "INTEGER", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "EOF"

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """
            String representation of the class instance

            Example:
                Token(INTEGER, 3)
                Token(PLUS, +)
        """
        return "Token({type}, {value})".format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g "3+5"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None
        self.current_char = self.text[self.pos] 

    #### Lexer Code
    def error(self):
        current_pos = self.pos
        raise Exception(f"Error: Invalid character '{self.text[current_pos]}' at position {current_pos + 1}")

    def skipWhiteSpace(self):
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.advance()

    def advance(self):
        """
            advance the 'pos' pointer and the 'current_char' variable
        """
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def integer(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """
            Lexical analyzer (also know as scanner or tokenizer)

            This method is responsible for breaking a sentense
            apart into tokens. One token at a time
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skipWhiteSpace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char in "+-*/":
                if self.current_char == "+":
                    token = Token(PLUS, self.current_char)
                elif self.current_char == "-":
                    token = Token(MINUS, self.current_char)
                elif self.current_char == "*":
                    token = Token(MULTIPLY, self.current_char)
                else:  # self.current_char == "/"
                    token = Token(DIVIDE, self.current_char)
                self.advance()
                return token
            self.error()
        return Token(EOF, None)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def term(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        """
            expr -> INTEGER OP INTEGER
        """
        # set current token to the first token taken fron the input
        self.current_token = self.get_next_token()

        result = self.term()

        while self.current_token.type in (PLUS, MINUS, MULTIPLY, DIVIDE):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()
            elif token.type == MULTIPLY:
                self.eat(MULTIPLY)
                result = result * self.term()
            else:
                self.eat(DIVIDE)
                result = result / self.term()

        return result

def main():
    while True:
        try:
            text = input(">>>> ")
            if text.lower() in ['exit', 'quit']:
                print(" Goodbye!")
                break
            if not text:
                continue
            interpreter = Interpreter(text)
            result = interpreter.expr()
            print(result)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
