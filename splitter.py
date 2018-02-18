# splitter - break a long string into shorter lines - with a max length of n...


class splitter():
	def __init__(self, n):
		self.n = n
		self.lines = []

	def __str__(self):
		r = ""
		for _ in self.lines:
			r += _ + "\n"
		return r

	def split(self, string):
		p = 0
		done = False
		while not done:
			if len(string[p:]) <= self.n:
				self.lines.append(string[p:])
				done = True
			else:
				substring = string[p:p + self.n]
				if substring[-1] == ' ':
					self.lines.append(substring)
					p += self.n
				else:
					q = substring.rfind(' ')
					if q != -1:
						self.lines.append(substring[:q])
						p += q + 1
					else:
						self.lines.append(substring)
						p += self.n


s = splitter(20)

s.split("ABCDEFGHIJKLMNOPQRS TUVWXYZ")
print(s)

s = splitter(20)
s.split("ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz")
print(s)

s = splitter(20)
# The cat sat on the 
# mat by the door
s.split("The cat sat on the mat by the door")
print(s)

s = splitter(12)
# The cat sat 
# on the mat 
# by the door
s.split("The cat sat on the mat by the door")
print(s)

s = splitter(30)
# The cat sat 
# on the mat 
# by the door
s.split("The cat sat on the mat by the door")
print(s)
