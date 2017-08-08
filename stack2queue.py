# using two stacks as a queue

class stack2queue:
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, item):
        self.instack.append(item)


    def dequeue(self):
        if len(self.outstack) == 0:
            if len(self.instack) > 0:
                for i in range(len(self.instack)):
                    self.outstack.append(self.instack.pop())
                first = self.outstack.pop()
                for i in range(len(self.outstack)):
                    self.instack.append(self.outstack.pop())
                return first
            else:
                return '[]'

    def whose_next(self):
        return self.instack[0]

s2q = stack2queue()

q = int(input().strip())

for i in range(q):
    line = input().strip()
    if line[0] == '1':
        q_type, x = line.split()
        s2q.enqueue(x)
    elif line[0] == '2':
        s2q.dequeue()
    elif line[0] == '3':
        print(s2q.whose_next())

    

