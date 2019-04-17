from threading import Timer
import time

def hello():
    print("hello, world")
    Timer(2.0, hello).start()

# Timer(2.0, hello).start() # after 30 seconds, "hello, world" will be printed

# blast off v1
# def blast_off():
#     count = 10
#     while count > 0:
#         print(count)
#         count -= 1

# blast_off()

#blast off v2
# def blast_off():
#     count = 10
#     while count > 0:
#         print(count)
#         count -= 1
#         if count == 0:
#             print('blast off!')

# blast_off()

#blast off v3
# def blast_off():
#     count = input("enter a number: ")
#     count = int(count)
#     while count > 0:
#         print(count)
#         count -= 1
#         if count == 0:
#             print('blast off!')

# blast_off()

#blast off v4
# def blast_off():
#     count = int(input("enter a number: "))
#     if count > 20:
#         count = int(input("enter a number SMALLER than 20: "))
#     while count > 0:
#         print(count)
#         count -= 1
#         if count == 0:
#             print('blast off!')

# blast_off()


# blast off v5
def blast_off():
    count = int(input("enter a number: "))
    if count > 20:
        count = int(input("enter a number SMALLER than 20: "))
    while count > 0:
        print(count)
        time.sleep(1)
        count -= 1
        if count == 0:
            print('blast off!')

blast_off()