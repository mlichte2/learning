from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Item("MyItem", 750, 6)

item1.send_email()

phone1 = Phone("iPhone 7", 1100, 2)
phone1.send_email()

keyboard1 = Keyboard('jscKeyboard', 400, 3)
keyboard1.apply_discount()
print(keyboard1.price)
