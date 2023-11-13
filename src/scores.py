import requests
from utils import categories


# fetches scores from osrs api
# scores are newline separated for each category
# each category is comma separated for each value (rank,score,exp)
def fetchUserScores(endpoint, username):
    response = requests.get(f"{endpoint}{username}")

    if (response.status_code == 404):
        print(f"USER NOT FOUND WITH USERNAME {username}")
        return
    
    return response.text


# save each score attached to a user, the user's gamemode, and the category
def saveUserScores(endpoint, username, gamemode, scores):
    for index, score in enumerate(scores.split("\n")):
        if (not score):
            break

        category = categories[index]
        # `score` in the form (rank,score,exp), exp is optional
        score_parts = score.split(",") 

        # do not save score if user has no ranking
        if (score_parts[0] == "-1"):
            continue

        body = {}
        body["username"] = username
        body["gameMode"] = gamemode
        body["categoryName"] = category 
        body["rank"] = score_parts[0]
        body["score"] = score_parts[1]

        if len(score_parts) > 2:
            body["exp"] = score_parts[2]
            
        requests.post(f"{endpoint}", json=body)