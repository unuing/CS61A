class Pet():
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')


# Question 4.1
# Below is a skeleton for the Cat class, which inherits from the Pet class.
# To complete the implementation, override the init and talk methods and add
# a new lose_life method.
# Hint: You can call the init method of Pet to set a cat’s name and owner.

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives

    def talk(self):
        """ Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print("{0} says meow!".format(self.name))

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        if self.lives == 0:
            print("{0} has no more lives to lose!".format(self.name))
            return
        self.lives -= 1
        self.is_alive = (self.lives == 0)


# Question 4.2
# More cats! Fill in this implemention of a class called NoisyCat, which is just like a
# normal Cat. However, NoisyCat talks a lot – twice as much as a regular Cat!

class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""
    # def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        # No, it isn't.

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        Cat.talk(self)
        Cat.talk(self)