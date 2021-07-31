from database import create_table, add_entry, get_entries

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.


Your selection: """
welcome = "Welcome to the programming today!"



# entries = [
#     {"content": "Today I started learning programming.", "date": "01-01-2020"},
#     {"content": "I created my first SQLite database!", "date": "02-0102020"},
#     {"content": "I finished writing my programming diary application.", "date": "03-01-2020"},
#     {"content": "Today I'm going to learning programming", "date": "04-01-2020"},
#
# ]


def prompt_new_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")

    add_entry(entry_content, entry_date)

def view_entry(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


print(welcome)
create_table()

while (user_input := input(menu)) != "3":
    # we'll deal with user input here...
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entry(get_entries())
    else:
        print("Invalid option, please try again!")
