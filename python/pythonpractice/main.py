from movie import Movie
from random import *
import numpy as np

def create_movie_list(): 
   movies = [
      Movie("Star Trek", 2009, 156),
      Movie("Justice League", 2017, 115),
      Movie("Batman Returns", 2001, 245),
      Movie("War Games", 1983, 176)
   ]
   return movies

def main():
   print("\n ================= PART ONE ===================")
   m = Movie("Star Trek", 2009, 137)
   print(m)
   hrs, min = m.getRuntime()
   print("{}:{}".format(hrs,min))

   print("\n ================= PART TWO ===================")

   movies = create_movie_list()
   for movie in movies:
      print(movie)
   print("")

   long = [ m for m in movies if m.runtime > 150 ]

   for movie in long:
      print(movie)
   print("")

   dic = {}
   for movie in movies:
      dic[movie.title] = round(uniform(0,5.0),2)

   for movie, rating in dic.iteritems():
      print "Movie:", movie, ", Rating:", rating

   print("\n ================ PART THREE ==================")

   numpyarr = get_movie_data()
   print "Number of rows:", len(numpyarr)
   print "Number of cols:", len(numpyarr[0])
   print ""

   first2 = numpyarr[0:3]
   for item in first2:
      print "Movie-ID:", int(item[0])
      print "Views:",    int(item[1])
      print "Stars:",    round(item[2],2)
      print ""

   for item in first2:
      data = item[-2:]
      print "Views:",    int(data[0])
      print "Stars:",    round(data[1],2)
      print ""

   oneD = []
   for data in numpyarr:
      oneD.append(int(data[1]))

   print oneD

def get_movie_data():
    """
    Generate a numpy array of movie data
    :return:
    """
    num_movies = 10
    array = np.zeros([num_movies, 3], dtype=np.float)

    random = Random()

    for i in range(num_movies):
        # There is nothing magic about 100 here, just didn't want ids
        # to match the row numbers
        movie_id = i + 100

        # Lets have the views range from 100-10000
        views = random.randint(100, 10000)
        stars = random.uniform(0, 5)

        array[i][0] = movie_id
        array[i][1] = views
        array[i][2] = stars

    return array

main()
