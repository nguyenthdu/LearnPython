#TODO: Giá trị trong tuple không thay đổi được
car = ("Ford", "Raptor", 2019, "Red")
print(car)

# Length
print(len(car))

# Indexing
print(car[1])

# Slicing
print(car[2:])

print("===========================")
#TODO: Gộp Tuple
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = hero1 + hero2
print(awesome_team)

print("=====================")
#TODO: Tuple lồng nhau
hero3 = ("Batman", "Bruce Wayne")
hero4 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero3, hero4)
print(awesome_team)
print("=========================")
#TODO: Tìm kiếm tuple
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Moscow" in cities)
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities.index("Tokyo"))