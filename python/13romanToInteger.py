class Solution:
    def romanToInt(self, s: str) -> int:
    	inv_map = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
    	res = 0
    	for i in range(len(s)):
    		if i + 1 < len(s) and inv_map[s[i]] < inv_map[s[i+1]]:
    			res -= inv_map[s[i]]
    		else:
    			res += inv_map[s[i]]
    	return res
