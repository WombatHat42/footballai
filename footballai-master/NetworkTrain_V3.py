import PickleLS
import Matrix
import time
import stats
    
def nn_train(neuralNet, num1, num2, num3, time1, var, maxEfficiency, filename, stopSW):
    masterList = stats.statList(num1,num2)
    count = 0
    
    bk = False
    while count != num2 - num1:

        if neuralNet.variation >= (100000 * var):
            if num3 > 0:
                print('PROGRESS REPORT #' + str(var))
                time2 = time.perf_counter()
                totalTime = float(time2) - float(time1)
                print(totalTime, 'Seconds')
                efficiency = nn_grade(neuralNet, 0, num3)
                if efficiency > maxEfficiency:
                    maxEfficiency = efficiency
                    PickleLS.saveObj(neuralNet, filename)
                print('Max Efficiency:', maxEfficiency)
                print('---------------------------------')
                if stopSW == True:
                    switch = False
                    while switch != True:
                        choice = input("Would you like to stop(y/n): ").lower()
                        if choice == 'y':
                            bk = True
                            print('Exiting...')
                            print('---------------------------------')
                            switch = True
                        elif choice == 'n':
                            print('Continuing...')
                            print('---------------------------------')
                            switch = True
                        else:
                            print("Invalid option, try again")
                        
                var += 1
            else:
                print('PROGRESS REPORT #' + str(var))
                time2 = time.perf_counter()
                totalTime = float(time2) - float(time1)
                print(totalTime, 'Seconds')
                efficiency = nn_grade(neuralNet, num1, num2)
                if efficiency > maxEfficiency:
                    maxEfficiency = efficiency
                    PickleLS.saveObj(neuralNet, filename)
                print('Max Efficiency:', maxEfficiency)
                if count == num2 - num1:
                    print('Total Error:', loss)
                else:
                    print('Current Error:', loss)
                print('---------------------------------')
                if stopSW == True:
                    switch = False
                    while switch != True:
                        choice = input("Would you like to stop(y/n): ").lower()
                        if choice == 'y':
                            bk = True
                            print('Exiting...')
                            print('---------------------------------')
                            switch = True
                        elif choice == 'n':
                            print('Continuing...')
                            print('---------------------------------')
                            switch = True
                        else:
                            print("Invalid option, try again")
                var += 1

        if bk == True:
            return bk
        count = 0
        counter = 1
        loss = 0
        for data in masterList:
            scenario = data[0]
            offense = data[1]
            defense = neuralNet.feedforward(scenario)
            grade = Matrix.grade(offense, defense)
            if grade == 0 or grade == 1:
                neuralNet.backprop(offense, defense, scenario)
                loss += neuralNet.loss
                counter += 1
            else:
                count += 1
    return bk

def nn_train_time(neuralNet, num1, num2, stopSW):
    filename = input("Please enter file name to autosave your trained neural network: ")
    print("\nNow Training...\n")
    print('__Starting Report__')
    var = (neuralNet.variation // 100000) + 1
    maxEfficiency = nn_grade(neuralNet, num1, num2)
    print('---------------------------------')
    time1 = time.perf_counter()
    nn_train(neuralNet, num1, num2, 0, time1, var, maxEfficiency, filename, stopSW)
        
    time2 = time.perf_counter()
    print('__Final Report__')
    print('Data Set:', (num2 - num1))

    totalTime = float(time2) - float(time1)
    print(totalTime, 'Seconds')
    nn_grade(neuralNet, num1, num2)

def nn_grade(neuralNet, num1, num2):
    masterList = stats.statList(num1,num2)
    
    print('Variation:', neuralNet.variation)
    print('LR:', neuralNet.learning_rate)

    grade4 = 0
    grade3 = 0
    grade2 = 0
    grade1 = 0
    grade0 = 0
    efficiency = 0
    eff = 0
    for data in masterList:
        scenario = data[0]
        offense = data[1]
        defense = neuralNet.feedforward(scenario)
        grade = Matrix.grade(offense, defense)
        if grade == 0:
            grade0 += 1
        elif grade == 1:
            grade1 += 1
        elif grade == 2:
            grade2 += 1
            efficiency += 1
            eff = efficiency
        elif grade == 3:
            grade3 += 1
            efficiency += 1
            eff = efficiency
        elif grade == 4:
            grade4 += 1
            efficiency += 1
            eff = efficiency
            
    print("Grade 4's:", grade4)
    print("Grade 3's:", grade3)
    print("Grade 2's:", grade2)
    print("Grade 1's:", grade1)
    print("Grade 0's:", grade0)
    print('Efficiency:', str(efficiency) + '/' + str(len(masterList)))
    return efficiency

def factor_train(neuralNet, num1, num2, factor, stopSW):
    switch = False
    while switch != True:
        if ((num2 - num1) % factor) != 0:
            print("Factor error, ((num2 - num1) % factor) must equal 0")
            factor = int(input('Please re-enter factor you want to train by: '))
        else:
            switch = True
            
    filename = input("Please enter file name to autosave your trained neural network: ")
    print("\nNow Training...\n")
    masterList = stats.statList(num1,num2)
    correctness = 0
    rng = 0
    print('__Starting Report__')
    num3 = int(num2 - num1)
    maxEfficiency = nn_grade(neuralNet, 0, num3)
    print('---------------------------------')
    time1 = time.perf_counter()
    
    while correctness != num2 - num1:
        correctness = 0

        var = (neuralNet.variation // 100000) + 1
        bk = nn_train(neuralNet, rng, (rng + factor), int(num2 - num1) , time1, var, maxEfficiency, filename, stopSW)
        if bk == True:
            break
        if (rng + factor) >= num2:
            rng = 0
        else:
            rng += factor
        
        for data in masterList:
        
            scenario = data[0]
            offense = data[1]
            defense = neuralNet.feedforward(scenario)
            grade = Matrix.grade(offense, defense)
            if 2 <= grade <= 4:
                correctness += 1

    print('__Final Report__')
    print('Data Set:', len(masterList))

    time2 = time.perf_counter()

    totalTime = float(time2) - float(time1)
    print(totalTime, 'Seconds')
    nn_grade(neuralNet, num1, num2)
