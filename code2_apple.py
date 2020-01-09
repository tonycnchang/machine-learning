import os

def main():
    print("Hello World!")
    print("这是Tony\'的问候")
    print("这是Bob\'的问候")

    foo(5,10)

    print("==========")
    print("这将直接执行" + os.getcwd())

    counter = 0
    counter += 1

    food = ["苹果","杏","李子","梨"]
    for i in food:
        print("俺就爱整只：" + i)

    print("数到十")
    for i in range(10):
        print(i)

def foo(paraml,secondparam):
    res  = paraml + secondparam
    print("%s 加 %s 等于 %s" %(paraml,secondparam,res))
    if res < 50:
        print("这个")
    elif (res >= 50) and ((paraml == 42) or (secondparam == 24)):
        print("那个")
    else:
        print("嗯")
    return res

if __name__ == "__main__":
    main()
