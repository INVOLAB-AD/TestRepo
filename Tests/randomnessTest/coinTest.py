outcomes = []
prediction = 0
timer = 0
predict = ''
previous=''
prnt = 'H'
prnt2 = 'T'
times = int(input("Enter the number of times: "))
times2 = int(input("Enter the number of rounds: "))

for i in range(times):
    outcomes.append({'H':0,'T':0})

for i in range(times2):
    print("Round: ",i+1)
    for j in range(times):
        inp = input("H or T: ")
        outcomes[j][inp]+=1

        if predict==inp:
            prediction+=1
        
        if prediction<(timer-(times*0.4)):
            temp = prnt
            prnt = prnt2
            prnt2 = temp
        
        if outcomes[j]['H']>outcomes[j]['T']:
            timer += 1
            print("Prediction: ",prnt)
            predict=prnt
        elif outcomes[j]['H']<outcomes[j]['T']:
            timer += 1
            print("Prediction: ",prnt2)
            predict=prnt2
        else:
            print("Prediction: ",previous)
            timer+=1
        previous = inp

print(prediction,', ',timer)
print("Prediction Percentage is: ",(prediction/timer)*100)


