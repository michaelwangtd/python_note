# -*- coding:utf-8 -*-

"""
python中使用到的两种try,except逻辑
"""

# one
'''
	try块在for里面，一旦出现错误，在except中结束本次循环
	然后可以在for后面的代码中实现接下来的逻辑
'''
resultList = []
testList = [4,3,2,1]
i = 1
for item in testList:
	try:
		result = 1 / (item - 2)
		print('结果为：',str(result))
		resultList.append(result)
	except Exception as ex:
		print('第',str(i),'条出现错误')
		print(ex)
		break
	print('已经处理数目...',str(i))
	i += 1
print(resultList)
'''
	result:
	结果为： 0.5
	已经处理数目... 1
	结果为： 1.0
	已经处理数目... 2
	第 3 条出现错误
	division by zero
	[0.5, 1.0]
'''

# two methon
'''
	其实，将resultList放在try外面，当except出现异常，后面的逻辑仍然能够执行
	这里，利用了finally，在finally中处理后续的逻辑
	尽管这里看起来，finally的作用没有利用起来
'''
resultList = []
testList = [4,3,2,1]
i = 1
try:
	for item in testList:
		result = 1 / (item - 2)
		print('结果为：',str(result))
		resultList.append(result)
		print('已经处理数目...', str(i))
		i += 1
except Exception as ex:
	print('第',str(i),'条出现错误')
	print(ex)
finally:
	print(resultList)
'''
	result:
	结果为： 0.5
	已经处理数目... 1
	结果为： 1.0
	已经处理数目... 2
	第 3 条出现错误
	division by zero
	[0.5, 1.0]
'''