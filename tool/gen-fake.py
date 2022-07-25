import random
from faker import Faker

# Tool to generate fake content
# Range for pictures: 1-994

fake = Faker()


# getProfilePic: Get a Profile Picture for a person
getProfilePic = lambda x: f"https://boredhumans.b-cdn.net/faces2/{x}.jpg" if x in range(1,995) else f"err: not valud"

# getName: Generate a fake name
getName = lambda : fake.name()

print(getName())
print(getProfilePic(random.randint(1,995)))