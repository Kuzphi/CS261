def CheckSingle(Input):
	dic = {}
	for item in Input:
		if dic.has_key(item):
			dic[item] += 1
		else:
			dic[item] = 1
	ans = []
	for key in dic:
		if dic[key] == 1:
			ans.append(key)
	return ans


