class Actor:
    def __init__(self, actor_name):
        self.actor_name = actor_name

    def display(self):
        print("Actor:", self.actor_name)


class Director:
    def __init__(self, director_name):
        self.director_name = director_name

    def display(self):
        print("Director:", self.director_name)


class Movie(Actor, Director):
    def __init__(self, movie_title, actor_name, director_name):
        self.movie_title = movie_title
        Actor.__init__(self, actor_name)
        Director.__init__(self, director_name)

    def display(self):
        print("Movie Title:", self.movie_title)
        super().display()
        Director.display(self)
m = Movie("Inception", "Leonardo DiCaprio", "Christopher Nolan")
m.display()
