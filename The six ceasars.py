#The Six Caesars
from PIL import Image  
#Intro 
print("Welcome to The Six Caesars! Make your choices wisely to successfully solve the mystery!")
img = Image.open('caesar bust.jpg')
img.show()
print()
name=input("Enter your name: ")
name=name.capitalize()
print("\nHello",name,". You are a renowned detective who enjoys tackling peculiar cases. Your next case awaits...")
print("Enter 1 to start the case. Enter 0 to exit")
choice=int(input("Are you ready? "))
print()
bad_end=0
#Pg 1
if choice==0:
    exit()
else:
    pass
print('You are at your residence, anticipating a friend’s arrival.')
print('Inspector Dale walks in, lost in thought. \n"',name,'I have a strange case on hand, something of your type. Interested in taking a look?"')
print("1. I'd be intrigued to take a look at it")
print("2. I'm busy, maybe some other time")
c1=int(input("Enter your choice number: \n"))
print()
if c1==1:
    print('Amazing! Here are the case details so far.')
elif c1==2:
    print("Maybe later then. \nGame Over.")
    exit()
print("Inspector Dale gladly hands over his official notebook to you.")
print()
print("Case Details:")
print()
print("First incident in Morse Hudson Shop: Four days ago: ")
print('The Assistant left shop for an instant when he heard a crash, came back to see that the bust of Caesar on the display counter had been smashed to pieces on the counter itself.')
print("He rushed outside and to his dismay, though many said they saw a man run out of the store, no one could point him out.")
print("It was dismissed as an act of meaningless vandalism and not looked into further.")
print()
print("Second incident at Kennington Road (close to Morse Hudson's shop:")
print("Dr.Barnicot's residence and principal consulting room. \nThe doctor is a very well known practitioner and has a second surgery/clinic and dispensary at Lower \
Brixton Road 2 miles away.")
print("Dr.Barnicot is a Caesar enthusiast. His house is filled with books, pictures and relics of the Roman Royal.")
print("Recently, he bought two duplicate plaster casts of the original bust of Caesar by French sculptor Devine.\nHe placed one in\
the hall of his house at Kennington Road and another on the mantelpiece of his surgery at Lower Brixton.")
print("When he came down to his hall last morning, he saw that it had been burgled, but strangely enough, everything was intact except his busts of Caesar.\
\nIt had been carried outside and smashed against the garden, the splintered fragments lying under the wall as evidence of it.")
print("After ensuring all else was intact and safe, Dr.Barnicot left for his clinic at 12 PM, and discovered that in the night, the window had been opened\
 and the second bust had been smashed on it's mantelpiece itself.")
print()
img = Image.open('broken bust.jpg')
img.show()
print("There were no signs of clues in either location to lead to the burglar's identity. \
 \nSo far, the only thing we know about the thief is his strange hatred for Caesar.")
print()
#Allow user to see notes so far before every choice
c2_note = int(input("\nYou can start taking your own case notes to keep track of things you find important. Do you want to? \n1.Yes\n2.No\n"))
notes = []
if c2_note == 1:
      print("Enter 'Close' when you're done.")
      n_points = input("- ")
      while n_points != 'Close':
          notes.append(n_points)
          n_points = input("- ") 
else:
    pass

#Pg 2
print()
print('Hmm, a strange layout indeed.')
print('1. How many busts were destroyed in total? \n2. Were all the busts broken exactly identical?')
c3 = int(input('Choice: '))
print()
if c3 == 1:
    print('"Only the ones in my notes, ',name,', 3 in total."')
elif c3 == 2:
    print("They were made from the same mould, so yes, ",name,", they were.")
    print("Then it's less likely to be due to a general hatred for Caesar, isn't it? There could be a hundred more such  busts, why did he begin with those from the same mould?")
    print("A fair observation, ",name," but I have already looked into it. Morse Hudson is the sole known dealer of such busts, and these were the three in his store for years. \
So, it's most probable that these happened to be the only busts in that area, and so the lunatic began with them." )
    print("1. Interesting, Inspector, but I still believe there's more to this than a general hatred. \n2. Oh, well what could be behind this hatred then?")
    c4 = int(input("Choice: "))
    if c4 == 1:
        print("Why so? What have you spotted that I missed?")
        print("Well, not much else at the moment but small details like the fact that the thief was in a great hurry despite having all the night for just a single article's \
burglary, and was still cautious. \nAt the residence, where he would be caught if an alarm was raised, he carried the bust outside and then broke it. \
In the clinic, where he knew he was safe, he just broke it in its place. In the shop, where there was the risk of being caught, he still didn't bother to carry it away and \
just broke it on the counter instead and left the moment he got a chance to")
        print("And this deductive skill is why I approach you with cases, ",name,'.')
    elif c4 == 2:
        print("Ah, I did some research, you see, and found something plausible. There is a medical condition called id´ee fixe, and to simply put it, this man could have been \
deeply impacted in some way by Caesar, hereditarily or through readings, and as a result has developed a craze for the emperor, but is completely sane in every other way.")
        print("Hmm. Sounds a little far fetched though. At any rate, every observation is important to a case.")
print("Anyways, all that can be done now is wait for further development of the case. No detail can be dismissed, no matter how minute. And so, I shall be more than happy to \
assist you further. Do keep me up to date.")
print("For sure, ",name,", something tells me this is going to be a very interesting investigation.")
print()
print("Chapter 1 - Fin. \nDo you want to make more case notes?")
print("1. Yes, I'll take down notes.\n2.No, but I want to see my notes.\n3.No, move on.")
c2_note = int(input("Choice: "))
if c2_note == 1:
      print("Enter 'Close' when you're done and 'View' to see your notes so far.")
      n_points = input("- ")
      while n_points != 'Close':
          if n_points == 'View':
              for i in notes:
                  print("- ", i)
              break
          else:
              notes.append(n_points)
              n_points = input("- ")
               
elif c2_note == 2:
    print ("Your notes:")
    for i in notes:
                  print("- ", i)
                    
print("Chapter 2 : A grave turn of events.")
print("\nThe updates you wanted reach you sooner and in a more grave form than expected. \nYou have received a fax from Inspector Dale :")
print("Come as soon as it is possible: 131, Pitt Street, Kensington. \nYour curiosity, now aroused because the Inspector couldn't even wait to talk in person, takes you to the \
address within half  an hour.")
print("Upon reaching, you see such a crowd that you think it can't be anything less than a murder attempt, and approach the Inspector waiting outside for you with a grave expression.")
print("\nWhat's all this, Dale? ")
print("It's the Caesar business again, ",name,", best you find out from our source himself. He's in the hall, come on in.")
print('\nGuiding you into the hall, Inspector informs you of what to expect. \n"You must know Mr. Harker, surely,',name,' he is a well known journalist, and has covered some of your \
more popular cases before. He is rather disturbed yet excited by the whole scene he witnessed, but is agitated by the fact that he is unable to write out a report of the events he \
got to witness."')
print("Inside, an exceedingly unkempt and agitated elderly man, clad in a flannel dressing-gown, is pacing up and down. This is Horace Harker, owner of this crime scene.")
print("Good day, Mr. Horace. What has gotten you this agitated? What has this case turned to?")
print("Murder. Murder, Detective ",name,", that's what it has turned to. It's such a shame too, all my life I have been collecting other's news but now that such an extraordinary bit \
has approached my doorstep, I'm too flustered to put together words. If I had come as a journalist, I'd have my two page report published in the evening's papers. By repeating the tale\
to different people,I'm already giving away valuable copies of my tale and can't make use of it myself, but I've heard well about you, Detective, and if you could explain this bizarre \
business, it'll be payment for me troubles." )
print("Of course, please go on.")
print("The trigger seemed to be the bust of Caesar kept in this very room. I picked it up for cheap from Harding Brothers, two doors down High Street Station four months ago. \
\nI do most of my journalistic work through the night till dawn, as I was last night. I was nested up in my den, a room at the upper back side of the house, when around 3 AM I heard \
noises downstairs. I listened closely but it seemed to never have happened. Shrugging it off as a trick of sleeplessness, I went back to my work, but barely 5 minutes later, I heard \
the most blood curdling scream - the most horrifying sound I've ever heard, Detective. It will ring in my ears for life. \nI sat frozen in terror for a minute before grabbing the poker \
and steeling my nerves. I headed down and noticed at once that the bust was missing. For the life of me, I couldn't figure why anyone would break in for a mere plastic cast ")
print("And what do I see more agitating than the missing bust? BLOOD! A stream of it flowing from my dead housekeeper. I immediately called the police and the ambulance. This entire ordeal \
has left me completely shaken Detective.")
print()
print("A murder? Now this case has completely caught your interest.")
print()
print('1. Examine the crime scene \n2. Wait for the cops to finish their work and console Mr. Harker instead')
c5 = int(input('Choice: '))
print()
if c5 == 1:
    print("The blood hasn't been cleaned from the crime scene. It's bright crimson colour is deeply disturbing. The killer is a cold one, their chosen weapon of murder is a hammer, which \
is lying next to the chalk outline of the body.")
    img = Image.open('body.jpg')
    img.show()
    print("As you examine every nook and cranny, you realise the killer hasn't been so careful after all. There are a few mud patches which vaguely resemble footprints. Though, it is unlike \
any normal footprint made by a shoe.")
    print()
    print('1. Examine the footprints closely \n2. Dismiss it as irrelevant')
    c6 = int(input('Choice: '))
    print()
    if c6 == 1:
        print("The footprints are pointed. They have definitely been made by a person wearing high heels. The killer is a woman!")
        img = Image.open('footstep.png')
        img.show()
        print()
        print("End of Chapter 2")
    else:
        bad_end+=1
else:
    bad_end+=1
    print("Don't worry Mr. Harker. I will try my best to investigate and help you out")
    print("End of Chapter 2")
  



