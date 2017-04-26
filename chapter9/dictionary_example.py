players = dict(
    Messi='forward',
    Pique='Defender',
    Xavi='Midfielder',
    Valdez='Goalie')

for key in players:
    print(f"FCBarcelona player: {key}")

print("____")

for key in players:
    print("{} plays as a {}".format(key, players[key]))

# will return everything in dictionary
print(players.items())


for [k, v] in players.items():
    print("Name: {}, Position: {}".format(k, v))


print(players.get('Neymar', 'Player not in list yet'))
print(players.get('Messi', 'player exist in list'))

player = players.pop('Valdez', 'Not a player')
print(players.items())
# add 
players['Valdez'] = player
print(players.items())
