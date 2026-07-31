player_statistics = {}

while True:
    player_info = input()

    if player_info == "Season end":
        break

    if "->" in player_info:
        player, position, skill = player_info.split(" -> ")
        skill = int(skill)

        if player not in player_statistics:
            player_statistics[player] = {}

        if position not in player_statistics[player]:
            player_statistics[player][position] = 0

        if skill > player_statistics[player][position]:
            player_statistics[player][position] = skill

    elif "vs" in player_info:
        player_one, player_two = player_info.split(" vs ")

        if (player_one and player_two) in player_statistics.keys():
            player_one_positions = [position for position in player_statistics[player_one].keys()]
            player_two_positions = [position for position in player_statistics[player_two].keys()]

            common_position = ''

            for position in player_one_positions:
                if position in player_two_positions:
                    common_position = position

            if common_position:
                if player_statistics[player_one][common_position] > player_statistics[player_two][common_position]:
                    del player_statistics[player_two]
                elif player_statistics[player_two][common_position] > player_statistics[player_one][common_position]:
                    del player_statistics[player_one]

sorted_by_total_skill = dict(sorted(player_statistics.items(), key=lambda v: sum(v[1].values()), reverse=True))

for player in sorted_by_total_skill:
    print(f"{player}: {sum(sorted_by_total_skill[player].values())} skill")
    sorted_by_position = dict(sorted(sorted_by_total_skill[player].items(), key=lambda ps:(-ps[1], ps[0])))
    for position, skill in sorted_by_position.items():
        print(f"- {position} <::> {skill}")

