#have a HELP command
#have a SHOW command
#Code refactoring

#have a HELP command
def show_help():
    #print out instuctions on how use app
    print("what should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items
    Enter 'SHOW' to stop adding items
    Enter 'HELP' to stop adding items
    """)

#have a SHOW command
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        #print out the list
        print(item)

def add_to_list(new_item):
    #add new items to out list
    shopping_list.append(new_item)
    print("Added {}. List has {} items.".format(new_item, len(shopping_list)))

#make a list to hold onto our items
shopping_list = []

show_help()

while True:
    #ask for new items
    new_item = input("> ")
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)
show_list()

#be able to quit the app
