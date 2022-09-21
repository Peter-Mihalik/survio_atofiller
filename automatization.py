from selenium import webdriver
import time, random

link = "https://www.survio.com/survey/d/A6E5M2R4C6I4I7L2G"
# OPEN AND MAXIMAZE
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
dr = webdriver.Chrome(chrome_options=options)

dr.get(link)
# START DOTAZNIK
time.sleep(3)
start_btn = dr.find_element_by_class_name('start')
start_btn.click()
time.sleep(2)
# FIRST QUESTION
def numberOfQuestions():
    progres_bar_width = dr.find_element_by_class_name("progress").value_of_css_property("width")
    dr_width = 1920
    progres_bar_width = progres_bar_width.split('p')
    progres_bar_width = progres_bar_width[0]
    print(progres_bar_width)
    global number_of_questions
    number_of_questions = int(dr_width / float(progres_bar_width) - 1)
    print(number_of_questions)

i = 1

def clickQuestion(nieInQuestionStatus):
    time.sleep(0.5)
    headline = dr.find_element_by_class_name('help').text
    global question
    questions = dr.find_elements_by_class_name('flaticon-frontend-check')
    # OTAZKA 3
    if i == 3:
        right_answer = questions[0]
        not_sure = questions[2]
        POSIBILITIES = [right_answer, right_answer, right_answer, not_sure]
        question = POSIBILITIES[random.randint(0, len(POSIBILITIES) - 1)]
        question.click()
    elif i == 4:
        right_answer = questions[1]
        not_sure = questions[2]
        POSIBILITIES = [right_answer, right_answer, right_answer, not_sure]
        question = POSIBILITIES[random.randint(0, len(POSIBILITIES) - 1)]
        question.click()
    else:
        if 'viac' in headline:
            if i == 5:
                right_answers = [questions[1], questions[4], questions[5], questions[6]]
                for right_answer in right_answers:
                    EXCEPTION_POSIBILITY = [0, 0, 0, 0, 1]
                    if EXCEPTION_POSIBILITY[random.randint(0, len(EXCEPTION_POSIBILITY) - 1)] == 1:
                        pass
                    else:
                        right_answer.click()
            else:
                print(i)



        else:
            randomPick = random.randrange(1, len(questions))
            question = questions[randomPick]
            question.click()


def nextQuestion():
    next_btn = dr.find_element_by_class_name('next')
    next_btn.click()

# FIRST QUESTION AND GET NUMBER OF QUESTIONS
nieInQuestionStatus = False
clickQuestion(nieInQuestionStatus)
numberOfQuestions()
if "Nie" in question.text:
    nieInQuestionStatus = True
else:
    nieInQuestionStatus = False

nextQuestion()
time.sleep(1.5)



while (i < number_of_questions):
    clickQuestion(nieInQuestionStatus)
    nextQuestion()
    i += 1
    time.sleep(1.5)
