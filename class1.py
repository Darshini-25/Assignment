#EXAMPLE ON LIST AND ITS METHODS

vegetables=["potato","raddish","beans","carrot","tomato","onion"]
print(vegetables)

#append
vegetables.append("pumpkin")
print(vegetables)

#insert
vegetables.insert(1,"sweetpotato")
print(vegetables)

#sort
vegetables.sort()
print(vegetables)

#reverse
vegetables.reverse()
print(vegetables)

#pop
vegetables.pop()
print(vegetables)

#remove
vegetables.remove("raddish")
print(vegetables)

#slicing
print(vegetables[0:4])


#EXAMPLE ON TUPLE

t=(5,45.6,8,"car","fruits",25,44,"car")
print(t)

#count-->count the occurance of the value/data in given tuple
print(t.count("car"))
print(t.count(8))

#index-->displays the index value for the specified data
print(t.index(25))

#slicing
print(t[-4:-2])

#EXAMPLE ON DICTIONARY

details={"name":"darshini",
         "number":12345678,
         "course":"cse"
    }
print(details)
print(details.items())
print(details.keys())

#update
details.update({"state":"karnataka","number":98765432})
print(details)

#SLICING

a="roller coaster"
print(a[-14:-8])
print(a[-7:-2])
print(a[-5:15])
print(a[0:-10])


#STEP INDEX

b="teachnook internship"
print(b[-20::1])
print(b[-4::1])
print(b[-12:-7:2])
print(b[-16:-21:-2])
print(b[-1:-20:-9])

#SET AND FROZENSET

#set
s=set()
print(s)
print(type(s))

#frozen set
f=frozenset()
print(f)
print(type(f))

s={1,2,3,4}
l=['Denmark','Australia','Russia','Spain','HolySee']
t=('V','O','W','E','L')
f=frozenset(l)
print(f)
f1=frozenset(t)
print(f1)








