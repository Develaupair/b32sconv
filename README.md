# Numerative Text Converter
## Purpose
This program is a Python 3 implementation of a numerative text converter which performs these two main functions:
- convert a base 32 text (string) to a decimal number (which can be VERY large)
- convert a decimal number to a base-32 text string

This program can also be used with other (also larger or smaller) alphabets, the preset however is the base 32 alphabet from 0 to 9 and from a to v. If you want to use this program with another alphabet (f.e. the hex-aplhabet), you just have to change the content of the alphabet in the code*.

## How to use
`python b32converter.py `[`-parameter`]` text`|`number`

### Parameters:
- `i`, `int`, `n`, `num`, `number` - force interpretation as decimal-number
- `t`, `txt`, `text`, `s`, `str`, `string` - force interpretation as text-string
- `text` or `number` - the input to be processed, which is either a text or a decimal number
- `help` - show the help

### Examples:
`python3 b32converter.py "text"` converts the string to a decimal number

`python3 b32converter.py -n 1337` forces the interpretation of the main parameter as decimal-number --> output is base32-text

`python3 b32converter.py -s 1337` forces the interpretation of the main parameter as base-32 text --> output is decimal number

### Exit Codes

`0`: No Error

`1`: Unkown error

`2`: No parameters received

`3`: Wrong use of parameters

## *Additional information: 
- The letters of the __text__ which is supposed to be converted will be interpreted __as lowercase__.
- Any __other characters__ which are not listed in the alphabet (for instance the letters w, x, y, z or any other characters than letters or numbers), they will be __replaced with 0__.
