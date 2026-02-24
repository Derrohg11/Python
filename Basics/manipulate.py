m = [["apple", "banana", "cherry"], ["dog", "cat", "mouse"], ["red", "green", "blue"]]
#Without list comprehension
mod_m = []
for sublist in m:
    mod_sublist = []
    for item in sublist:
        mod_sublist.append(item.capitalize())
    mod_m.append(mod_sublist)

print(mod_m)

#Using list comprehension
m = [["apple", "banana", "cherry"], ["dog", "cat", "mouse"], ["red", "green", "blue"]]
mod_m = [[item.capitalize() for item in sublist] for sublist in m]
print(mod_m)