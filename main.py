#emil verification
email = input("please, verify your email below:\n")

#introduction
ISCP = input("""have you ever heard 'ISCP?'\n""")

if ISCP == "yes":
  print(" ")
  print("ohh, I see.\n")
  input("where did you heard about ISCP? \n a. Social Media \n b. Trough Friends \n c. I go to ISCP \n d. Just now\n")
else:
  print("You don't know ISCP?\n"
"how dare you not know ISCP.\n")
  
#brief introduction
know_iscp = input("do you want to know What's ISCP?\n")

if know_iscp == "yes":
    print(" ")
    print("Here's a brief introduction of ISCP:\n")
else:
    print(" ")
    print("""Shame, Im still going to tell you what ISCP is.\n""")

#iscp info
print("International State College of the Philippines or ISCP for short, is one of the most prestigious colleges that exist in the universe.\n")

#Iscp Campuses
print("ISCP contains more than 8 campuses, such as:\n"
"Main Campus, Sun and Moon Campus, Moon Campus, Biringan Campus, Overseas, Antarctica Campus, Antlantis Campus, Mars Campus, Jupiter Campus, and more.\n""")

#Iscp extension and courses
print("""Other than campuses in ISCP, there are also campus extension in ISCP. As well of heaps of subjects and courses. some of the popular courses taken by the students are:\n
BS Psychlogy Major in Gaslighting, BA in Mass Communication Major in Community Information Gathering and Relying Systems(Marites),BA Accountancy Major in Mangkukupit, and more.\n""")


#ask if they would like to enroll in this school 
interested = input("are you interested in joining our school, ISCP?\n")

if interested == "yes":
  print("")
  print("Welcome, future ISCPanians!")
else:
  print(" ")
  print("what a dissapointment. Go and enroll.")

print(" ")
enrol = input("do you wish to enroll in this school?\n")

if enrol == "yes":
  print(" ")
  print("""cool!""")
  print(" ")
  print("Before you enroll, please participate in the entrance exam if you're an up-coming new student.")
else:
  print(" ")
  print("you can't back out now.")
  print(" ")
  print("Please wait for the Administration to contact you for further details. You will still need take the entrance exam test.")

#a conversation with the administration
print(" ")
print("Administrator: Hello there.")
print(" ")
name = input("Administrator: What's your name?\n")
print(" ")
print("Administrator: Hello, {}. {} is a nice name.".format(name, name))
print("Administrator: Now I'm not trying to be flirty, but your name sounds indeed nice.")
print(" ")
exam = input("Administrator: I heard that you are taking an entrance exam test? Did I heard right?\n")

if exam == "yes":
  print(" ")
  print("Please sit back and get ready for the entrance exam.")
  
else:
  print(" ")
  print("Administrator: Too bad, you still have to go and take the entrance exam.")

#disclaimer before the exam
print(" ")
print("Disclaimer.\n"
     "You can't drop out of this school once you're enrolled.\n"
     "This meant you're fully commited to the terms and regulation of this school, even if it meant that you don't want to go/attend this school.")

#exam prep
print(" ")
print("welcome to the entrance test of ISCP.")
print(" ")
name = input("Please enter your full name below\n")
print(" ")
print("{} will now take the exam in".format(name))
print(" ")
print("3")
print(" ")
print("2")
print(" ")
print("1")
print(" ")
print("START!")

#exam question 1-10
score = 0
  
print(" ")
print("Question #1")
print("")
answer1 = input("Fill in the blank: 'Baby baby ___ my Sun and Moon.' \nA.you're \nB.your \nC.U'r \nD.ur \nE.you \n")
if answer1 == "A" or answer1 == "you're" or answer1 == "a":
  score += 1

else:
  print(" ")
print(" ")
print("Question #2")
print(" ")
answer2 = input("Why is a boxing ring called a ring even though it is square? \nA. The name 'ring' is a relic from when contests were fought in a roughly drawn circle on the ground. The name ring continued with the London Prize Ring Rules in 1743, which specified a small circle in the centre of the fight area where the boxers met at the start of each round. \nB. Because it's a box. \nC. I don't know \n")
if answer2 == "A" or answer2 == "a":
  score += 1

else:
  print(" ")
print(" ")
print("Question #3")
print(" ")
answer3 = input("1 + 1?\n")
if answer3 == "magellan" or answer3 == "Magellan":
   score += 1

else:
  print(" ")
print(' ')
print("Question #4")
answer4 = input("While walking, you saw your classmate's having problems, as a good student what should you do? \nA. Hangout \nB. You know... \nC. Walk like nothing happened. \n")
if answer4 == "A" or answer4 == "a" or answer4 == "C" or answer4 == "c":
  score += 1

else:
  print("why???")
print(" ")
print("Question #5")
answer5 = input("Where was the Philippine hero, Dr. Jose Rizal got shot? \nA. Bagumbayan. \nB. At the back. \nC. in The Philippines. \n")
if answer5 == "B" or answer5 == "b":
  score += 1

else:
  print(" ")
print(" ")
print("Question #6")
answer6 = input("Who killed Lapu-Lapu? \nA. Magellan. \nB. Aldous. \nC. None.\n")
if answer6 == "B" or answer6 == "b":
    score += 1

else:
  print(" ")
print(" ")
print("Question #7")
answer7 = input("why is the blackboared green?")
score += 1

print(" ")
print("Question #8")
answer8 = input("what's the full name of the philippines national hero? \nA. José Protacio Rizal Mercado y Alonso Realonda. \nB. Jose Rizal. \nC. J Riz. \n")
if answer8 == "A" or answer8 == "a":
  score += 1

else:
  print(" ")
print(" ")
print("Question #9")
answer9 = input("what is orange? \nA. A colour. \nB. A kind of fruit.")
score += 1

print(" ")
print("Question #10")
answer10 = input("Why did you take this entrance exam? (requires 100 word essay)\n")
score += 1

#scoring
if score <= 5:
  print("Your total score is {} out of 10.".format(score))
  print("You failed. You need to retake an exam again.")

if score >= 1:
  print("Your total score is {} out of 10.".format(score))
  print("Congratulations! you passed!")
