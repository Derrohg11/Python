# fruits = {"Apple", "Banana", "Cherry"}
# print(fruits)

# empty_set = set()
# print(type(empty_set))

# list_set = set([1, 2, 3, 4, 5])

# tuple_set = set((1, 2, 3, 4, 5))

# string_set = set("Hello")

# print(list_set)
# print(tuple_set)
# print(string_set)

# numbers_with_duplicates = set([1, 2, 2, 3, 4, 4, 5])
# print(numbers_with_duplicates)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5,6}

# print(set1 | set2)  # Union
# print(set1 & set2)  # Intersection
# print(set1 - set2)  # Difference
# print(set1 ^ set2)  # Symmetric Difference

# customer_ids = {101,102,101,103,102,104,105,103}
# unique_customer_ids = set(customer_ids)
# print(f"We have {len(unique_customer_ids)} unique customers: {unique_customer_ids}")

in_stock = {"apple", "banana", "orange", "grape", "peach"}
to_reorder = {"banana", "peach", "kiwi", "melon"}
on_sale = {"apple", "orange", "melon", "grape"}

# Items that are in stock and on sale
print(f"These items are in stock and on sale: {in_stock & on_sale}")

# Items that need to be reordered but are not on sale
print(f"These items need to be reordered but are not on sale: {to_reorder - on_sale}")

#Check if all items on sale are in stock
if on_sale.issubset(in_stock):
    print("All items on sale are in stock.")
else:
    print("Not all items on sale are in stock.")

#Remove items from reorder list that are already in stock
updated_reorder = to_reorder - in_stock
print(f"Updated reorder list: {updated_reorder}")