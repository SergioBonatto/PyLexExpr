# Simple Mathematical Expression Interpreter (WIP)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A basic mathematical expression interpreter built in Python that can handle simple arithmetic operations. This is part of an ongoing project to create a more comprehensive interpreter.

## Current Features

- Tokenization of mathematical expressions
- Support for basic arithmetic operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- Single-digit integer processing
- Whitespace handling
- Interactive calculator mode

## Getting Started

### Prerequisites

- Python 3.7 or higher

### Installation

```bash
git clone git@github.com:SergioBonatto/PyLexExpr.git
cd PyLexExpr
```

### Running the Calculator

```bash
python pylexexpr.py
```

## Usage Example

```bash
calc> 5+3
8
calc> 7-2
5
calc> 4*6
24
calc> 8/2
4
```

## Project Structure

```
.
├── calculator_handle.py    # Main interpreter implementation
└── README.md              # Documentation
```

## Implementation Details

The interpreter consists of two main components:

- **Lexical Analyzer (Tokenizer)**: Breaks input into tokens
- **Parser**: Processes tokens and evaluates expressions

### Supported Token Types

- `INTEGER`: Numeric values
- `PLUS`: Addition operator
- `MINUS`: Subtraction operator
- `MULTIPLY`: Multiplication operator
- `DIVIDE`: Division operator
- `EOF`: End of input marker

## Limitations and TODOs

- [ ] Multi-digit number support
- [ ] Parentheses support
- [ ] Floating-point number support
- [ ] Order of operations (PEMDAS)
- [ ] Error handling improvements
- [ ] Support for more complex expressions

## Contributing

This is a development project. Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by Ruslan Spivak's "Let's Build A Simple Interpreter" series
- Built as a learning project for understanding interpreter design
