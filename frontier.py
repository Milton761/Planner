import queue

class Frontier:

	def __init__(self):
		print("Frontier")


class Stack(Frontier):

	def __init__(self):
		print("Stack")



F = Frontier()
S = Stack()

print(F.__class__.__name__)
print(S.__class__.__name__)

q = queue.Queue()

q.put(1)
q.put(3)
q.put(2)

print(q.get())
print(q.get())
print(q.qsize())

s = queue.LifoQueue()

s.put(1)
s.put(3)
s.put(2)

print(s.get())
print(s.get())


s = queue.PriorityQueue()

s.put(1)
s.put(3)
s.put(2)

print(s.get())
print(s.get())
