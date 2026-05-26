#CONTROL CENTER

def cal():
    print("Choose One Operation: ")
    print("1: +\n2: -\n3: x\n4: /\n5: %\n6: //\n7: ^\n8: =\n9: !=\n10: >\n11: <\n 12: >=\n13: <=\n")

    op=input("Chosen Operation: ")
    op=op.lower()
    try:
        a=int(input("Enter 1st Operand: "))
        b=int(input("Enter 2nd Operand: "))
        match op:
            case '+':
                res=a+b
                return res

            case '-':
                res=a-b
                return res

            case 'x'|'*':
                res=a*b
                return res

            case '/':
                res=a/b
                return res

            case '%':
                res=a%b
                return res

            case '//':
                res=a//b
                return res

            case '^'|'**':
                res=a**b
                return res

            case '='|'==':
                res=a==b
                return res

            case '!='|'=!':
                res=a!=b
                return res

            case '>':
                res=a>b
                return res

            case '<':
                res=a<b
                return res

            case '>=':
                res=a>=b
                return res

            case '<=':
                res=a<=b
                return res

            case _:
                return "Invalid"
    except ValueError:
        print("Enter Number Input Please")
print("Welcome To Number Calculator!!\n")
print(cal())