#list copy
import copy

li = [1,2,3,4,5,6,7,8,9]
li2 = li.copy()
li3 = li
li[2] = "rajesh",2.5
print(li)
print(li2)
print(li3)

#set copy

se = {1,2,3,5,4,}
se1 = {22,33,6,7,8,9,}
se2 = se1.copy()
se = se1
se1.add("rajesh")
se.add("challa")
print(se)
print(se1)
print(se2)


#dict copy

di = {1:66,2:22,3:44,4:55,}
di2 = {22:75,8:95,9:98}
di1 = di2.copy()
di = di2
di.update({99:697})
print(di)
print(di2)
print(di1)
d = {i:i**2 for i in range(0,20)}
print(d)
dd = d.copy()
print(dd)
d.update({"rajesh":"challa"})
print(d)

#import copy

import copy

#copy.copy()

li = [1, 2, 3, 4]
li1 = copy.copy(li)

li1[2] = 'rajesh'

print("li:", li)
print("li1:", li1)

#deepcopy()

di = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
di1 = copy.deepcopy(di)

di1['b'][1] = 'rajesh'
di1['c']['d'] = 'challa'

print("di:", di)
print("di1:", di1)