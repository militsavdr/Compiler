#  Compiler Implementation Project

##  Overview
This project implements a **translator (compiler)** capable of performing the complete sequence of stages in a compilation process — including **lexical analysis**, **syntax analysis**, **intermediate code generation**, **symbol table management**, and **final code generation**.

The goal of this project is to provide a **practical understanding of compiler design principles**, illustrating how high-level language instructions are analyzed, transformed, and translated into executable code.

This work was developed as part of a **university coursework project** on compiler design and programming languages.

---

##  Compilation Stages

### 1.  Lexical Analysis
The **lexical analyzer (lexer)** scans the source code and breaks it down into **tokens**, such as identifiers, keywords, operators, and literals.  
It ensures that the input conforms to the valid lexical structure of the language.

**Output:** Token stream saved in a structured format (e.g., tuples of type and value).

---

### 2.  Syntax Analysis
The **syntax analyzer (parser)** receives the tokens from the lexer and checks if they form valid grammatical constructs according to the language grammar.  
It detects **syntactic errors** and builds the **parse tree** or **syntax tree** representing the program’s structure.

**Output:** Abstract Syntax Tree (AST) or parse representation.

---
### 3. Intermediate Code Generation
The **intermediate representation (IR)** bridges the gap between the high-level source code and low-level machine code.  
It simplifies optimization and final translation by converting operations into a uniform form, typically **quadruples** or **three-address code (TAC)**.

---
### 4.  Symbol Table Management
The **symbol table** stores information about identifiers (variables, constants, functions) encountered during parsing.  
It maintains metadata such as:
- Name  
- Type  
- Scope  
- Memory address or offset  
- Value (if applicable)

This structure is crucial for semantic checks and code generation.

---
### 5.  Final Code Generation
The final stage translates the intermediate representation into **target machine code** or **assembly instructions**.  
It uses the symbol table to map identifiers to memory addresses and ensures the correct execution order.

**Output:** Executable-like or assembly-level code that can be simulated or executed.

---

