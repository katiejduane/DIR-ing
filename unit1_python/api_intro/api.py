import requests # makes API requests (this is a third-party module)
import json # convert the API data into python dictionaries and arrays
import time # module for working with timestamps

# variables for grabbing our data
URL = "https://www.anapioficeandfire.com/api/characters?page=%d&pageSize=100"
DELAY = 1
OUTPUT = 'got-2.json'

chars = []
clean_chars = []

# Make Requests to the API for character data
for page in range(1, 50):
    print('Making request for page %d' % page)
    r = requests.get(URL % page)
    new_chars = r.json()
    if len(new_chars) == 0:
        break
    chars.extend(new_chars)
    print('Sleeping...\n\n')
    time.sleep(DELAY)

# Only people with names
for char in chars:
    if len(char['name']) > 0:
        clean_chars.append(char)

print('Got %d characters!' % len(clean_chars))

# with open(OUTPUT, 'w') as f:
#     print('Writing to file...')
#     f.write(json.dumps(clean_chars))

##### do stuff with clean_chars variable
print("You got %d characters back from the API" % len(clean_chars))



