# Welcome to HIT137 Assignment 2! 🎉

Hey there! This is our project for HIT137 Assignment 2. We've created two Python programs that handle text encryption/decryption and mathematical expression parsing. Let's dive in!

## What This Project Does

### Q1: Text Encryption & Decryption

- Takes plain text from a file
- Encrypts it using clever shifting rules based on letter positions
- Saves the encrypted version
- Decrypts it back
- Checks if everything matches perfectly

### Q2: Expression Parser

- Reads math expressions from a file
- Breaks them down into tokens
- Parses them with proper operator precedence
- Builds a tree representation
- Evaluates the expressions
- Handles errors gracefully

## Quick Setup

### Get the Code

```bash
git clone https://github.com/Dharma001/HIT137-Assignment2.git
cd HIT137-Assignment2
```

### What You Need

- Python 3.x (that's it!)

## Project Files

```
HIT137-Assignment2/
├── Q1/                          # Encryption program
│   ├── main.py                  # Main script
│   ├── encryption.py            # Encryption logic
│   ├── decryption.py            # Decryption logic
│   ├── file_handler.py          # File operations
│   ├── verify.py                # Verification
│   ├── raw_text.txt             # Input text
│   ├── encrypted_text.txt       # Encrypted output
│   └── decrypted_text.txt       # Decrypted output
├── Q2/                          # Parser program
│   ├── main.py                  # Main script
│   ├── sample_input.txt         # Math expressions
│   ├── sample_output.txt        # Expected results
│   └── output.txt               # Your results
├── README.md                    # This guide
└── github_link.txt              # Repository link
```

## How to Run

### Q1: Encryption/Decryption

```bash
cd Q1
python main.py
```

Enter two numbers when prompted - these are your encryption keys!

### Q2: Expression Parser

```bash
cd Q2
python main.py
```

Check `output.txt` for the parsed results.

## What You'll See

**Q1**: Your text gets scrambled, then unscrambled, with a success message.

**Q2**: For each math problem:

```
Input: 2 + 3 * 4
Tree: (+ 2 (* 3 4))
Tokens: [NUM:2] [OP:+] [NUM:3] [OP:*] [NUM:4] [END]
Result: 14
```

## Cool Features

- **Q1**: Position-based encryption (not just simple shifts!)
- **Q2**: Handles complex expressions, unary operators, and nested parentheses

## Need Help?

- Make sure you're in the right folder
- Use whole numbers for Q1 shifts
- Check `python --version` if things don't work
- Error messages are usually helpful!

## Fun Notes

- Q1's encryption adapts based on where letters appear in the text
- Q2 can handle tricky cases like --5 or -(3+4)
- Both programs use clean Python code with no extra libraries

Enjoy exploring the code! If you have questions, feel free to ask. 🚀
