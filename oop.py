def calculate_scoreboard(participants):

    # Create an empty list to store each participant's name and score
    scoreboard = []

    for participant in participants:
        # Calculate the score for each participant based on the points for each food
        score = (participant["chickenwings"] * 5) + (participant["hamburgers"] * 3) + (participant["hotdogs"] * 2)

        # Append the participant's name and score to the scoreboard list
        scoreboard.append({"name":participant["name"], "score": score})

    # Sort the scoreboard list by score in descending order and then by name alphabetically
    scoreboard = sorted(scoreboard, key=lambda k: (-k["score"], k["name"]))

    # Return the final scoreboard
    return scoreboard


participants = [
    {"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
    {"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}

]
print(calculate_scoreboard(participants))