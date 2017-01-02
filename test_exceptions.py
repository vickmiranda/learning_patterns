def raise_error():
    a = True
    if a:
        raise IOError("Always raise error")
    else:
        print a

def test1():
    b = 'other test'
    print b

def test2():
    a = 'test1'
    try:
        raise_error()
    except:
        raise ValueError("Val error")

    # finally:
    #     return True

def test3():
    c = 'other test'
    print c

def main():
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()

