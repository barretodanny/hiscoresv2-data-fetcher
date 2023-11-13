from scores import fetchUserScores, saveUserScores
from users import fetchUsers

ENDPOINT                    = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player="
IRONMAN_ENDPOINT            = "https://secure.runescape.com/m=hiscore_oldschool_ironman/index_lite.ws?player="
HARDCORE_IRONMAN_ENDPOINT   = "https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/index_lite.ws?player="
ULTIMATE_IRONMAN_ENDPOINT   = "https://secure.runescape.com/m=hiscore_oldschool_ultimate/index_lite.ws?player="

LOCAL_ENPOINT               = "http://localhost:8000/api/users/"

users = fetchUsers(LOCAL_ENPOINT)
print(f"Fetching scores for the following users: {[user['username'] for user in users]}")

for user in users:
    username = user["username"]
    gamemode = user["gameMode"]

    print(username, gamemode)
    endpoint = ""
    if gamemode == "normal":
        endpoint = ENDPOINT
    elif gamemode == "ironman":
        endpoint = IRONMAN_ENDPOINT
    elif gamemode == "hardcore_ironman":
        endpoint = HARDCORE_IRONMAN_ENDPOINT
    elif gamemode == "ultimate_ironman":
        endpoint = ULTIMATE_IRONMAN_ENDPOINT
    
    scores = fetchUserScores(endpoint, username)
    print("Saving score...")
    saveUserScores("http://localhost:8000/api/scores/", username, gamemode, scores)

