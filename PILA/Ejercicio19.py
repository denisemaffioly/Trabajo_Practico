class Movie:
    def __init__(self, title, studio, year):
        self.title = title
        self.studio = studio
        self.year = year

class Peliculas:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("La pila está vacía")

    def size(self):
        return len(self.items)

    def get_movies_by_year(self, year):
        movies = []
        for movie in self.items:
            if movie.year == year:
                movies.append(movie.title)
        return movies

    def count_movies_by_year(self, year):
        count = 0
        for movie in self.items:
            if movie.year == year:
                count += 1
        return count

    def get_marvel_movies_by_year(self, year):
        movies = []
        for movie in self.items:
            if movie.studio == "Marvel Studios" and movie.year == year:
                movies.append(movie.title)
        return movies


peliculas = Peliculas()

peliculas.push(Movie("Rapidos y Furiosos 7", "Original Film One Race Films", 2014))
peliculas.push(Movie("Guardianes de la Galaxia", "Marvel Studios", 2014))
peliculas.push(Movie("Captain America: Civil War", "Marvel Studios", 2016))
peliculas.push(Movie("Black Panther", "Marvel Studios", 2018))
peliculas.push(Movie("Campeones", "Universal Studios", 2018))
peliculas.push(Movie("Misterio a Bordo", "Happy Madison", 2018))

movies_2014 = peliculas.get_movies_by_year(2014)
print("Películas estrenadas en 2014:")
for movie in movies_2014:
    print(movie)

count_2018 = peliculas.count_movies_by_year(2018)
print("Cantidad de películas estrenadas en 2018:", count_2018)

marvel_movies_2016 = peliculas.get_marvel_movies_by_year(2016)
print("Películas de Marvel Studios estrenadas en 2016:")
for movie in marvel_movies_2016:
    print(movie)