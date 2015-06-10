import fresh_tomatoes
import media

# List of movie name instances
god_father = media.Movie("God Father",
                         "1972 American crime film",
                         "https://d12vb6dvkz909q.cloudfront.net/uploads/" +
                         "galleries/24681/the-godfather-1.jpg",
                         "https://www.youtube.com/watch?v=vdQi6Ebjm8c",
                         "Al Pacino",
                         "1972")
terminator = media.Movie("Terminator",
                         "1984 Scifi film",
                         "http://educatinggeeks.com/wp-content/" +
                         "uploads/2014/09/arnold_schwarzenegger_the_ter" +
                         "minator_1920x1080_55398.jpg",
                         "http://www.youtube.com/watch?v=-9ceRgWV8io",
                         "Arnold Schwarzenegger",
                         "1984")
matrix = media.Movie("Matrix",
                     "1999 American-Australian science fiction action film ",
                     "http://www.riskreversal.com/wp-content/" +
                     "uploads/2015/05/matrix_style_by_he4rty-d39qszq.jpg",
                     "https://www.youtube.com/watch2v=3PsUJFEBC74",
                     "Keanu Reeves",
                     "1999")
the_following = media.Movie("The following",
                            "A young writer who follows strangers" +
                            "meets a thief who takes him under his wing",
                            "http://upload.wikimedia.org/wikipedia/en" +
                            "/5/55/Following_film_poster.jpg",
                            "https://www.youtube.com/watch2v=c3sBBRxDAgk",
                            "Jeremy Theobald",
                            "1998")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "nostalgic screenwriter finds himself" +
                                "mysteriously going back to the 1920s every" +
                                "day at midnight",
                                "http://upload.wikimedia.org/wikipedia/" +
                                "en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch2v=atLg2wQ12mvu",
                                "Owen Wilson, Rachel McAdams",
                                "2011")
hunger_games = media.Movie("Hunger Games",
                           "Teenage hunger games story",
                           "http://upload.wikimedia.org/wikipedia/en/4/" +
                           "42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch2v=PbA63a7H0bo",
                           "Jennifer Lawrence",
                           "2008")
# Array of movie names
movies = [god_father, terminator, matrix, the_following,
          midnight_in_paris, hunger_games]
# This will generate html page with movies list
fresh_tomatoes.open_movies_page(movies)
