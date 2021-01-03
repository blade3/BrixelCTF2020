#/usr/bin/python3

import os
import requests
from bs4 import BeautifulSoup

phpsessionID=""
page = ""
URL = 'http://timesink.be/quizbot/index.php'
last_success_answer=''
last_question=''
rep=""

with requests.Session() as s:
    page = s.get(URL)

    questions = []
    soup = BeautifulSoup(page.content, 'html.parser')
    print(phpsessionID)

    with open(os.path.dirname(__file__) + "/questions.txt", encoding="utf-8") as file:
        questions = [l.rstrip("\n") for l in file]

    for i in range(0,1000):
        #Get the question:
        html_question = soup.find("h4").text.strip()

        # check if its a bad answer:
        bad_response=soup.find(id='answer')
        if bad_response and i > 0:
            #if yes, get the real answer
            answer=bad_response.text
            if answer == last_success_answer:
                print('Last response seems to be the equals to the following response. something wrong.')
                exit()
            print(rep, ' is not the answer. the answer is: ',answer)
            with open(os.path.dirname(__file__) + "/questions.txt", 'a') as fd:
                fd.write(f'\n{last_question}|{answer}')

        print('')
        print('> (',i+1,')',html_question)
        rep=""
        for j in questions:
            if html_question in j:
                rep= j[j.find("|")+1:]
                last_success_answer=rep
                print("trouver:",rep)
                break
        if not rep:
            rep="dontknow"

        last_question=html_question
        page = s.post(URL, data={'insert_answer': rep})
        soup = BeautifulSoup(page.content, 'html.parser')
    # the last questions is never stored, need to store yourself, after running twice, you got the flag
    print(page.content)

    # brixelCTF{kn0wl3dg3}