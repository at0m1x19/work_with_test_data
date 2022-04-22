from csv import DictReader
from json import load, dump

books_list = []
users_list = []
needed_fields_of_user = ['name', 'gender', 'address', 'age']

with open('books.csv', newline='') as file:
    reader = DictReader(file)

    for row in reader:
        del row['Publisher']
        lowercase_keys_row = {key.lower(): value for key, value in row.items()}
        books_list.append(lowercase_keys_row)

with open('users.json', newline='') as file:
    reader = load(file)

    for user in reader:
        user_with_needed_fields = {key: user[key] for key in user if key in needed_fields_of_user}
        user_with_sorted_fields = {key: user_with_needed_fields[key] for key in needed_fields_of_user}
        user_with_sorted_fields['books'] = []
        users_list.append(user_with_sorted_fields)


    def endless_gen(args):
        while True:
            for el in args:
                yield el


    endless_users_list = endless_gen(users_list)

    for book in books_list:
        next(endless_users_list)['books'].append(book)

with open('result.json', 'w') as file:
    dump(users_list, file, indent=4)
