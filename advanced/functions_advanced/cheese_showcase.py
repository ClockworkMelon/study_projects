def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""

    for chees_name, pieces in sorted_data:
        result += f"{chees_name}\n"
        for piece in sorted(pieces, reverse=True):
            result += f"{piece}\n"

    return result

print(

sorting_cheeses(

Parmigiano=[165, 215],

Feta=[150, 515],

Brie=[150, 125]

)

)