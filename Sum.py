import math
import os
from unittest import result


class MyBigNumber:
    a = "0"
    b = "0"
    chuoia = []
    chuoib = []
    result = ""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        self.chuoia = list(self.a)
        self.chuoib = list(self.b)

        tmpresult = []
        lena = len(self.chuoia)
        lenb = len(self.chuoib)
        rem = 0
        step = 0
        limit = lena if lena <= lenb else lenb

        while (step < limit):
            step = step + 1
            tmpsum = int(self.chuoia[lena-step]) + int(self.chuoib[lenb-step]) if rem == 0 else int(
                self.chuoia[lena-step]) + int(self.chuoib[lenb-step]) + rem

            if tmpsum >= 10:
                rem = 1
                tmpresult.insert(0, tmpsum-10)
                print(f"Step {step}: {
                      self.chuoia[lena-step]} + {self.chuoib[lenb-step]} = {tmpsum} => {tmpresult} (1) ")
            else:
                rem = 0
                tmpresult.insert(0, tmpsum)
                print(f"Step {step}: {
                      self.chuoia[lena-step]} + {self.chuoib[lenb-step]} = {tmpsum} => {tmpresult} (0)")

            if (step == limit):
                left = ''.join([str(elem) for elem in self.chuoia[0:lena-limit]] if limit ==
                               lenb else [str(elem) for elem in self.chuoib[0:lenb-limit]])
                print("Left:", left)
                tmpsum = int(left)+rem
                tmpresult.insert(0, tmpsum)
                print(
                    f"Step {step+1}: {left}(Left) + {rem}(Remember) => {tmpresult}")

        for i in tmpresult:
            self.result += str(i)
        print(f"Result: {self.result}")


def main():
    exit = ""
    while (exit != "x"):
        os.system('cls')
        print("Nhap a va b:")
        f = input(" a = ")
        s = input(" b = ")
        print("Explain: []: Taken Value; (): Remember")
        cal = MyBigNumber(f, s)
        cal.sum()
        exit = input("Input 'x' to exit program\n")


main()
