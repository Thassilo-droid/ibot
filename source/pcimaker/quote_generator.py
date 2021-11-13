import random

class Quote:

    def __init__(self, author, text):
        self.author, self.text = author, text


class RandomQuoteGenerator:

    @staticmethod
    def load_quote(filename):

        if filename.endswith(".csv"):
            #csv file

            with open(filename, "r") as f:

                quotes = f.readlines()[1:]



            authors = [el.split(",")[0] for el in quotes]
            quotes = [el.split(",")[1] for el in quotes]

            random_number = random.randrange(0, len(authors))

            return Quote(authors[random_number], quotes[random_number])

    
