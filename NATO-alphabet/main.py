import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phone_alpha = {value.letter:value.code for (key,value) in data.iterrows()}

# print(phone_alpha)
while True:
    word = input("Enter your text: ").upper()
    try:
        list = [phone_alpha[name] for name in word]
    except KeyError:
        print("sorry words only")
    else:
        print(list)
        break