from __future__ import print_function
import sys, json

cmds = [x.strip().split(' ', 1) for x in sys.stdin.readlines()]

db = []

# TODO: implement KMP algorithm
def contains_list(pat, src):
	for i in range(len(src)-len(pat)+1):
		matched = True
		for j in range(len(pat)):
			if not json_contains(pat[j], src[i+j]):
				matched = False
				break
		if matched: return True
	return False

def json_contains(pat, src):
	if type(pat) != type(src):                        return False
	if type(pat) in [bool, int, float, str, unicode]: return pat == src 
	if type(pat) == list:                             return contains_list(pat, src)
	if type(pat) == dict:
		if all(k in src and json_contains(pat[k], src[k]) for k in pat.keys()):
			return True
		return any(json_contains(pat, src[key]) for key in src.keys())
	raise Exception('Invalid Type:', type(pat), type(src))

for c, val in cmds:
	obj = json.loads(val)
	if   c == 'add':    db.append((val, obj))
	elif c == 'get':    [print(s) for s, x in db if json_contains(obj, x)]
	elif c == 'delete': db = [(s, x) for s, x in db if not json_contains(obj, x)]
