#Downloading an Image
import requests
#stream is set to True, the data will be read as it arrives in whatever size of chunks
# are received as and when they are
req = requests.get('https://robots.net/wp-content/uploads/2019/11/Lozingle_10032014-1280x720.jpg', stream=True)
req.raise_for_status()
with open('resources/python.jpg', 'wb') as fd:
    #it is recommended that you download a file in pieces or chunks using the iter_content(chunk_size = 1) method.
    for chunk in req.iter_content(chunk_size=500):
    #this method iterates over the response data in chunk_size number of bytes at once.
    # And when the stream=True has been set on the request, this method will avoid
    # reading the whole file into memory at once for just the large responses
        print('Received a Chunk')
        fd.write(chunk)

#When chunk_size is set to None and stream is set to True, the data will be read as it
# arrives in whatever size of chunks are received as and when they are.