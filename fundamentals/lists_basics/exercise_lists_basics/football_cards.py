team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

given_cards = list(input().split())
new_list = []

card_list = []
player_list = []
team_names = ['A', 'B']
team_a_sent_away = []
team_b_sent_away = []

if given_cards is not None:
    for i in given_cards:
        card_list.append(i[0])
        player_list.append(i[2:])

for m, j in zip(card_list, player_list):
    j = int(j)
    if m == 'A' and j in team_a:
        team_a.remove(j)
        team_a_sent_away.append(j)
    elif m == 'B' and j in team_b:
        team_b.remove(j)
        team_b_sent_away.append(j)

    if len(team_a) < 7 or len(team_b) < 7:
        print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
        print(f'Game was terminated')
        break
else:
    print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')

