stack = []
def push():
    element = input("Enter Ele: ")
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("Empty stack")
    else:
        element = stack.pop()
        print("removed:", element)
        print(stack)

while True:
    print("Select the options 1.push 2.pop 3.quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Incorrect operation")


# for i in range(4, 10, 2):
#     print(i)
