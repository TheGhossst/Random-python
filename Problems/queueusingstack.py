# Enter your code here. Read input from STDIN. Print output to STDOUT
def push(stack, item):
    stack.append(item)
    
def pop(stack):
    if len(stack) == 0:
        return
    else:
       return stack.pop()
        
def enqueqe(stack1,item):
    push(stack1, item)

def dequeue(stack1, stack2):
    if len(stack2) == 0:  
        while len(stack1) > 0:
            push(stack2, pop(stack1))
    return pop(stack2)

stack1 = []
stack2 = []

queries = int(input().strip())

for i in range(queries):
    input_line = input().strip()
    inputs = input_line.split()

    if len(inputs) == 2:
        choice, item = map(int, inputs)
    elif len(inputs) == 1:
        choice = int(inputs[0])
        item = None
    else:
        choice = item = None  
    
    if choice == 1:
        enqueqe(stack1, item)
    elif choice == 2:
        dequeue(stack1, stack2)
    elif choice == 3:
        if len(stack2) > 0:
            print(stack2[-1])
        else:
            print(stack1[0])

    

