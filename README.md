# Numerative Text Converter
## Purpose
This program is a Python 3 implementation of a numerative text converter which performs these two main functions:
- convert a text as string to a base 32 decimal number (which can be VERY large)
- convert a decimal number to text, based on the same given base 32 alphabet as above

This program can also be used with other (also larger or smaller) alphabets, the preset however is the base 32 alphabet from 0 to 9 and from a to v. If you want to use this program with another alphabet (f.e. the hex-aplhabet), you just have to change the content of the alphabet in the code*.

## How to use
`python b32converter.py `[`-parameter`]` text`|`number`

### Parameters:
- `i`, `int`, `n`, `num`, `number` --> force interpretation as decimal-number
- `t`, `txt`, `text`, `s`, `str`, `string` --> force interpretation as text-string
- `text`|`number` --> the text or number to be processed
- `help` --> show the help

### Examples:
`python3 b32converter.py "text"`

Force interpretation of main parameter as decimal-number: `python3 b32converter.py -n 1337` --> 19p (output is base32-text)

Force interpretation of main parameter as base32-string: `python3 b32converter.py -s 1337` --> 35943 (output is decimal-number)

### Exit Codes

`0: No Error`

`1: Unkown error`

`2: No parameters received`

`3: Wrong use of parameters`

## *Additional information: 
- The letters of the __text__ which is supposed to be converted will be interpreted __as lowercase__.
- Any __other characters__ which are not listed in the alphabet (for instance the letters w, x, y, z or any other characters than letters or numbers), they will be __replaced with 0__.
