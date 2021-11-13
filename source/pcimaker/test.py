from quote_generator import *

q = RandomQuoteGenerator.load_quote("quotes.csv")
print(q.author+": "+q.text)


