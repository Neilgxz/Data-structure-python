“大O记法”： 对于单调的证书函数f，如果存在一个整数g和实常数c>0使得对于充分大的n总有f(n)<=c*g(n),
就说函数g是f的一个渐进函数（忽略常数），记为f(n)=O(g(n))。也就是说在趋近无穷的极限意义下，函数f的
增长速度受到函数g的约束，亦函数f与函数g的特征相似

时间复杂度： 假设存在函数g，使得算法A处理规模n的问题示例所用时间T(n)=O(g(n))，则称O(g(n))为算法A的
渐进时间复杂度（asymptomatic time complexity），简称时间复杂度，记为T（n）

O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<O(n^3)<O(2^n)<O(n!)<O(n^n)

import timeit  
class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>)  
	Timer是测量小段代码执行速度的类  
	stmt参数是要测试的代码语句（statement）  
	setup参数是运行代码时需要的设置  
	timer参数是一个定时器函数，与平台有关  

timeit.Timer.timeit(number = 1000000)  
	Timer类中测试语句执行速度的对象方法  
	方法返回执行代码的平均耗时，一个float类型的秒数  

timer1 = Timer("test()", "from __main__ import t1")  
print("append", timer1.timeir(1000))  

list = list + [i] 是把list和[i]先生成一个新的列表再传给list  
list += [i] 和extend类似，直接在list上操作  
少用前者加法  

range()： 在python2生成一个列表 srange()生成一个可迭代的对象  
	 在python3返回一个可迭代对象  

Python列表与字典操作的时间复杂度  
List:  
index[] 	 O(1)  
index assignment O(1)	赋值  
append 		 O(1)  
pop() 		 O(1)  
pop(i) 		 O(n)	最坏  
insert(i,item)   O(n)  
del 		 O(n)  
iteration 	 O(n)  
contains(in) 	 O(n)  
get slice[x:y] 	 O(k)	先找x位置再找k个  
del slice 	 O(n)	删之后要移位  
set slice 	 O(n+k)	li[0:3] = [2,3,4,5,6,7] 先删O()再补充O(k)  
reverse		 O(n)  
concatenate	 O(k)	第二个list补充k个在第一个后面  
sort		 O(nlogn)  
multiply	 O(nk)	k次  
  
dict:  
copy		 O(n)  
get item	 O(1)  
set item	 O(1)  
delete item	 O(1)  
contains(in)	 O(1)  
iteration	 O(n)  

抽象数据类型 Abstract Data Type （ADT）   
