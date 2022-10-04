# Challenge 1: Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.

class Player:
    def __init__(self, player_info):
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.postion = player_info["position"]
        self.team = player_info["team"]

# Ninja Bonus: Add a @class method called get_team(cls, team_list) that, given a list of dictionaries, populates and returns a new list of Player objects. Be sure to test your method!
    @classmethod
    def get_team(cls, team_list):
        new_team =[]
        for player_dict in team_list:
            new_team.append(cls(player_dict))
        return new_team

# Unsure about how to test this class method to see if is working?? 


kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

# Challenge 2 Given these variables, create Player instances for each of the above dictionaries.

player_Kevin = Player(kevin)
print(player_Kevin)

player_Jason = Player(jason)
print(player_Jason)

player_Kyrie = Player(kyrie)
print(player_Kyrie)


# Challenge 3 Finally, given the example list of players below. Write a for loop that will populate an empty list with Player objects from the original list of dictionaries.

# new_team = []

players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "Ralph", 
    "age":16, 
    "position": "Power Foward", 
    "team": "Boston Celtics"
    }
]

# for loop over the list of dict's, each time use the dictionary info to create a new player. Then add the new player to the emplty new team list.

# for player_dict in players:
#     player = Player(player_dict)
#     new_team.append(player)
