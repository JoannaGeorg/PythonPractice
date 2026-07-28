menu = {
  1: {
    'name': 'Bag',
    'cost': 20.5
  },
  2: {
    'name': 'Pen',
    'cost': 0.5
  },
  3: {
    'name': 'Book',
    'cost': 10.0
  },
  4: {
    'name': 'Pencil',
    'cost': 0.25
  },
  5: {
    'name': 'Bottle',
    'cost': 15.75
  }
}
cart = {}

def displayMenu(menu):
  print('\nMENU:')
  for index in menu:
    print(f'{index}: {menu[index]['name']} (${menu[index]['cost']})')

def displayCart():
  print('\nCART:')
  for item in cart:
    print(f'{menu[item]['name']}: ({cart[item]})')

def addToCart(key, amount):
  if key not in cart:
    cart[key] = amount
  else:
    cart[key] += amount

def calculateCost():
  cost = 0
  for item in cart:
    cost += (menu[item]['cost']) * (cart[item])
  return cost


is_shop = True
while is_shop:
  displayMenu(menu)
  item = int(input('Enter the index of the item to purchase: '))
  amount = int(input('Enter the number of copies: '))
  addToCart(key=item, amount=amount)
  displayCart()
  if input('Would you like to add more items? (n): ') == 'n':
    is_shop = False

print(f"The total cost = ${calculateCost()}")
