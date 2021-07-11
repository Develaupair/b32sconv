"""
This program is a fun text to base 32 number converter. This works by interpreting every character (0-9a-v) as digit of a 32 digit alphabet and calculating the number. It also works the other way around.
Copyright (C) 2021 Anubosiris

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys;DEBUGMODE=False;alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']
def charToDecDigit(char):return alphabet.index(char.lower())if alphabet.__contains__(char.lower())else 0
def decDigitToChar(decDigit):return alphabet[(decDigit)%(len(alphabet))]
def baseNStringToDecNumber(text,result=0):
    for i in range(len(text)-1,-1,-1):result+=(pow(len(alphabet),(len(text)-1-i))*charToDecDigit(text[i]))
    return(result)
def decNumberToBaseNString(decNumber,result=""):
    while decNumber>0:rest=(decNumber%len(alphabet));decNumber=((decNumber-rest)//len(alphabet));result=decDigitToChar(int(rest))+result
    return result
def dprint(text):print(str("DEBUG: "+text+"\n") if DEBUGMODE else "", end='')
def help(ecode = 0):
    print('\n@##############+-->{ PYTHON3 NUMERATIVE TEXT CONVERTER }<--+###############@')
    print('#                                                                          #')
    print('#   How to use:                                                            #')
    print('#   python3 b32converter.py [-parameter] text|number                       #')
    print('#                                                                          #')
    print('#   Parameters:                                                            #')
    print('#   text|number --> the (b32) text or (b10) number to be processed         #')
    print('#   i, int, n, num, number --> force interpretation as decimal-number      #')
    print('#   t, txt, text, s, str, string --> force interpretation as text-string   #')
    print('#   help --> show this help page                                           #')
    print('#                                                                          #')
    print('@##########################################################################@\n')
    exit(ecode)
if __name__ == "__main__":
    if ((sys.argv[0].lower().strip(" ")=="-help")or(sys.argv[0].lower().strip(" ")=="--help")): help()
    if len(sys.argv) == 1:
        help(2)
    elif len(sys.argv) >= 3:
        a=sys.argv[1].lower().strip()
        if (a=="-t")or(a=="-txt")or(a=="-text")or(a=="-s")or(a=="-str")or(a=="-string"):
            try:
                print(baseNStringToDecNumber(str(sys.argv[2].strip("\""))))
            except:
                print("ERROR: Parameter could not be interpreted as string\n")
                exit(3)
        elif (a=="-n")or(a=="-num")or(a=="-number")or(a=="-i")or(a=="-int"):
            try:
                number=int(sys.argv[2])//1
                print(decNumberToBaseNString(number))
            except:
                print("ERROR: Parameter could not be interpreted as number\n")
                exit(3)
        else:
            print("ERROR: Invalid use of parameters\n")
            exit(3)
    else:
        try:
            number=int(sys.argv[1])//1
            print(decNumberToBaseNString(number))
        except:
            try:
                print(baseNStringToDecNumber(str(sys.argv[1].strip("\""))))
            except:
                print("ERROR: unknown error\n")
                exit(1)
    exit(0)
