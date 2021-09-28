wrong_sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
true_sentence = []

for i in wrong_sentence:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            true_sentence.append(f"'{int(i):02}'")
        else: true_sentence.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        true_sentence.append(i)


print(true_sentence)
print(" ".join(true_sentence))