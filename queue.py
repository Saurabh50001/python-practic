# Queue is a linear data structure.
# Stores items in First in first out(fifo) manner
# Queue Operations :-
# Enqueue => Adds an item to the queue.
# Dequeue => Removes an item from the queue.
# front => Get the front(first) item from queue.
# Rear => Get the last(rear) item from queue.

l=[]
while True:
    c=int(input('''
    1 enqueue Elements
    2 dequeue first Elements
    3 front Element
    4 last Element
    5 Display Queue
    6 Exit
    '''))
    if c==1:
        n=input("Enter the value")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Queue")    
        else:
           del l[0]
           print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Queue")
        else:
            print("First Queue Value :-",l[0])
    elif c==4:
        if len(l)==0:
            print("Empty Queue")
        else:
            print("Last Queue Value :-",l[-1])
    elif c==5:
        print("Display Queue :-" ,l)        
    elif c==6:
        break
    else:
        print("invalid opr...")