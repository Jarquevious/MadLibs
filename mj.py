# FIRST SENTENCE
#Shoutout to Francis my classmate for teaching me the while loop to handle improper user input
from termcolor import colored
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
    print(f"Micheal Jackson was born in {colored(noun1,'red')} USA in 1958.") 
    print(f"He was a {colored(adjective1, 'red')} performer with a {colored(adjective2, 'red')} voice {colored(conjection1, 'red')} a {colored(adjective3, 'red')} personality.")
    print(f"Although he was a {colored(adjective4, 'red')} person, his family and friends thought he was {colored(adjective5, 'red')} for {colored(adverb1, 'red')}, {colored(verb1, 'red')} when he interacted with fans.")
    print(f"{colored(pronoun1, 'red')} became famous for creating {colored(adjective6, 'red')} music, {colored(adjective7, 'red')} collaborations, and {colored(adjective8, 'red')} love for his fans. In 1984, Jackson was")
    print(f"{colored(adjective9, 'red')} onto the Hollywood Walk of Fame.")
    print(f"After his death in 2009, Jackson’s {colored(noun2, 'red')} was released for his fans, becoming the most {colored(adjective10, 'red')} documentary or concert film ever.")

output() 



