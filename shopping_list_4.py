import os
# make a list to hold onto your items.
shopping_list = []


def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")


def show_help():
	clear_screen()
	# print out instructions on how to use the app
	print("What should we pick up at the store?")
	print("""
Enter 'DONE' to stop adding items
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
Enter 'REMOVE' to remove an item from your list.
""")


def show_list():
	clear_screen()
	print("Here's your list:")

	for index, item in enumerate(shopping_list, start=1):
		print("{}. {}".format(index, item))
	print("-" * 10)


def add_to_list(new_item):
	show_list()
	if len(shopping_list):
		position = input("Where shoud I add {}? \n"
						"Press ENTER to add to the end of the list \n"
						"> ".format(new_item))
	else:
		position = 0

	try:
		position = abs(int(position))
	except ValueError:
		position = None
	if position is not None:
		shopping_list.insert(position - 1, new_item)
	else:
		shopping_list.append(new_item)

	show_list()
	# print("Added {}. List now has {} items. ".format(new_item, len(shopping_list)))


def remove_from_list():
	show_list()
	item_to_remove = input('Which item would you like to remove?\n> ')
	try:
		shopping_list.remove(item_to_remove)
	except ValueError:
		print("The item {} was not found in your list.".format(item_to_remove))
		pass
	show_list()


show_help()

while True:
	# ask for new items
	new_item = input("> ")
	# be able to quit the app
	if new_item.upper() == "DONE" or new_item.upper() == 'QUIT':
		show_list()
		break
	elif new_item.upper() == "HELP":
		show_help()
		continue
	elif new_item.upper() == "SHOW":
		show_list()
		continue
	elif new_item.upper() == "REMOVE":
		remove_from_list()
		continue
	add_to_list(new_item)

