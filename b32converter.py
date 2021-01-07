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
        exit(1)
    else:
        try:
            number=int(sys.argv[1])//1
            print(decNumberToBaseNString(number))
        except:
            try:
                print(baseNStringToDecNumber(str(sys.argv[1])))
            except:
                print("unknown error")
