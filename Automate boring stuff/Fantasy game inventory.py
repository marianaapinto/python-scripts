stuff={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    total=0
    print ('Inventory:')
    for k, v in inventory.items():
        print (str(v)+ ' ' +k)
        total+=v
    print ('Total number of items: '+ str(total))

display_inventory(stuff)


def display_inventory1(inventory):
    total=0
    print ('Inventory:')
    for item in inventory:
        print (str(inventory[item]) + ' ' + item)
        total+=inventory[item]
    print ('Total number of items: '+ str(total))

display_inventory1(stuff)


def add_inventory(inventory, addeditems):
    for item in addeditems:
        inventory.setdefault(item, 0)
        inventory[item]=inventory[item]+1
    return inventory


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = add_inventory(stuff, dragonLoot)
display_inventory(stuff)
