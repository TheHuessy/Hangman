import re
import random

#set the 'game' variable that decides whether or not to keep going
game = 0
#create a while loop that works as long as game == 0. Once game stops being 0, the program ends
while game == 0:
    #setting the word variable. Each time the player wins or loses the hangman game, gotit changes to !=0
    gotit = 0
    #load a dummy location list
    loc = []
    #start the turn counter to 0
    trn = 0
    #set the number of incorrect tries to 0
    bad = 0
    #load the corpus of words
    words = ["shelter",
             "separate",
             "encourage",
             "juggle",
             "graceful",
             "balance",
             "needless",
             "trains",
             "window",
             "frog",
             "bouncy",
             "mint",
             "holistic",
             "clumsy",
             "wall",
             "inconclusive",
             "rule",
             "sea",
             "observation",
             "cracker",
             "last",
             "bat",
             "motion",
             "kindly",
             "frantic",
             "accurate",
             "knot",
             "kaput",
             "return",
             "bright",
             "bomb",
             "angle",
             "wrist",
             "door",
             "greasy",
             "thankful",
             "end",
             "fork",
             "breath",
             "corn",
             "command",
             "squeeze",
             "harmony",
             "relieved",
             "coast",
             "married",
             "ubiquitous",
             "property",
             "ambitious",
             "replace",
             "defective",
             "gullible",
             "note",
             "repair",
             "grip",
             "ashamed",
             "boy",
             "farm",
             "sand",
             "type",
             "gabby",
             "scattered",
             "kitty",
             "halting",
             "satisfying",
             "condition",
             "thrill",
             "pushy",
             "functional",
             "optimal",
             "statuesque",
             "pack",
             "harmonious",
             "pretty",
             "squeak",
             "stereotyped",
             "governor",
             "detailed",
             "simple",
             "scent",
             "glorious",
             "piquant",
             "lacking",
             "arm",
             "agonizing",
             "slip",
             "cold",
             "animated",
             "water",
             "substantial",
             "excite",
             "sneaky",
             "rough",
             "bath",
             "precede",
             "dependent",
             "flat",
             "person",
             "frightening",
             "authority"]
    #create a random number that will decide which word we choose from the corpus
    ch = random.randint(0,len(words)-1)
    #While loop that is the actual game
    while gotit == 0:
        #load the word we're going to guess
        word = words[ch]
        #intiate a new turn
        trn = trn+1        
        #conditional argument that shows how many total letters are in the word
        #this is sort of helpful, but less so now that there over 5 words
        #still could help people...
        if trn == 1:
            print(str(len(word)) + ' total letters')
            resp = '-' * len(word)
        #the user input variable, it prompts the user
        gu = input("Letter?")
        #conditional argument if the letter the user (both the guess and the word are set to upper case for this test)
        #chose is in the word
        if gu.upper() in word.upper():
            #rewriting the response string so that we can build it based on the number of correct letters chosen
            resp = ""
            #letting them know they did it
            print('Yes')
            #checking the word to see how many times the guessed letter appears
            #it then appends to the location list (all locations of the letter)
            loc.extend([x.start() for x in re.finditer(gu, word)])
            #building the response variable
            for i in range(len(word)):
                #if the location of the right letter is not iterated, print a dash
                if i not in loc:
                    resp = resp + '-'
                #if the location of the right letter IS iterated, print that letter
                else:
                    resp = resp + word[i]
            #show the people what they have so far
            print(resp)
            #checking to seeif that last letter was the final one
            if resp == word:
                #if it is, then gotit turns to 1 and the game is over for that word
                gotit = 1
        #if they guessed incorrectly, then bad things happen
        else:
            #number of bad tries is increased
            bad = bad+1
            #checking to see if we've hit our max failure rate of 10
            if bad == 10:
                #if it's at 10, you lose because you killed him
                print("You killed him!")
                #It then tells you what the word was so you don't hate life
                print("The word was " + '"' + word + '"')
                #changing the value of gotit from 0 so that it ends the game
                gotit = 2
            #if this isn't failure 10, then it just tells you no
            else:
                print('No')
                print(resp)
    #if gotit is 1, then the player won
    if gotit == 1:
        print("YOU DID IT!")
    #asking if the player wants to play again
    ad = input("Continue?.....(y/n)")
    #if the player doesn't want to play again
    if ad.upper() == 'N':
        #game set to 1, the program ends
        game = 1
    else:
        #prints this message and then goes back to the beginning of the while loop
        print("Starting new game...")
#parting message before closing
print("Goodbye!")
        
