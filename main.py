from selenium import webdriver
import time, random

completeCount = 1
while completeCount == 1:
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
    questionNumber = 1
    questions = dr.find_elements_by_class_name('flaticon-frontend-check')
    question = questions[random.randint(0, len(questions) - 1)]
    firstQuestionText = question.text
    question.click()
    # NEXT QUESTION
    next_btn = dr.find_element_by_class_name('next')
    next_btn.click()
    # SECOND QUESTION
    time.sleep(0.5)
    if firstQuestionText == "Nie":
        secondQuestions = dr.find_elements_by_class_name('flaticon-frontend-check')
        secondQuestion = secondQuestions[4]
        secondQuestion.click()
        questionNumber += 1
        # NEXT QUESTION
        time.sleep(2)
        next_btn = dr.find_element_by_class_name('next')
        next_btn.click()
    else:
        secondQuestions = dr.find_elements_by_class_name('flaticon-frontend-check')
        ALLOWED_QUESTIONS = [secondQuestions[0], secondQuestions[1], secondQuestions[2], secondQuestions[3]]
        secondQuestion = ALLOWED_QUESTIONS[random.randint(0, len(ALLOWED_QUESTIONS) - 1)]
        print(secondQuestion.text)
        secondQuestion.click()
        questionNumber += 1
        # NEXT QUESTION
        time.sleep(1)
        next_btn = dr.find_element_by_class_name('next')
        next_btn.click()
    #THIRD QUESTION
    time.sleep(0.5)
    thirdQuestins = dr.find_elements_by_class_name('flaticon-frontend-check')
    THIRD_QUESTION_POSIBILITIS = [thirdQuestins[0], thirdQuestins[0], thirdQuestins[0], thirdQuestins[2]]
    thirdQuestion = THIRD_QUESTION_POSIBILITIS[random.randint(0, len(THIRD_QUESTION_POSIBILITIS) - 1)]
    thirdQuestion.click()
    questionNumber += 1
    #NEXT QUESTION
    time.sleep(1)
    next_btn = dr.find_element_by_class_name('next')
    next_btn.click()
    # FOURTH QUESTION
    time.sleep(0.5)
    fourthQuestions = dr.find_elements_by_class_name('flaticon-frontend-check')
    FOURTH_QUESTION_POSIBILITIES = [fourthQuestions[0], fourthQuestions[1], fourthQuestions[1], fourthQuestions[1], fourthQuestions[1], fourthQuestions[2], fourthQuestions[2]]
    fourthQuestion = FOURTH_QUESTION_POSIBILITIES[random.randint(0, len(FOURTH_QUESTION_POSIBILITIES) - 1)]
    fourthQuestion.click()
    #NEXT QUESTION
    time.sleep(1)
    next_btn = dr.find_element_by_class_name('next')
    next_btn.click()
    #FIFTH QUESTION
    time.sleep(0.5)
    fifthQuestions = dr.find_elements_by_class_name('flaticon-frontend-check')
    FIFTH_QUESTON_POSIBILITIS = [fifthQuestions[1], fifthQuestions[4], fifthQuestions[5], fifthQuestions[6]]
    for fifthQuestion in FIFTH_QUESTON_POSIBILITIS:
        PASS_POSIBILITY = [0, 0, 0, 0, 1]
        if PASS_POSIBILITY[random.randint(0, len(PASS_POSIBILITY) - 1)] == 1:
            pass
        else:
            fifthQuestion.click()
    #NEXT QUESTION
    time.sleep(1)
    next_btn = dr.find_element_by_class_name('next')
    next_btn.click()
    # SIXTH QUESTION
    time.sleep(0.5)
    sixthQuestions = dr.find_elements_by_class_name('flaticon-frontend-check')
    sixthQuestin = sixthQuestions[1]
    sixthQuestin.click()
    #NEXT QUESTION
    time.sleep(1)
    next_btn = dr.find_element_by_class_name('next')
    next_btn.click()
    # SEVENTH QUESTION
    time.sleep(0.5)
    seventhQuestions = dr.find_elements_by_class_name('flaticon-frontend-check')
    seventhQuestion = seventhQuestions[3]
    seventhQuestion.click()
    #NEXT QUESTION
    time.sleep(1)
    next_btn = dr.find_element_by_class_name('next')
    next_btn.click()
    # EIGHT QUESTION
    time.sleep(0.5)
    eightQuestions = dr.find_elements_by_class_name('flaticon-frontend-check')
    eightQuestion = eightQuestions[3]
    eightQuestion.click()
    #NEXT QUESTION
    time.sleep(1)
    next_btn = dr.find_element_by_class_name('next')
    next_btn.click()
    # NINETH QUESTION
    time.sleep(0.5)
    ninethQuestions = dr.find_elements_by_class_name('flaticon-frontend-check')
    NINETH_POSIBILITYS = [0, 0, 0, 1]
    if NINETH_POSIBILITYS[random.randint(0, len(NINETH_POSIBILITYS) - 1)] == 1:
        ninethQuestion = ninethQuestions[0]
        ninethQuestion.click()
    else:
        ninethQuestion = ninethQuestions[1]
        ninethQuestion.click()
    #NEXT QUESTION
    time.sleep(1)
    next_btn = dr.find_element_by_class_name('next')
    next_btn.click()
    # LAST QUESTION
    time.sleep(0.5)
    lastQuestions = dr.find_elements_by_class_name('flaticon-frontend-check')
    LAST_QUESTION_POSSIBILITIES = [0, 0, 0, 0, 1, 1, 2]
    if LAST_QUESTION_POSSIBILITIES[random.randint(0, len(LAST_QUESTION_POSSIBILITIES) - 1)] == 0:
        lastQuestion = lastQuestions[0]
        lastQuestion.click()
    elif LAST_QUESTION_POSSIBILITIES[random.randint(0, len(LAST_QUESTION_POSSIBILITIES) - 1)] == 1:
        lastQuestion = lastQuestions[1]
        lastQuestion.click()
    else:
        lastQuestion = lastQuestions[2]
        lastQuestion.click()

    # SEND BUTTON
    time.sleep(1)
    sendBtn = dr.find_element_by_class_name('submit')
    sendBtn.click()
    time.sleep(5)
    dr.close()

    completeCount += 1
    print("SUCCESS" + str(completeCount))

print("PROGRAM SKONČIL")
