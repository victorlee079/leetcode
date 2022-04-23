"""
Design a TinyURL Service
1. Number of URL serves
2. 62 characters can be used [A-Za-z0-9] and 62^n URLs can be served (n = number of characters)
    e.g. If n = 7, 62^7 ~= 3500 billions URLs

Basic Solution:
(ID, Original URL)
Example: https://tinyurl.com/Ab123X2 for https://www.google.com
    ID = Ab123X2 and URL = https://www.google.com
Problem:
hash collisions, in which 2 long urls map to the same short url

Better Solutions:
(ID, Original URL, Short URL)
ID int PRIMARY_KET AUTO_INCREMENT

ID can be used to do the conversion

Get shortened URL

hash original URL string to 2 digits as hashed value hash_val

use hash_val to locate machine on the ring

insert original URL into the database and use getShortURL function to get shortened URL short_url

Combine hash_val and short_url as our final_short_url (length=8) and return to the user

Retrieve original from short URL

get first two chars in final_short_url as hash_val

use hash_val to locate the machine

find the row in the table by rest of 6 chars in final_short_url as short_url

return original_url to the user

"""
from random import choices


class Codec:
    def __init__(self):
        self.long_short = {}
        self.short_long = {}
        self.alphabet = "abcdefghijklmnopqrstuvwzyz"

    def encode(self, longUrl):
        while longUrl not in self.long_short:
            code = "".join(choices(self.alphabet, k=6))
            if code not in self.short_long:
                self.short_long[code] = longUrl
                self.long_short[longUrl] = code
        return 'http://tinyurl.com/' + self.long_short[longUrl]

    def decode(self, shortUrl):
        return self.short_long[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))