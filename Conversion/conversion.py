class convert:

    # Convert Decimal to Binary
    @staticmethod
    def binary(num):
        lst = []
        while True:
            q = num//2
            r = num - (q*2)
            lst.append(r)
            num = q
            if q == 0:
                break
        a = lst[::-1]
        for i in a:
            print(i,end="")
        print()

    # Convert Decimal to Octal
    @staticmethod
    def octal(num):
        lst = []
        while True:
            if num<8:
                lst.append(num)
                break
            if num>8:
                q = num//8
                r = num-q*8
                lst.append(r)
                num = q
        a = lst[::-1]
        for i in a:
            print(i,end="")
        print()

    # Convert Decimal to Hexadecimal
    @staticmethod
    def hexadec(num):
        lst = []
        while True:
            if num<10:
                lst.append(str(num))
                break
            if num == 10:
                lst.append('a')
                break
            elif num == 11:
                lst.append('b')
                break
            elif num == 12:
                lst.append('c')
                break
            elif num == 13:
                lst.append('d')
                break
            elif num == 14:
                lst.append('e')
                break
            elif num == 15:
                lst.append('f')
                break
            if num>15:
                q = num//16
                r = num-q*16
                if r == 10:
                    lst.append('a')
                elif r == 11:
                    lst.append('b')
                elif r == 12:
                    lst.append('c')
                elif r == 13:
                    lst.append('d')
                elif r == 14:
                    lst.append('e')
                elif r == 15:
                    lst.append('f')
                else:
                    lst.append(str(r))
                num = q
        a = lst[::-1]
        for i in a:
            print(i,end="")
        print()
     

