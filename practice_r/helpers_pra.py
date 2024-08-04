a = [1, 2, 3, 4, 5]
b = [7, 8, 9, 0, 4]
c = [4, 5, 6, 7, 8]
d = (9,10,11,12,)
z = list(zip(a, b, c,d))
zz = tuple(zip(b, a, d))
#zzz2 = dict(zip(b, c, a))
zzz = dict(zip(b, c))
print(z)
print(zz)
print(zzz)
fv = [1, 2, 3, 4, 5, 6, 7, 8, 5, 6, 3, 4, 7, 8]
def even_one(e):
        li = [3,4,5,6,7,8,9,]
        return e in li
f =filter(even_one,fv)
print(list(f))
r_1 = filter(lambda e: e%2==0,fv)
print(list(r_1))
r_2 = filter(lambda e: e%2!=0,fv)
print(list(r_2))

#def raj_one(r,z):
    #return r in d
#ra = list(zip(a,b,))
#print(ra)
