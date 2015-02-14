__author__ = 'Applegrain'
#welcome message

print "Welcome to the quiz. The goal is to get 5 points by answering a total of 5 questions."
print "If you answer the question correctly on the first try, you will get 2 points."
print "If you answer incorrectly, one point will be subtracted from your current score."

#score calculations
score = 0

#first question
print "Question #1: Which country currently has a female prime minister or president?"
ans_1 = raw_input("Is it (a)Australia, (b)Liberia or (c)Iceland?")
if ans_1 == "b":
    score = score + 2
    print ("Great! Your current score is %d." % score)
else:
    score = score -1
    print ("Incorrect. The correct answer was Liberia. Your current score is %d." % score)

#second question
print "Question #2: In which country can you find most remnants of the Inca Empire?"
ans_2 = raw_input("Is it (a)Peru, (b)Mexico, or (c)Brazil?")
if ans_2 == "a":
    score = score + 2
    print ("Awesome! Your current score is %d." % score)
else:
    score = score -1
    print ("Incorrect. The correct answer is Peru. Your current score is %d." % score)

#third question
print "Question #3: Which phrase do Chinese people use to greet acquaintances?"
ans_3 = raw_input("Is it (a)'How are you doing?', (b)'Have you had lunch?' or (c)'Are you tired?'")
if ans_3 == "b":
    score = score + 2
    print ("Go you! Your current score is %d." % score)
else:
    score = score -1
    print ("Incorrect. The correct answer is 'Have you had lunch?'. Your current score is %d." % score)

#fourth question
print "Question #4: Which well-known island do you find off the coast of Ecuador?"
ans_4 = raw_input("Is it (a)Easter Island, (b)Hawaii or (c)the Galapagos?")
if ans_4 == "c":
    score = score + 2
    print ("Wop wop! Your current score is %d." % score)
else:
    score = score - 1
    print ("Incorrect. The correct answer is the Galapagos. Your current score is %d." % score)

#fifth question
print "Question #5: Which one of these incumbent national leaders have ruled the longest?"
ans_5 = raw_input("Is it (a)Robert Mugabe, (b)Bashar al-Assad or (c)Vladimir Putin?")
if ans_5 == "a":
    score = score + 2
else:
    score = score -1
    print ("Incorrect. Correct answer is Robert Mugabe. Your current score is %d." % score)


if score == 10:
    score = score + 10
    print ("10 bonus points for five correct answers!")

if score >= 5:
    print ("You made it! Your final score is %d!" % score)
else:
    print ("You lost! Your final score is %d." % score)


