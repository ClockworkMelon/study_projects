def loading_bar(n: int):
    load_progress = n // 10
    bar = []
    for i in range(12):
        if i == 0:
            bar.append('[')
        elif i == 11:
            bar.append(']')
        elif 1 <= i < load_progress + 1:
            bar.append('%')
        else:
            bar.append('.')
    return "".join(bar)

percent_loaded = int(input())

bar_ = loading_bar(percent_loaded)

if bar_.count("%") == 10:
    print(f'100% Complete!')
    print(bar_)
else:
    print(f'{percent_loaded}% {bar_}')
    print(f'Still loading...')