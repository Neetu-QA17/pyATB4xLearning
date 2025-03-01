# tuple within tuple

hero1 = ("Batman", "Bruce")
hero2 = ("WonderLand", "DianaPrince")

new_tuple = (hero1,hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[0][0])    # if I want only the 1st item from the 1st tuple
print(new_tuple[1][1])