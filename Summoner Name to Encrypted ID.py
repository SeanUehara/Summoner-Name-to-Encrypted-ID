import json, requests

PlayerNameList = input("List of names separated by commas:\n")
PlayerNameList = PlayerNameList.replace(" ", "")
PlayerNameList = PlayerNameList.split(",")

PlayerIDList = ""
for Player in PlayerNameList:
    url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{Player}?api_key=RGAPI-1464e067-1b2a-4868-8cae-3bf5549fefef"

    try:
        response = requests.get(url)
        response.raise_for_status()
        Data = json.loads(response.text)
        PlayerIDList += Data['accountId']
        PlayerIDList += ', '

    except:
        print(Player + " does not exist.")

print(PlayerIDList)
