"""
Expression Parser for HIT137 Assignment Q2

This program reads mathematical expressions from 'Q2/sample_input.txt',
tokenizes them, parses them using recursive descent with plain functions,
builds an expression tree, evaluates the expressions, and outputs the results
to 'Q2/output.txt' in the specified format.

Features:
- Supports numbers, operators (+ - * /), parentheses, and unary minus.
- Operator precedence: parentheses > * / > + -
- Handles errors: invalid characters, division by zero, parsing errors, unary +.
- Outputs tree in prefix notation, tokens list, and evaluation result.
- No classes used, plain functions for parsing.
"""

import sys
import os

def tokenize(expr):
    """
    Tokenizes the input expression string into a list of tokens.

    Tokens include:
    - NUM: integer numbers
    - OP: operators (+, -, *, /)
    - LPAREN: left parenthesis '('
    - RPAREN: right parenthesis ')'
    - END: end of expression marker

    Ignores whitespace. Raises ValueError for invalid characters.

    Args:
        expr (str): The expression string to tokenize.

    Returns:
        list: List of token dictionaries, each with 'type' and 'value'.

    Raises:
        ValueError: If an invalid character is encountered.
    """
    tokens = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c.isspace():
            i += 1
            continue
        elif c.isdigit():
            # Parse multi-digit number
            num = ''
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append({'type': 'NUM', 'value': num})
        elif c in '+-*/':
            tokens.append({'type': 'OP', 'value': c})
            i += 1
        elif c == '(':
            tokens.append({'type': 'LPAREN', 'value': c})
            i += 1
        elif c == ')':
            tokens.append({'type': 'RPAREN', 'value': c})
            i += 1
        else:
            raise ValueError(f"Invalid character '{c}' in expression")
    # Add end marker
    tokens.append({'type': 'END', 'value': 'END'})
    return tokens

def current(tokens, pos):
    """
    Returns the current token at position pos.

    Args:
        tokens (list): List of tokens.
        pos (list): Mutable position [index].

    Returns:
        dict or None: Current token or None if at end.
    """
    return tokens[pos[0]] if pos[0] < len(tokens) else None

def consume(pos):
    """
    Advances the position by one.

    Args:
        pos (list): Mutable position [index].
    """
    pos[0] += 1

def parse_expression(tokens, pos):
    """
    Parses an expression: term ((+|-) term)*

    Args:
        tokens (list): List of tokens.
        pos (list): Mutable position.

    Returns:
        dict: AST node for the expression.
    """
    left = parse_term(tokens, pos)
    while current(tokens, pos) and current(tokens, pos)['type'] == 'OP' and current(tokens, pos)['value'] in '+-':
        op = current(tokens, pos)['value']
        consume(pos)
        right = parse_term(tokens, pos)
        left = {'op': op, 'left': left, 'right': right}
    return left

def parse_term(tokens, pos):
    """
    Parses a term: factor ((*|/) factor)*

    Args:
        tokens (list): List of tokens.
        pos (list): Mutable position.

    Returns:
        dict: AST node for the term.
    """
    left = parse_factor(tokens, pos)
    while current(tokens, pos) and current(tokens, pos)['type'] == 'OP' and current(tokens, pos)['value'] in '*/':
        op = current(tokens, pos)['value']
        consume(pos)
        right = parse_factor(tokens, pos)
        left = {'op': op, 'left': left, 'right': right}
    return left

def parse_factor(tokens, pos):
    """
    Parses a factor: NUM | (expression) | (-|+) factor

    Handles numbers, parenthesized expressions, and unary operators.
    Unary + raises an error.

    Args:
        tokens (list): List of tokens.
        pos (list): Mutable position.

    Returns:
        int or dict: Number or AST node.

    Raises:
        ValueError: For invalid syntax or unary +.
    """
    if current(tokens, pos)['type'] == 'NUM':
        val = int(current(tokens, pos)['value'])
        consume(pos)
        return val
    elif current(tokens, pos)['type'] == 'LPAREN':
        consume(pos)
        expr = parse_expression(tokens, pos)
        if not current(tokens, pos) or current(tokens, pos)['type'] != 'RPAREN':
            raise ValueError("Missing closing parenthesis ')'")
        consume(pos)
        return expr
    elif current(tokens, pos)['type'] == 'OP' and current(tokens, pos)['value'] in '+-':
        op = current(tokens, pos)['value']
        consume(pos)
        expr = parse_factor(tokens, pos)
        if op == '+':
            raise ValueError("Unary + not supported")
        else:
            return {'op': 'neg', 'expr': expr}
    else:
        raise ValueError("Invalid factor")

def tree_to_string(tree):
    """
    Converts an AST to its prefix string representation.

    Args:
        tree: AST node (int for numbers, dict for operators).

    Returns:
        str: Prefix notation string.
    """
    if isinstance(tree, int):
        return str(tree)
    elif tree['op'] == 'neg':
        return f"(neg {tree_to_string(tree['expr'])})"
    else:
        return f"({tree['op']} {tree_to_string(tree['left'])} {tree_to_string(tree['right'])})"

def evaluate(tree):
    """
    Evaluates the AST to compute the numerical result.

    Args:
        tree: AST node.

    Returns:
        float: The computed value.

    Raises:
        ValueError: For division by zero.
    """
    if isinstance(tree, int):
        return tree
    elif tree['op'] == 'neg':
        return -evaluate(tree['expr'])
    elif tree['op'] == '+':
        return evaluate(tree['left']) + evaluate(tree['right'])
    elif tree['op'] == '-':
        return evaluate(tree['left']) - evaluate(tree['right'])
    elif tree['op'] == '*':
        return evaluate(tree['left']) * evaluate(tree['right'])
    elif tree['op'] == '/':
        right = evaluate(tree['right'])
        if right == 0:
            raise ValueError("Division by zero")
        return evaluate(tree['left']) / right

def main():
    """
    Main function: reads input, processes each expression, writes output.
    """
    input_file = 'Q2/sample_input.txt'
    output_file = 'Q2/output.txt'

    # Read all input lines
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Process each line and write output
    with open(output_file, 'w') as out:
        for line in lines:
            expr = line.strip()
            try:
                # Tokenize
                tokens = tokenize(expr)
                # Parse using position list
                pos = [0]
                tree = parse_expression(tokens, pos)
                # Check for extra tokens
                if pos[0] < len(tokens) and tokens[pos[0]]['type'] != 'END':
                    raise ValueError("Extra tokens after expression")
                # Build tree string
                tree_str = tree_to_string(tree)
                # Evaluate
                try:
                    result = evaluate(tree)
                    # Format result as int if whole number
                    result_str = str(int(result)) if result == int(result) else str(result)
                except ValueError:
                    result_str = 'ERROR'
                # Format tokens
                tokens_str = " ".join(f"[{t['type']}]" if t['type'] == 'END' else f"[{t['type']}:{t['value']}]" for t in tokens)
            except (ValueError, IndexError):
                # Any error: set all to ERROR
                tree_str = 'ERROR'
                tokens_str = 'ERROR'
                result_str = 'ERROR'

            # Write output in specified format
            out.write(f"Input: {expr}\n")
            out.write(f"Tree: {tree_str}\n")
            out.write(f"Tokens: {tokens_str}\n")
            out.write(f"Result: {result_str}\n\n")

if __name__ == "__main__":
    main()