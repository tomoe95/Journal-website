from cs50 import SQL

db = SQL("sqlite:///data.db")


def calculator_feelings(feelings):
    feelings_dict = {}
    emoji = []
    numbers = []
    backgroundColor = []
    borderColor = []
    result = {}

    for feeling in feelings:
        # feeling['feeling'] <- get emoji (value) of dictionary ({'feeling' : 'emoji'})
        if feeling['feeling'] in feelings_dict:
            feelings_dict[feeling['feeling']] += 1
        else:
            feelings_dict[feeling['feeling']] = 1

    sorted_dict = {}
    for key, value in sorted(feelings_dict.items(), key=lambda x: (-x[1], x[0])):
        sorted_dict[key] = value

    for key, value in sorted_dict.items():
        emoji.append(key)
        numbers.append(value)
        if key == '😊':
            backgroundColor.append('rgba(255, 99, 132, 0.7)')
            borderColor.append('rgba(255, 99, 132, 1)')
        elif key == '😢':
            backgroundColor.append('rgba(54, 162, 235, 0.7)')
            borderColor.append('rgba(54, 162, 235, 1)')
        elif key == '😡':
            backgroundColor.append('rgba(255, 206, 86, 0.7)')
            borderColor.append('rgba(255, 206, 86, 1)')
        else:
            backgroundColor.append('rgba(75, 192, 192, 0.7)')
            borderColor.append('rgba(75, 192, 192, 1)')

    result = {
        'emoji': emoji,
        'numbers': numbers,
        'backgroundColor': backgroundColor,
        'borderColor': borderColor
    }
    return result
