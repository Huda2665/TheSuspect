import random
import json

with open("data/victims.json") as f:
    victims = json.load(f)

with open("data/locations.json") as f:
    locations = json.load(f)

with open("data/methods.json") as f:
    methods = json.load(f)

with open("data/suspects.json") as f:
    suspects = json.load(f)

with open("data/motives.json") as f:
    motives = json.load(f)

with open("data/clues.json") as f:
    clues = json.load(f)

victim = random.choice(victims)
location = random.choice(locations)
method = random.choice(methods)

chosen_suspects = random.sample(suspects, 4)

killer = random.choice(chosen_suspects)

motive = random.choice(motives)

chosen_clues = random.sample(clues, 3)

print("\n=== THE SUSPECT ===\n")

print("Victim:", victim)
print("Location:", location)
print("Method:", method)

print("\nSuspects:")
for suspect in chosen_suspects:
    print("-", suspect)

print("\nKiller:")
print("-", killer)

print("\nMotive:")
print("-", motive)

print("\nClues:")
for clue in chosen_clues:
    print("-", clue)