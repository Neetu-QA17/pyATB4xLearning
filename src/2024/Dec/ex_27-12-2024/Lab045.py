my_shopping_list = ["milk", "oats", "bread", "butter"]
# to remove duplicate from the list we can use SET
print(my_shopping_list[0])  # access 1st element from the list
print(len(my_shopping_list)) # get the length of the list

# we can also pass the list in a function as below

def bring_more_food(my_list):
    more_item = input("Enter the item\n")
    my_list.append(more_item)  # add item to the list using append function
#    my_list.remove(more_item)       # remove item from the list using remove function
    my_list.insert(0, more_item)  # insert the item at a specific location using insert function
    return my_list

l = bring_more_food(my_shopping_list)
print(l)
