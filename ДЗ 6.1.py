with open("nginx_logs.txt", "r", encoding="utf-8") as my_list:
    content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in my_list)
    for i in content:
        print(i)

my_list.close()