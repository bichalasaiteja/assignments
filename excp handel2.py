#case1--exception raised at outer try and corresponding except block is matched
try:
    print(int("abcd"))
    try:
        print("inner try block")
        print("inner try block2")
    except ZeroDivisionError:
        print("inner except block")
    finally:
        print("inner finally block")
    print("outside the inner block")
except ValueError:
    print("outer except block")
    print("outer except block2")
finally:
    print("outer finally block")
print("outside the all block")


#case2--exception raised at outer try and corresponding except block is not matched
try:
    print(int("abcd"))
    try:
        print("inner try block")
        print("inner try block2")
    except ZeroDivisionError:
        print("inner except block")
    finally:
        print("inner finally block")
    print("outside the inner block")
except SyntaxError:
    print("outer except block")
    print("outer except block2")
finally:
    print("outer finally block")
print("outside the all block")


#case3--exception raised at inner try(stat3) and corresponding except block is  matched
try:
    print("hello")
    try:
        print("inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("inner except block")
    finally:
        print("inner finally block")
    print("outside the inner block")
except SyntaxError:
    print("outer except block")
    print("outer except block2")
finally:
    print("outer finally block")
print("outside the all block")