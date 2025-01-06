from cs50 import SQL

db = SQL("sqlite:///data.db")
def calculator_feelings(user_id):
    feelings_data = {}
    feelings = db.execute("SELECT feeling FROM journals WHERE user_id = ? ORDER BY date desc", user_id)
    for feeling in feelings:
        if feeling in feelings_data:
            feelings_data[feeling] += 1
        else:
            feelings_data[feeling] = 1

    return feelings_data
