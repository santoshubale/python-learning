# Basics

## Indentation

In Python, indentation is a core part of the syntax and is used to define the structure and scope of the code. Unlike many other programming languages that use braces {} or keywords to mark blocks of code, Python relies solely on indentation. Improper indentation will result in a IndentationError or unexpected behavior.

## Rules for Indentation

Consistent indentation is required. Typically, either 4 spaces or a tab is used per level, but never mix the two. The first line of a block must be indented, and subsequent lines in the same block must match that indentation level. Indentation is rejected as inconsistent if a source file mixes tabs and spaces in a way that makes the meaning dependent on the worth of a tab in spaces; a TabError is raised in that case.

## Comment and multiline comment

\# is used for comments. There is no multiline comments in Python, either you can use \# for multiple lines or as a workaround you can use """ this is multiline comment """

## Reserved words

Cannot be used as ordinary identifiers.
| Keyword | Keyword | Keyword | Keyword | Keyword |
|-----------|-----------|-----------|-----------|-----------|
| False | await | else | import | pass |
| None | break | except | in | raise |
| True | class | finally | is | return |
| and | continue | for | lambda | try |
| as | def | from | nonlocal | while |
| assert | del | global | not | with |
| async | elif | if | or | yield |

## Escape Sequence

| Escape Sequence | Meaning                          | Notes |
| --------------- | -------------------------------- | ----- |
| `<newline>`     | Backslash and newline ignored    | (1)   |
| `\\`            | Backslash (`\`)                  |       |
| `\'`            | Single quote (`'`)               |       |
| `\"`            | Double quote (`"`)               |       |
| `\a`            | ASCII Bell (BEL)                 |       |
| `\b`            | ASCII Backspace (BS)             |       |
| `\f`            | ASCII Formfeed (FF)              |       |
| `\n`            | ASCII Linefeed (LF)              |       |
| `\r`            | ASCII Carriage Return (CR)       |       |
| `\t`            | ASCII Horizontal Tab (TAB)       |       |
| `\v`            | ASCII Vertical Tab (VT)          |       |
| `\ooo`          | Character with octal value `ooo` | (2,4) |
| `\xhh`          | Character with hex value `hh`    | (3,4) |
