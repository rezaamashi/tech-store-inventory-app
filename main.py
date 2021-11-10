from item import Item

item1 = Item("MyItem", 890)
item1.name = "SomeItem"

print(item1.read_only_name)

item1.read_only_name = "ZZZ"
