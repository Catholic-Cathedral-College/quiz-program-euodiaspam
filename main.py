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

#sarting exam qquestions
print(" ")
print("Question #1")
print("")