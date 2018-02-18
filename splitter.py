# splitter - break a long string into shorter lines - with a max length of n...

class splitter():
	def __init__(self, n):
		self.n = n
		
	def split(self, string):
		r = ""
		l = 0
		for i in range (int(len(string)/self.n)+2):
			substring = string[l:i * self.n]
			p = substring.rfind(" ")
			if p == -1:
				r += substring + "\n"
				l = i * self.n		
			else:
				r += substring[:p] + "\n"
				l = l + p + 1
		return r
		
s = splitter(20)
string = s.split("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(string)

string = s.split("ABCDEFGHIJKLMNOPQRSTUVWXYZ"+
								 "abcdefghijklmnopqrstuvwxyz")
print(string)

# The cat sat on the 
# mat by the door
string = s.split("The cat sat on the mat by the door")
print(string)
