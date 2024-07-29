name_address = "Yaron Brand Pardesiya"

#a.
print(f"a. The length of the string is {len(name_address)}")
#b.
print(f"b. The string in upper cases is {name_address.upper()}")
#c.
print(f"c. The string in lower cases is {name_address.lower()}")
#d.
print (f"d. Does the string starts with my name? {name_address.startswith("Yaron")}")
#e.
print (f"e. Does the string ends with the location I live in? {name_address.endswith("Pardesiya")}")
#f.
print (f"f.{name_address.split()}")
#g.
new_name_address = name_address.replace(" ","*")
print(f"g. new list is {new_name_address.split()}")
#h.
print(f"h. {name_address.center(50 , "=")}")
#i.
print(f"i. {name_address[3:]}")
#j.
print(f"j. {name_address[:4]}")
#k.
print(f'k. {name_address[1::2]}')
#l.
print (f"l. {name_address.title()}")