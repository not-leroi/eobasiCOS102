#Returs false as game_1 not equal to game_2
game_1 = 2
game_2 = 4
print(bool(game_1 == game_2))
#or
print(game_1 == game_2)

#Returns false as val is None
val =None
print(bool(val))

#Returns false as num is an empty sequence
num = ()
print(bool(num))

#Returns true as age is boolean
age = True
print(bool(age))