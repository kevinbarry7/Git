want_cake = "yes"
have_cake = "yes"

if want_cake == 'yes':
    print("We want cake...")
    if have_cake == 'no':
        print("But we don't have any cake")
    elif have_cake == 'yes':
        print("And it's our lucky day")
else:
    print("The cake is a lie")


word = input("Please enter a word to be tested for length: ")

if len(word) > 5:
    print("The word that you entered is greater than 5 characters!!")
elif len(word) < 5:
    print("The word that you entered is less than 5 characters!!")
else:
    print("The word you entered is exactly 5 characters in length!!")

