from selenium import webdriver
import time, random

def next():
    # NEXT QUESTION
    time.sleep(0.5)
    next_btn = dr.find_element_by_class_name('next')
    next_btn.click()
    time.sleep(1)

completeCount = 1
while completeCount <= 64:
    link = "https://www.survio.com/survey/d/D5E1Q9Y9G1H4F5T6G"
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
    firstQs = dr.find_elements_by_class_name('flaticon-frontend-check')
    FIRST_POSIBILITIS = [firstQs[0],firstQs[0],firstQs[0],firstQs[0],firstQs[0],firstQs[0],firstQs[0],firstQs[0],firstQs[1],firstQs[2],firstQs[2]]
    fisrt = FIRST_POSIBILITIS[random.randint(0, len(FIRST_POSIBILITIS) - 1)]
    fisrt.click()
    next()

    #SECOND QUESTION
    secondQs = dr.find_elements_by_class_name('flaticon-frontend-check')
    SECOND_POSIBILITIES = [secondQs[1],secondQs[1],secondQs[1],secondQs[0],secondQs[3],secondQs[2],secondQs[2],secondQs[2],secondQs[2]]
    second = SECOND_POSIBILITIES[random.randint(0, len(SECOND_POSIBILITIES) - 1)]
    second.click()
    next()

    #THIRD QUESTION
    threeQs = dr.find_elements_by_class_name('flaticon-frontend-check')
    THREE_POS = [threeQs[0],threeQs[0],threeQs[3],threeQs[3],threeQs[3],threeQs[2],threeQs[2],threeQs[2],threeQs[1],threeQs[1],threeQs[1]]
    three = THREE_POS[random.randint(0, len(THREE_POS) - 1)]
    three.click()
    next()

    # 4 QUESTION
    number = dr.find_elements_by_class_name("active")
    while len(number) == 0:
        fourQs = dr.find_elements_by_class_name('flaticon-frontend-check')
        for four in fourQs:
            if random.randint(0, 1) == 1:
                four.click()
        number = dr.find_elements_by_class_name("active")
    next()

    # 5 QUESTION
    fiveQs = dr.find_elements_by_class_name('flaticon-frontend-check')
    FIVE_POS = [fiveQs[2],fiveQs[2],fiveQs[2],fiveQs[2],fiveQs[2],fiveQs[1],fiveQs[0]]
    five = FIVE_POS[random.randint(0, len(FIVE_POS) - 1)]
    five.click()
    next()

    # 6 QUESTION
    sixQs = dr.find_elements_by_class_name('flaticon-frontend-check')
    SIX_POS = [sixQs[2], sixQs[2], sixQs[2], sixQs[2], sixQs[1], sixQs[1], sixQs[1], sixQs[1]]
    six = SIX_POS[random.randint(0, len(SIX_POS) - 1)]
    six.click()
    next()

    # 7 QUESTION
    seven = dr.find_elements_by_class_name('flaticon-frontend-check')
    seven[0].click()
    next()
    
    # 8 QUESTION
    eight = dr.find_elements_by_class_name('flaticon-frontend-check')
    eight[0].click()
    next()

    # 9 QUESTION
    nineQs = dr.find_elements_by_class_name('flaticon-frontend-check')
    NINE_POS = [nineQs[0],nineQs[1],nineQs[1],nineQs[1],nineQs[1], nineQs[1], nineQs[1], nineQs[1], nineQs[1]]
    nine = NINE_POS[random.randint(0, len(NINE_POS) - 1)]
    nine.click()
    next()

    # LAST QUESTION
    lastQs = dr.find_elements_by_class_name('flaticon-frontend-check')
    LAST_POS = [lastQs[0], lastQs[1], lastQs[1],lastQs[1],lastQs[1],lastQs[1],lastQs[1],lastQs[1],lastQs[1],lastQs[1]]
    last = LAST_POS[random.randint(0, len(LAST_POS) - 1)]
    last.click()

    # SEND
    time.sleep(1)
    sendBtn = dr.find_element_by_class_name('submit')
    sendBtn.click()
    time.sleep(5)
    dr.close()
    print(f"DONE {completeCount} times")
    completeCount += 1

print("***SUCESS***")