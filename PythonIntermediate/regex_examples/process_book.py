import re
import requests
the_idiot_url = 'https://www.gutenberg.org/files/2638/2638-0.txt'

def get_book(url):
    # Sends a http request to get the text from project Gutenberg
    raw = requests.get(url).text
    # Discards the metadata from the beginning of the book
    start = re.search(r"\*\*\* START OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*",raw ).end()
    # Discards the metadata from the end of the book
    stop = re.search(r"II", raw).start() # Read only till end of section I
    # Keeps the relevant text
    text = raw[start:stop]
    return text

# What is done in this method? What kind of pre-processing?
def preprocess(sentence):
    return re.sub('[^A-Za-z0-9.]+' , ' ', sentence).lower()

book = get_book(the_idiot_url)
processed_book = preprocess(book)
print(processed_book)

#Find the number of the pronoun "the" in the corpus
print("Pronoun 'The':",len(re.findall(r'the', processed_book)))
#convert every single stand-alone instance of 'i' to 'I' in the corpus
processed_book = re.sub(r'\si\s', " I ", processed_book)
print("Replaced i with I:",processed_book)
