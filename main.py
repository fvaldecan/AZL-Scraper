from AZL import getJSON
from pymongo import MongoClient
import time
from pprint import pprint
import json

artist = str(input('Enter Artist:\n'))
disc = getJSON(artist)
# Save discography as JSON
with open(artist + '.json', 'w') as fp:
    json.dump(disc, fp,  indent=4)

# db = client.get_database('Analyrics')
# artist_db = db.artists
# artists = ['2Pac'] #,'Joji','John Lennon', ,'Tupac','Kendrick Lamar','BROCKHAMPTON','Earl Sweatshirt','Beatles']
# for a in artists:
#     artist_json = getJSON(a)
#     artist_db.insert_one(artist_json)
#     time.sleep(120)
#     print ("End : %s" % time.ctime())
# artist_name = str(input("Enter Artist: "))
# obj = artist_db.find_one({'artist': 'Frank Ocean'})
# album_name = str(input("Enter Album: "))
# song_to_find = str(input("Enter Song: "))
# songs = {}
# song_lyrics = []
# for a in obj['albums']:
#     if(a['album_title'] == album_name):
#         songs = a['songs']
# for s in songs:
#     if(s['song_title' == song_to_find]):
#         song_lyrics = s['lyrics']
# pprint(song_lyrics)


