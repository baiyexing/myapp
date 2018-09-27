def get_answers():
    with open('Exercises.txt',"r",encoding="gbk") as file:
        lines = file.readlines()
        list = ()
        for line in lines:
            answer = line.split('=')[1]
            answer1 = answer.replace(' ','')
            print(answer1)
            dic ={
                  'answer':   answer1
              }
            list.append(answer1)
        print(dic)
    return list
def check(list):
    with open('Answer.txt',"r",encoding="gbk") as f:
        lines = f.readlines()
        listA =[]
        correct=[]
        wrong=[]
        grade=[]
        for line in lines:
            right_answer = line.split('.')[1]
            right_answer1 = right_answer.replace(' ','')
            listA.append(right_answer1)
        i = 0
        if (i) < len(listA):
            for char in listA:
                if char != list[i]:
                    wrong.append(i+1)
                    i+=1
                elif char == list[i]:
                    correct.append(i+1)
                    i+=1
            grade.append(correct)
            grade.append(wrong)
        return grade
def write_grade(grade):
    G = open('Grade.txt',"w")
    print(grade[0])
    G.write('Correct:'+ str(len(grade[0])) + str(grade[0])+'\n'+ 'Wrong:'+ str(len(grade[1])) + str(grade[1])+'\n')
    G.close()

write_grade(check(get_answers()))
