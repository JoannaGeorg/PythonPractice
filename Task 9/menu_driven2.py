class Shop:
  def __init__(self):
    self.menu = {
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
    self.cart = {}

  def displayMenu(self):
    """
    This displays the Menu in the terminal.
    """
    print('\nMENU:')
    for index in self.menu:
      print(f'{index}: {self.menu[index]['name']} (${self.menu[index]['cost']})')

  def displayCart(self):
    """
    This diaplays the Cart in the terminal.
    """
    print('\nCART:')
    for item in self.cart:
      print(f'{self.menu[item]['name']}: ({self.cart[item]})')

  def addToCart(self, key, amount):
    """
    This adds an item and the amount to the cart.
    """
    if key not in self.cart:
      self.cart[key] = amount
    else:
      self.cart[key] += amount

  def calculateCost(self):
    """
    This Calculates the cost of the items in the cart.
    """
    cost = 0
    for item in self.cart:
      cost += (self.menu[item]['cost']) * (self.cart[item])
    return cost


shop = Shop()

is_shop = True
while is_shop:
  shop.displayMenu()
  item = int(input('\nEnter the index of the item to purchase: '))
  amount = int(input('Enter the number of copies: '))
  shop.addToCart(key=item, amount=amount)
  shop.displayCart()
  if input('\nWould you like to add more items? (Type "n" to finish): ') == 'n':
    is_shop = False

print(f"\nThe total cost = ${shop.calculateCost()}")