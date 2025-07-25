class Solution():	
	def myAtoi(self, s: str) -> int:
		if not s: return 0

		n = len(s); i = 0; res = 0; flag = "+"

		while i<n and s[i]==" ": i+=1      #ignoring whitespace

		if i<n and (s[i] == "-" or s[i] == "+"):
			flag = s[i]
			i+=1

		while i<n:
			if s[i].isdigit():
				res = res*10 + int(s[i])
				i+=1    
			else: break

		res = res if flag == "+" else -res
		res = min(res, 2 ** 31 - 1)
		res = max(-(2 ** 31), res)

		return res