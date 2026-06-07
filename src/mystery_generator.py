import random

victims = [
    "Professor Black",
    "CEO James Carter",
    "Dr Emily Stone",
    "Author Sarah Blake"
]

locations = [
    "Mansion",
    "Museum",
    "Luxury Hotel",
    "Train"
]

methods = [
    "Poison",
    "Knife",
    "Gunshot",
    "Electrocution"
]

suspects = [
    "Assistant",
    "Business Partner",
    "Neighbour",
    "Ex-Spouse",
    "Son"
]

victim = random.choice(victims)
location = random.choice(locations)
method = random.choice(methods)
killer = random.choice(suspects)

print("=== MURDER MYSTERY ===")
print(f"Victim: {victim}")
print(f"Location: {location}")
print(f"Method: {method}")
print(f"Killer: {killer}")