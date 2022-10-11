## 첫번째 문제
from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    
    for i in range(len(terms)):
        a,b = terms[i].split(' ')
        terms_dict[a] = int(b)
        
    t_year, t_mm, t_day = map(int, today.split('.'))
    ttoday = datetime(t_year, t_mm, t_day)
    
    ## 분리하기 privacies
    for i in range(len(privacies)):
        tmp = privacies[i].split(' ')
        p_day = tmp[0]
        p_type = tmp[-1]
        
        p_year, p_mm, p_day = map(int, p_day.split('.'))
        pp = datetime( p_year, p_mm, p_day)

        #td = 28*terms_dict[p_type]
        ##p_plus = timedelta(days=28*terms_dict[p_type])
        p_after = pp + relativedelta(months=terms_dict[p_type])

        #print(p_after)

        if ttoday >= p_after:
            #print(i,': ',p_after)
            answer.append(i+1)


    print(answer)
    return answer




##today = "2022.05.19"
##terms = ["A 6", "B 12", "C 3"]
##privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z",
             "2019.08.02 D", "2019.07.01 D","2018.12.28 D"]
solution(today, terms, privacies)
