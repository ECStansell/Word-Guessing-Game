#import random to select a word from each category
import random
import main

#one wordlist per category
birds = ["parrot", "cardinal", "crow", "eagle", "flamingo", "chicken", "hummingbird", "duck", "sparrow", "raven"]

fishes = ["angelfish", "carp", "salmon", "tuna", "goldfish", "halibut", "trout", "catfish", "bass", "lionfish"]

animals = ["mouse", "ferret", "gorilla", "wolf", "giraffe", "ocelot", "lemur", "antelope", "bear", "horse"]


#one function to randomly select a word from each category
def get_random_bird():
  bird = random.choice(birds)
  birds.remove(bird)
  if not birds:
    print()
    print("There are no more birds.")
    birds.append(bird)
    main.game_choice()
  return bird

def get_random_fish():
  fish = random.choice(fishes)
  fishes.remove(fish)
  if not fishes:
    print()
    print("There are no more fish.")
    fishes.append(fish)
    main.game_choice()
  return fish

def get_random_animal():
  animal = random.choice(animals)
  animals.remove(animal)
  if not animals:
    print()
    print("There are no more animals.")
    animals.append(animal)
    main.game_choice()
  return animal