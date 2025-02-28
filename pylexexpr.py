# Token types
#
# EOF (end-of-file) token is used to indicate that 
# there is no more input left for lexical analysis
#
INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, EOF = "INTEGER", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "EOF"

class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, "MINUS" or EOF
        self.type = type
        # token value: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+', '-' '*', '/' or None
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

    def error(self):
        raise Exception("Error parsing input")

    def skipWhiteSpace(self):
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

    def get_next_token(self):
        """
            Lexical analyzer (also know as scanner or tokenizer)

            This method is responsible for breaking a sentense 
            apart into tokens. One token at a time
        """
        text = self.text

        self.skipWhiteSpace()

        # is self.pos index past the end of the self.text? 
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # get a character at a position self.pos and decide
        # what token to create base on the single character
        current_char = text[self.pos]

        # if the character is a digit then convert it to
        # integer, create INTEGER token, increment self.pos
        # index to pont to next character after the digit,
        # and return the INTEGER token
        
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token
        
        if current_char == "+":
            token = Token(PLUS, current_char)
            self.pos +=1
            return token

        if current_char == "-":
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        if current_char == "*":
            token = Token(MULTIPLY, current_char)
            self.pos += 1
            return token

        if current_char == "/":
            token = Token(DIVIDE, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token 
        # and assign the nect token to the self.current_token,
        # otherwise raise an exception.

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

        # we expect the current token to be a single-digit integer (TODO: FIXME:)
        left = self.current_token
        self.eat(INTEGER)

        # we expect the current token to be a `+` token
        if self.current_token.type == PLUS:
            op = self.current_token
            self.eat(PLUS)
        elif self.current_token.type == MINUS:
            op = self.current_token
            self.eat(MINUS)
        elif self.current_token.type == MULTIPLY:
            op = self.current_token
            self.eat(MULTIPLY)
        else:
            op = self.current_token
            self.eat(DIVIDE)

        # we expect the current token to be a single-digit integer
        right = self.current_token
        self.eat(INTEGER)

        # after the above call the self.current_token is set to 
        # EOF token

        # at this point INTEGER PLUS INTEGER sequence of tokens 
        # has been successfully found and the method can just
        # return the result off adding two integers, thus
        # effectively interpreting client input
        if op.value == "+":
            result = left.value + right.value
        elif op.value == "-":
            result = left.value - right.value
        elif op.value == "*":
            result = left.value * right.value
        else:
            result = left.value / right.value
        return result

def main():
    while True:
        try: 
            text = input("calc> ")
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == "__main__":
    main()







