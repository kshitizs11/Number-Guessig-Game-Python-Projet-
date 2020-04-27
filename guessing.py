import random
#GET GUESS
def get_guess():
    return list(input("What is your guess"))

#Generate computer code123
def generate_code():
    digits=[str(num) for num in range(10)]
    #shuffel the digits
    random.shuffle(digits)
    #Grab the first three
    return digits[:3]
#Generate the clues
def generate_clues(code,user_guess):
    if user_guess==code:
        return "Code Cracked"
    clues=[]
    for ind,num in enumerate(user_guess):
        if num==code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues

#Run Game Logic
print("Welcome code breaker!")

secret_code=generate_code()

clue_report=[]

while clue_report != "Code cracked!":
    guess=get_guess()

    clue_report=generate_clues(guess,secret_code)
    print("Here is the result of your guess:")
    for clue in clue_report:
        print(clue)
