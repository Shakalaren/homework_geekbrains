from itertools import zip_longest
from json import dump

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:

        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)
            with open("final.json", "w", encoding="utf-8") as f:
                all_list = zip_longest((" ".join(us.split(",")) for us in users), hobby, fillvalue=None)
                result = {str(el[0]).strip(): str(el[1]).strip() for el in all_list}

                dump(result, f, ensure_ascii=False, indent=4)
            print(result)
        else:
            exit(1)