from cs50 import SQL

db = SQL("sqlite:///data.db")


def calculator_feelings(user_id):
    feelings_dict = {}
    feelings = db.execute(
        "SELECT feeling FROM journals WHERE user_id = ? ORDER BY date desc"
        ,user_id)

    for feeling in feelings:
        print(feeling['feeling'])
        if feeling['feeling'] in feelings_dict:
            feelings_dict[feeling['feeling']] += 1
        else:
            feelings_dict[feeling['feeling']] = 1
            
    return feelings_dict
