# PyLexExpr - Mathematical Expression Interpreter
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust mathematical expression interpreter implemented in Python that handles arithmetic operations. Built with extensibility and educational purposes in mind.

## Overview

PyLexExpr implements a lexer and parser for mathematical expressions, demonstrating core concepts of interpreter design. It currently supports basic arithmetic operations with plans for expansion.

## Features

### Core Functionality
- Lexical analysis (tokenization)
- Expression parsing
- Basic arithmetic evaluation
- Interactive REPL interface

### Supported Operations
- Basic arithmetic: `+`, `-`, `*`, `/`
- Integer operations
- Whitespace handling
- Error reporting

## Quick Start

### Requirements
- Python 3.7+
- Git

### Installation
```bash
git clone https://github.com/SergioBonatto/PyLexExpr.git
cd PyLexExpr
```

### Usage
Launch the interactive calculator:
```bash
python pylexexpr.py
```

Example session:
```bash
calc> 5 + 3
8
calc> 10 - 4
6
calc> 3 * 7
21
calc> 15 / 3
5
```

## Architecture

### Components
- **Lexical Analyzer**: Converts input string into tokens
- **Parser**: Processes token stream and builds AST
- **Interpreter**: Evaluates the parsed expressions

### Token Types
| Type | Description |
|------|-------------|
| INTEGER | Numeric values |
| PLUS | Addition operator |
| MINUS | Subtraction operator |
| MULTIPLY | Multiplication operator |
| DIVIDE | Division operator |
| EOF | End of input marker |

## Roadmap

### Planned Features
- [x] Multi-digit number support
- [ ] Parentheses handling
- [ ] Floating-point operations
- [ ] Operator precedence (PEMDAS)
- [ ] Enhanced error handling
- [ ] Complex expression support

### Under Consideration
- Abstract Syntax Tree visualization
- Custom operator definition
- Variable support
- Function support

## Contributing

Contributions are welcome! Please check our Contributing Guidelines before submitting PRs.

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Submit a pull request

## License

Licensed under MIT - see LICENSE for details.

## Credits

- Inspired by Ruslan Spivak's interpreter series
- Contributors and maintainers
