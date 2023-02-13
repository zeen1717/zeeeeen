class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions_prompts = [
"Does your face look shiny in the photo?\n(a) Never\n(b) Sometimes\n(c) Often\n(d) Always\n\n",
"Being in a dry environment, if you don't use skin care products, your facial skin?\n(a)Feels normal\n(b)feels tight \n(c)Feels dry or tingly Dry \n(d) Looks shiny or never feels the need to moisturize \n\n  ",
"After washing your face with a rich soap cleanser, how sensitive do you feel?\n(a)Feels dry, or has a tingling sensation\n(b)Feels a little dry but no stinging\n(c)Feel no abnormalities \n(d)Feeling oily\n\n",
"Is the T-zone (forehead and nose area) oil?\n(a) Never\n(b) Sometimes\n(c) Often\n(d) Always\n\n",
"Which one best describes the appearance of your pores?\n(a)Large and clearly visible\n(b)medium size greasy\n(c)Small, not visible unless you pay attention\n(d)Large or medium sized, visible only on forehead and nose\n\n"    
]

questions = [
    Question(questions_prompts[0],"a","b","c","d")
    Question(questions_prompts[1],"a","b","c","d")
    Question(questions_prompts[2],"a","b","c","d")
    Question(questions_prompts[3],"a","b","c","d")
    Question(questions_prompts[4],"a","b","c","d")
    Question(questions_prompts[5],"a","b","c","d")

]

def run_test(questions):
    score = 0
    for quesiton in questions:
        answer = input(questions)


    