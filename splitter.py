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
		l = 0
		for i in range (int(len(string)/self.n)+2):
			substring = string[l:i * self.n]
			p = substring.rfind(" ")
			if p == -1:
				self.lines.append(substring)
				l = i * self.n		
			else:
				self.lines.append(substring[:p])
				l = l + p + 1
						
						
s = splitter(20)
s.split("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(s)

s.split("ABCDEFGHIJKLMNOPQRSTUVWXYZ"+
				"abcdefghijklmnopqrstuvwxyz")
print(s)

# The cat sat on the 
# mat by the door
s.split("The cat sat on the mat by the door")
print(s)
