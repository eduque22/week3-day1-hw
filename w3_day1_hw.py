##Exercise 1 - Filter out all the empty strngs from the list

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
new_places = list(filter(lambda name: True if name.strip() != '' else False, places))
print(new_places)


##Exercise 2 - Write an anonymous function that sorts this list by last name

def lname(name_list):
    name_list.sort(key=lambda x: x.split()[-1].lower())
    return name_list

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

print(lname(author))


##Exercise 3 - Convert the list below from Celsius to Faranheit, using map function with a lambda

# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

def fara(tup):
    x = tup[0]
    y = (9/5)*tup[1] + 32
    return (x, y)

print(list(map(fara, places)))

#unsuccessful lambda attempt
# places2 = list(map(lambda tup: (x=tup[0], y=(9/5)*tup[1]+32), places ))


##Exercise 4 - Create a generator function that individually returns each movie genre back from the list

genres = ["adventure", "drama", "horror", "comedy", "action", "romance"]

def movie(a_list, stop_item):
    for genre in a_list:
        yield genre 
        if genre == stop_item:
            break

pelicula = movie(genres, 'romance')
print(next(pelicula))
print(next(pelicula))
print(next(pelicula))
print(next(pelicula))
print(next(pelicula))
print(next(pelicula))
try:
    print(next(pelicula))
except:
    print('You are out of range. The object is empty.')