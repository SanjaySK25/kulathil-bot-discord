import requests, json

url = f'https://moviesdatabase.p.rapidapi.com/titles/search/keyword/avengers'

headers = {
    "X-RapidAPI-Key": "791581e205msh7192be2564e1b2fp14aee9jsn8ac3d2d98788",
    "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
json_response = response.json()

#embed = nextcord.Embed(title='Movie')
#embed.set_thumbnail(url=json_response['results'][0].primaryImage['url'])

#await interaction.response.send_message(embed=embed)

print(json_response['results'][0]['titleText']['text'])