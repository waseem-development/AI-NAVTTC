import random as rdm
print(rdm.random()) # Returns a random value between 0.0 - 1.0 (floating value)
print(rdm.randint(1, 100)) # Returns a random value between a and b including both a and b (integer value)
print(rdm.randrange(0, 10)) # Like range(), but returns one random value
print(rdm.randrange(0, 10, 2)) # with steps
colors = ["red", "green", "blue"]
print(rdm.choice(colors)) # colors = ["red", "green", "blue"]
myStr = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*_+-."
k = None
import random
rdm = random
print(rdm.random()) # Returns a random value between 0.0 - 1.0 (floating value)
print(rdm.randint(1, 100)) # Returns a random value between a and b including both a and b (integer value)
print(rdm.randrange(0, 10)) # Like range(), but returns one random value
print(rdm.randrange(0, 10, 2)) # with steps
colors = ["red", "green", "blue"]
print(rdm.choice(colors)) # colors = ["red", "green", "blue"]
myStr = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*_+-."
print(''.join(rdm.choices(myStr, k=1000))) # Returns a list of k random elements (with repetition)
print(rdm.sample(myStr, k=10))
cards = [1, 2, 3, 4, 5]
rdm.shuffle(cards) # Shuffles a list in-place
print(cards)
print(random.uniform(1.5, 3.5)) # Returns a random float between a and b

rdm.seed(10)
print(rdm.randint(1, 10))