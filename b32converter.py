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

import sys;alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']
def charToDecDigit(char):return alphabet.index(char.lower())if alphabet.__contains__(char.lower())else 0
def decDigitToChar(decDigit):return alphabet[(decDigit)%(len(alphabet))]
def baseNStringToDecNumber(text,result=0):
    for i in range(len(text)-1,-1,-1):result+=(pow(len(alphabet),(len(text)-1-i))*charToDecDigit(text[i]))
    return(result)
def decNumberToBaseNString(decNumber,result=""):
    while decNumber>0:rest=(decNumber%len(alphabet));decNumber=((decNumber-rest)//len(alphabet));result=decDigitToChar(int(rest))+result
    return result
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("use:", "python <thisfile>", '<"text(string)"|number>')
        exit(2)
    else:
        try:
            number=int(sys.argv[1])//1
            print(decNumberToBaseNString(number))
        except:
            try:
                print(baseNStringToDecNumber(str(sys.argv[1].strip("\""))))
            except:
                print("unknown error")
                exit(1)