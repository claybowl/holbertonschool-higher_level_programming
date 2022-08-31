#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    num = len(sys.argv) - 1
    if num == 0:
        div = '.'
    else:
        div = ':'
    if num == 1:
        arg = "argument"
    else:
        arg = "arguments"

    print(f"{num} {arg}{div}")
    for i in range(1, (num + 1)):
        print(f"{i}: {str(sys.argv[i])}")
