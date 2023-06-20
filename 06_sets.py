### Sets ###

my_set = set()
my_other_set ={}

print (type(my_set))
print (type(my_other_set))

my_other_set={"JC","Sardiñas", 55}
print (type(my_other_set))

print(len(my_other_set))

my_other_set.add("Mouredev")

print(my_other_set)

my_other_set.add("Mouredev")

print(my_other_set)

print("JC" in my_other_set)
print("JCi" in my_other_set)

my_other_set.remove("JC")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

#del my_other_set

my_set = {"JC", "Barrero", 33}
print(my_set)
my_list = list (my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin","Swift","Python"}

my_new_set = my_set.union(my_other_set)
print (my_new_set)