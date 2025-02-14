# Python Programming Language Notes

This document provides an overview of **Python Programming** concepts, from **history** to **advanced topics**. Whether you're a beginner or an advanced Python programmer, this guide will help you understand the language's key features.

## Table of Contents
1. [History of Python](#1-history-of-python)
2. [Character Set](#2-character-set)
3. [Variables](#3-variables)
4. [Data Types](#4-data-types)
5. [Strings](#5-strings)
6. [Conditional Statements](#6-conditional-statements)
7. [Indexing](#7-indexing)
8. [Lists and Tuples](#8-lists-and-tuples)
9. [Directory Methods](#9-directory-methods)
10. [Sets](#10-sets)
11. [Loops](#11-loops)
12. [Functions](#12-functions)
13. [File Input and Output (I/O)](#13-file-input-and-output-io)
14. [Object-Oriented Programming (OOP) Concepts](#14-object-oriented-programming-oop-concepts)

---

## 1. History of Python
- **Developed by**: Guido van Rossum in **1989**.
- **First release**: **Python 0.9.0** was released in **1991**.
- **Design philosophy**: Emphasizes code readability, simplicity, and ease of learning.
- **Versions**:
  - **Python 2.x** (1991–2020) – Earlier version, now deprecated.
  - **Python 3.x** (2008–present) – Current version, backward incompatible with Python 2.
- **Popular Usage**: Widely used in web development, data science, machine learning, and scientific computing.

---

## 2. Character Set
Python supports the **Unicode character set**, meaning it can handle characters from most human languages, including alphabets, symbols, and emojis.

- **String literals** in Python can be defined using:
  - Single quotes: `'hello'`
  - Double quotes: `"hello"`
  - Triple quotes (for multi-line strings):
    ```python
    """This is a 
    multi-line string"""
    ```

---

## 3. Variables
A **variable** is a name given to a memory location used to store data.
- **Declaration**: Python does not require explicit declaration of variables (no need to declare type).
  ```python
  x = 10   # integer variable
  y = 3.14 # float variable
  name = "Alice" # string variable
