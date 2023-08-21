string1 = "I like %s" % "Python"
print(string1) # 'I like Python'

temp = "Educative"
string2 = "I like %s" % temp
print(string2) # 'I like Educative'

string3 = "I like %s and %s" % ("Python", temp)
print(string3)  # 'I like Python and Educative'
my_string = "%i + %i = %i" % (1,2,3)
print(my_string) # '1 + 2 = 3'
string1 = "%f" % (1.11)
print(string1) # '1.110000'

string2 = "%.2f" % (1.11)
print(string2) # '1.11'

string3 = "%.2f" % (1.117)
print(string3) # '1.12'