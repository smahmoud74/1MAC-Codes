def read_text():
    
    quotes = open("C:\Users\Sinan\Downloads\movie-quotes (1)\movie_quotes")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_text()
