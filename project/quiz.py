class Question:
    def __init__(self, prompt):
        self.prompt = prompt

questions_prompts = [
"Does your face look shiny in the photo?\n(a) Never\n(b) Sometimes\n(c) Often\n(d) Always\n\n",
"Being in a dry environment, if you don't use skin care products, your facial skin?\n(a)Feels normal\n(b)feels tight \n(c)Feels dry or tingly Dry \n(d)Looks shiny or never feels the need to moisturize \n\n  ",
"After washing your face with a rich soap cleanser, how sensitive do you feel?\n(a)Feels dry, or has a tingling sensation\n(b)Feels a little dry but no stinging\n(c)Feel no abnormalities \n(d)Feeling oily\n\n",
"Is the T-zone (forehead and nose area) oil?\n(a) Never\n(b) Sometimes\n(c) Often\n(d) Always\n\n",
"Which one best describes the appearance of your pores?\n(a)Large and clearly visible\n(b)medium size greasy\n(c)Small, not visible unless you pay attention\n(d)Large or medium sized, visible only on forehead and nose\n\n"    
]

questions = [
    Question(questions_prompts[0]),
    Question(questions_prompts[1]),
    Question(questions_prompts[2]),
    Question(questions_prompts[3]),
    Question(questions_prompts[4])
]
# define how to run test and count score
def run_test(questions):
    score = 0
    for question in questions: 
        answer = input(question.prompt)
        if answer == "a":
            score += 1
        if answer == "b":
            score += 2
        if answer == "c":
            score += 3
        if answer == "d":
            score += 4
        else:
            print("The letter you entered is wrong, please try again.")
#20-18>17-14>13-11>10-8>7-5
    if score <= 20 and score >= 18:
        print("Your skintype is oily skin ")
    elif score <= 17 or score >= 14:
        print("Your skin type is combination skin")
    elif score <= 13 and score >= 11:
        print("Your skintype is dry skin")
    elif score <= 10 and score >= 8:
        print("Your skintype is sensitive skin")
    elif score <= 7 and score >= 5:
        print("Your skintype is neutral skin")
run_test(questions)






 


    