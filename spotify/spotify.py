import csv
import json

csv_file_name = 'spotify/spotify.csv'
json_file_name = 'spotify/songs.json'

songs_list = []

with open(csv_file_name, 'r', encoding='UTF8') as data_file:
    for row in csv.DictReader(data_file):
        songs_list.append(row)

with open(json_file_name, 'w', encoding='UTF8') as json_file:
    json.dump(songs_list, json_file, indent=4)

#UZDEVUMS 1
#Lai programma izvada terminālī tikai dziesmas nosaukumus

for song in songs_list:
    print(f"{song['Title']} ({song['Popularity']})")


years = []

for song in songs_list:
    if song['Year'] not in years: 
        years.append(song['Year'])

print(years)