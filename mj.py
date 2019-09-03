# FIRST SENTENCE
noun1 = input("Enter a noun(City in the Midwest USA): ")
while len(noun1) == 0:
    noun1 = input("Enter a noun(place) again: ")
    
# SECOND SENTENCE 
adjective1 = input("Enter an adjective: ")
while len(adjective1) == 0:
    adjective1 = input("Enter an adjective again: ")

adjective2 = input("Enter an adjective: ")
while len(adjective2) == 0:
    adjective2 = input("Enter an adjective again: ")

conjection1 = input("Enter a conjunction: ")
while len(noun1) == 0:
    noun1 = input("Enter a noun(City in the Midwest USA) again: ")

adjective3 = input("Enter an adjective: ")
while len(noun1) == 0:
    noun1 = input("Enter a noun(place) again: ")

# THIRD SENTENCE 
adjective4 = input("Enter an adjective: ")
adjective5 = input("Enter an adjective: ")
adverb1 = input("Enter an adverb: ")
verb1 = input("Enter a verb: ")

#FOURTH SENTENCE 
pronoun1 = input("Enter a pronoun: ")
adjective6 = input("Enter an adjective: ")
adjective7 = input("Enter an adjective: ")
adjective8 = input("Enter an adjective: ")

# FIFTH SENTENCE 
adjective9 = input("Enter an adjective: ")

# SIXTH SENTENCE
noun2 = input("Enter a noun(a thing): ")
adjective10 = input("Enter an adjective: ")





#OUTPUT FUNCTION
def output():
    print("Micheal Jackson was born in (" + noun1 + ") USA in 1958.") 
    print("He was a (" + adjective1 + ") performer with a (" + adjective2 + ") voice (" + conjection1 + ") a (" + adjective3 + ") personality.")
    print("Although he was a (" + adjective4 + ") person, his family and friends thought he was (" + adjective5 + ") for (" + adverb1 + ") (" + verb1 + ") when he interacted with people.")
    print("(" + pronoun1 + ") became famous for creating (" + adjective6 + ") music, (" + adjective7 + ") collaborations, and (" + adjective8 + ") love for his fans. In 1984, Jackson was")
    print("(" + adjective9 + ") onto the Hollywood Walk of Fame.")
    print("After his death in 2009, Jackson’s (" + noun2 + ") was released for his fans, becoming the most ((" + adjective10 + ") documentary or concert film ever.")

output() 


