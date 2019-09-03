# FIRST SENTENCE
#Shoutout to Francis my classmate for teaching me the while loop to handle improper user input
noun1 = input("Enter a noun(City in the Midwest USA): ")
while len(noun1) == 0:
    noun1 = input("Enter again: ")
    
# SECOND SENTENCE 
adjective1 = input("Enter an adjective: ")
while len(adjective1) == 0:
    adjective1 = input("Enter again: ")

adjective2 = input("Enter an adjective: ")
while len(adjective2) == 0:
    adjective2 = input("Enter again: ")

conjection1 = input("Enter a conjunction: ")
while len(conjection1) == 0:
    conjunction1 = input("Enter again: ")

adjective3 = input("Enter an adjective: ")
while len(adjective3) == 0:
    adjective3 = input("Enter again: ")

# THIRD SENTENCE 
adjective4 = input("Enter an adjective: ")
while len(adjective4) == 0:
    adjective4 = input("Enter again: ")

adjective5 = input("Enter an adjective: ")
while len(adjective5) == 0:
    adjective5 = input("Enter again: ")

adverb1 = input("Enter an adverb: ")
while len(adverb1) == 0:
    adverb1 = input("Enter again: ")

verb1 = input("Enter a verb: ")
while len(verb1) == 0:
    verb1 = input("Enter again: ")

#FOURTH SENTENCE 
pronoun1 = input("Enter a pronoun: ")
while len(pronoun1) == 0:
    pronoun1 = input("Enter again: ")

adjective6 = input("Enter an adjective: ")
while len(adjective6) == 0:
    adjective6 = input("Enter again: ")

adjective7 = input("Enter an adjective: ")
while len(adjective7) == 0:
    adjective7 = input("Enter again: ")

adjective8 = input("Enter an adjective: ")
while len(adjective8) == 0:
    adjective8 = input("Enter again: ")

# FIFTH SENTENCE 
adjective9 = input("Enter an adjective: ")
while len(adjective9) == 0:
    adjective9 = input("Enter again: ")

# SIXTH SENTENCE
noun2 = input("Enter a noun(a thing): ")
while len(noun2) == 0:
    noun2 = input("Enter again: ")

adjective10 = input("Enter an adjective: ")
while len(adjective10) == 0:
    adjective10 = input("Enter again: ")





#OUTPUT FUNCTION
def output():
    print("Micheal Jackson was born in (" + noun1 + ") USA in 1958.") 
    print("He was a (" + adjective1 + ") performer with a (" + adjective2 + ") voice (" + conjection1 + ") a (" + adjective3 + ") personality.")
    print("Although he was a (" + adjective4 + ") person, his family and friends thought he was (" + adjective5 + ") for (" + adverb1 + ") (" + verb1 + ") when he interacted with people.")
    print("(" + pronoun1 + ") became famous for creating (" + adjective6 + ") music, (" + adjective7 + ") collaborations, and (" + adjective8 + ") love for his fans. In 1984, Jackson was")
    print("(" + adjective9 + ") onto the Hollywood Walk of Fame.")
    print("After his death in 2009, Jackson’s (" + noun2 + ") was released for his fans, becoming the most ((" + adjective10 + ") documentary or concert film ever.")

output() 


