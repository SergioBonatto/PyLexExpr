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
        self.current_char = self.text[0] if text else None

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

    def expr(self):
        """
            expr -> INTEGER OP INTEGER
        """
        # set current token to the first token taken fron the input
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)
        
        op = self.current_token
        if op.type == PLUS:
            self.eat(PLUS)
        elif op.type == MINUS:
            self.eat(MINUS)
        elif op.type == MULTIPLY:
            self.eat(MULTIPLY)
        else:
            self.eat(DIVIDE)

        right = self.current_token
        self.eat(INTEGER)

        if op.type == PLUS:
            result = left.value + right.value
        elif op.type == MINUS:
            result = left.value - right.value
        elif op.type == MULTIPLY:
            result = left.value * right.value
        elif op.type == DIVIDE:
            result = left.value / right.value
        else:
            return print("erro")
        return result

def main():
    while True:
        try:
            text = input("calc> ")
            if not text:
                continue
            interpreter = Interpreter(text)
            result = interpreter.expr()
            print(result)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
