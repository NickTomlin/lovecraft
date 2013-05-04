title: The Wonderful World of Clases
category: It's A category from the post!
fruitbat: FRUITBAT
---

Still trying to understand Python classes. Getting a little closer:
[summary](http://stackoverflow.com/a/8609238/1048479)

```Python
# A simple class
class Dog:
    def __init__(self, legs, color):
        self.legs = legs
        self.color = color

    def bark(self):
        return "woof,  I'm a %s colored dog with %s legs" % (self.color, self.legs)

fido = Dog(4, 'brown')

print(fido.bark())


class Shitzu(Dog):
    def barf(self):
        return 'Bluaghhh'

ringo = Shitzu(4,'blue')  # <-- how does this assignment work if we add extra parameters in a class?
print('%s : %s' % (ringo.bark(), ringo.barf()))
```