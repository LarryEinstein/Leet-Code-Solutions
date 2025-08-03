users = [
    ("Alice",   "Zephyr",  29),
    ("Bob",     "Yellow",  35),
    ("Charlie", "Xenon",   22),
    ("David",   "Yellow",  40),
]

print(users[1])

sorted_users = sorted(users, key=lambda user:user[1])
print(sorted_users)