party_size = int(input())
hero_list = {}

for hero in range(party_size):
    hero_name, health, mana = input().split()
    hero_list[hero_name] = {"HP": int(health), "MP": int(mana)}

commands = input()

while commands != "End":
    commands = commands.split(" - ")
    action = commands[0]
    hero = commands[1]

    if action == "CastSpell":
        mana_needed = int(commands[2])
        spell_name = commands[3]
        mana_left = hero_list[hero]["MP"] - mana_needed
        if mana_left >= 0:
            hero_list[hero]["MP"] -= mana_needed
            print(f'{hero} has successfully cast {spell_name} and now has {mana_left} MP!')
        else:
            print(f'{hero} does not have enough MP to cast {spell_name}!')
    elif action == "TakeDamage":
        damage = int(commands[2])
        attacker = commands[3]
        health_left = hero_list[hero]["HP"] - damage
        if health_left > 0:
            hero_list[hero]["HP"] -= damage
            print(f'{hero} was hit for {damage} HP by {attacker} and now has {health_left} HP left!')
        else:
            del hero_list[hero]
            print(f'{hero} has been killed by {attacker}!')
    elif action == 'Recharge':
        amount = int(commands[2])
        if hero_list[hero]["MP"] + amount > 200:
            mana_recovered = 200 - hero_list[hero]["MP"]
            hero_list[hero]["MP"] = 200
            print(f'{hero} recharged for {mana_recovered} MP!')
        else:
            hero_list[hero]["MP"] += amount
            print(f'{hero} recharged for {amount} MP!')
    elif action == 'Heal':
        amount = int(commands[2])
        if hero_list[hero]["HP"] + amount > 100:
            health_recovered = 100 - hero_list[hero]["HP"]
            hero_list[hero]["HP"] = 100
            print(f'{hero} healed for {health_recovered} HP!')
        else:
            hero_list[hero]["HP"] += amount
            print(f'{hero} healed for {amount} HP!')

    commands = input()

for hero, hero_stats in hero_list.items():
    health = hero_stats["HP"]
    mana = hero_stats["MP"]
    print(f'{hero}')
    print(f'  HP: {health}')
    print(f'  MP: {mana}')