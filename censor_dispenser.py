# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def censor(x):
    r = ''
    for i in range(len(x)):
        r += '#'
    return r


new_one = email_one.replace('learning algorithms', '***')
# print(new_one)

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]


def censor_words(email):
    for i in proprietary_terms:
        word = ''
        for j in i:
            if j == ' ':
                word += " "
            else:
                word += '#'
        email = email.replace(i, word)
    return email


# print(censor_words(email_two))

def censor_negative(email, no = 2):
    for i in negative_words:

        if email.count(i) >= no:
            word = ''
            for j in i:
                if j == ' ':
                    word += " "
                else:
                    word += '#'
            email.replace(i, word)
    return email


# print(censor_negative(email_three))

def ulcensor(email):

    ulist = proprietary_terms + negative_words
    nemail = censor_words(email)
    nemail = censor_negative(nemail, 0)
    em = nemail.split()
    print(nemail)
    i = 0
    while i < len(em):
        if '#' in em[i]:

            if i == 0:

                em[i + 1] = censor(em[i + 1])

            elif i == len(em) - 1:

                em[i - 1] = censor(em[ i - 1])
            else:

                em[i - 1] = censor(em[i - 1])
                em[i + 1] = censor(em[i + 1])
            i += 2
        else:
            i += 1
    return ' '.join(em)







print(ulcensor(email_four))








