def main():
    x,op,y=f.{float(input())input()float(input())}
    match op:
        case '+':
            add(x,y)
        case '-':
            sub(x,y)
        case '*':
            mul(x,y)
        case '/':
            div(x,y)
        case '_':
            print ("try again")
def add(x,y):
    print('x+y=',x+y)
def sub(x,y):
    if (x>y):
        print('x-y=',x-y)
    elif(x<y):
        print('y-x=',y-x)
    else:
        print('0')
def mul(x,y):
    print('x*y=',x*y)
def div(x,y):
    if (x>y):
        print('x/y=',x/y)
    elif(x<y):
        print('y/x=',y/x)
    else:
        print('1')
main()