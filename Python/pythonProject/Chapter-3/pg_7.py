user_name = input("Enter your name: ")
user_partner_name = input("Enter your name: ")

combine_name = user_name + user_partner_name

lowercase_name = combine_name.lower()

T = lowercase_name.count('t')
R = lowercase_name.count('r')
U = lowercase_name.count('u')
E = lowercase_name.count('e')

true = T+R+U+E

l = lowercase_name.count('l')
o = lowercase_name.count('o')
v = lowercase_name.count('v')
e = lowercase_name.count('e')

love = l+o+v+e

love_score = int(str(true)+ str(love))

if love_score < 20 or (50 < love_score < 80):
    print(f"your score is {love_score}. Your relationship has its unique dynamics.")
elif 30 < love_score <= 40:
    print(f"your score is {love_score}. You and your partner complete each other.")
else:
    print(f"your score is {love_score}.")