import NN_4 as nn4
import NN_3 as nn3
import PickleLS
import driveSim
import NetworkTrain_V1
import NetworkTrain_V2
import NetworkTrain_V3

switch = False

print('Hello, this interface is used to train, save, and load neural network objects')
print('along with playing a football drive against an AI defense')
print('Also expand your window until menu is a rectangle for best view of print statements')
neuralNet = ''
    
def menu():
    print('//////////////////////////////////////////////////////////////////////////////////////////////////')
    print("|OPTIONS:                                                                                        |")
    print("|NOTE -- SUB OPTIONS OCCUR AFTER THE OPTION MENTIONED                                            |")
    print("|option 1: Train                                                                                 |")
    print("|-----option 1 a: Load: load an existing neural network object                                   |")    
    print("|-----option 1 b: Create: create a neural network and enter establish its architecture and values|")
    print("|----------option 1b1 a: full backwards propagation neural network                               |")
    print("|----------option 1b2 b: two perceptron backwards propagation neural network                     |")
    print("|----------option 1b2 c: extra details                                                           |")
    print("|-----option 1 c: Continue with current neural network                                           |")
    print("|----------option 1c 1: Change Learning Rate:                                                    |")
    print("|----------option 1c 2: No change:                                                               |")
    print("|sub option 1: Train Type                                                                        |")
    print("|-----option s1 a: High School Coach Training(grades of 2's, 3's, and 4's,)                      |")
    print("|----------option s1a 1: Regular train                                                           |")
    print("|---------------option s1a1 a: Continuous Run                                                    |")
    print("|---------------option s1a1 b: Escape Run                                                        |")
    print("|----------option s1a 2: Factor train                                                            |")
    print("|---------------option s1a2 a: Continuous Run                                                    |")
    print("|---------------option s1a2 b: Escape Run                                                        |")      
    print("|-----option s1 b: College Coach Training(grades 3's and 4's,)                                   |")
    print("|----------option s1b 1: Regular train                                                           |")
    print("|---------------option s1b1 a: Continuous Run                                                    |")
    print("|---------------option s1b1 b: Escape Run                                                        |")
    print("|----------option s1b 2: Factor train                                                            |")
    print("|---------------option s1b2 a: Continuous Run                                                    |")
    print("|---------------option s1b2 b: Escape Run                                                        |")
    print("|-----option s1 c: NFL Coach Training(grades of 4's,)                                            |")
    print("|----------option s1c 1: Regular train                                                           |")
    print("|---------------option s1c1 a: Continuous Run                                                    |")
    print("|---------------option s1c1 b: Escape Run                                                        |")
    print("|----------option s1c 2: Factor train                                                            |")
    print("|---------------option s1c2 a: Continuous Run                                                    |")
    print("|---------------option s1c2 b: Escape Run                                                        |")
    print("|option 2: Play Drive                                                                            |")
    print("|-----option 2 a: AI Player Difficulty Level                                                     |")
    print("|----------Difficulty 1: AI NFL Coach                                                            |")
    print("|----------Difficulty 2: AI College Coach                                                        |")
    print("|----------Difficulty 3: AI High School Coach                                                    |")
    print("|-----option 2 b: Test Your AI                                                                   |")
    print("|----------Test a: load a neural network to test                                                 |")
    print("|----------Test b: Use currently loaded neural network                                           |")
    print("|option 3: Save                                                                                  |")
    print("|option 4: Load                                                                                  |")
    print("|option 5: Show Neural Network Weights                                                           |")
    print("|option 6: Show Neural Networks recent sigmoid values                                            |")
    print("|option X: Exit                                                                                  |")
    print("|option M: Print Menu again                                                                      |")
    print('//////////////////////////////////////////////////////////////////////////////////////////////////')
    
def learnRateSet(neuralNet, sw):
    if sw == False:
        rate = float(input("What would you like the learning rate to be for this neural network: "))
        neuralNet.newLearnRate(rate)
    if sw == True:
        select = input("\nWould you like to change the learning rate(y/n): ").lower()
        if select == 'y':
            rate = float(input("What would you like the learning rate to be for this neural network: "))
            neuralNet.newLearnRate(rate)
            
def trainType(neuralNet, coachType):
    print("\n__IMPORTANT NOTES__")
    print('-Training will use a csv file with 42,187 lines of data. You will enter a range for what part of the csv file you want to use for training')
    print('-Progress reports will happen every 100,000 backwards propagations')
    print('-The best scoring neural network will auto-save as well')
          
    switch = False
    while switch != True:
        print("\noption 1: Regular train")
        print("option 2: Factor train")
        print("option 3: Extra Details")
        opt = input('\nSelect 1, 2, or 3: ')
        if opt == '1':
            print("\n__Extra Details__")
            print("-Continuous means it will train until the neural network gets every playcall right")
            print("-Escape means you will be asked if you want to stop after each progress report")
            print("\noption a: Continuous Run")
            print("option b: Escape Run")
            opt2 = input('\nSelect a or b: ').lower()
            if opt2 == 'a':
                print("\n__IMPORTANT NOTES__")
                print('Starting range value must be greater than -1 and ending value must be less than 42,587')
                rng1 = int(input('\nPlease select start value of range: ').replace(',',''))
                rng2 = int(input('Please select ending value of range: ').replace(',',''))
                if rng2 <= rng1:
                    print('**ERROR** | Invalid Range, please try again')
                elif rng1 <0 or rng2 > 42586:
                    print('**ERROR** | Invalid Range, please try again')
                else:
                    if coachType == 'a':
                        NetworkTrain_V3.nn_train_time(neuralNet, rng1, rng2, False)
                        print("\n...Finished Training")
                        switch = True

                    elif coachType == 'b':
                        NetworkTrain_V2.nn_train_time(neuralNet, rng1, rng2, False)
                        print("\n...Finished Training")
                        switch = True

                    elif coachType == 'c':
                        NetworkTrain_V1.nn_train_time(neuralNet, rng1, rng2, False)
                        print("\n...Finished Training")
                        switch = True
                        
            elif opt2 == 'b':
                print("\n__IMPORTANT NOTES__")
                print('Starting range value must be greater than -1 and ending value must be less than 42,187')
                rng1 = int(input('\nPlease select start value of range: ').replace(',',''))
                rng2 = int(input('Please select ending value of range: ').replace(',',''))
                if rng2 <= rng1:
                    print('**ERROR** | Invalid Range, please try again')
                elif rng1 <0 or rng2 > 42586:
                    print('**ERROR** | Invalid Range, please try again')
                else:
                    if coachType == 'a':
                        NetworkTrain_V3.nn_train_time(neuralNet, rng1, rng2, True)
                        print("\n...Finished Training")
                        switch = True

                    elif coachType == 'b':
                        NetworkTrain_V2.nn_train_time(neuralNet, rng1, rng2, True)
                        print("\n...Finished Training")
                        switch = True

                    elif coachType == 'c':
                        NetworkTrain_V1.nn_train_time(neuralNet, rng1, rng2, True)
                        print("\n...Finished Training")
                        switch = True

            else:
                print('**ERROR** | Incorrect response, please try again')

        elif opt == '2':
            print("\noption a: Continuous Run")
            print("option b: Escape Run")
            print("\n__Extra Details__")
            print("-Continuous means it will train until the neural network gets every playcall right")
            print("-Escape means you will be asked if you want to stop after each progress report")
            opt2 = input('\nSelect a or b: ').lower()
            if opt2 == 'a':
                print("\n__IMPORTANT NOTES__")
                print('Starting range value must be greater than -1 and ending value must be less than 42,187')
                rng1 = int(input('\nPlease select start value of range: ').replace(',',''))
                rng2 = int(input('Please select ending value of range: ').replace(',',''))
                factor = int(input('Please enter factor you want to train by: '))
                if rng2 <= rng1:
                    print('**ERROR** | Invalid Range, please try again')
                elif rng1 <0 or rng2 > 42586:
                    print('**ERROR** | Invalid Range, please try again')
                else:
                    if coachType == 'a':
                        NetworkTrain_V3.factor_train(neuralNet, rng1, rng2, factor, False)
                        print("\n...Finished Training")
                        switch = True

                    elif coachType == 'b':
                        NetworkTrain_V2.factor_train(neuralNet, rng1, rng2, factor, False)
                        print("\n...Finished Training")
                        switch = True

                    elif coachType == 'c':
                        NetworkTrain_V1.factor_train(neuralNet, rng1, rng2, factor, False)
                        print("\n...Finished Training")
                        switch = True
                        
            elif opt2 == 'b':
                print("\n__IMPORTANT NOTES__")
                print('Starting range value must be greater than -1 and ending value must be less than 42,187')
                rng1 = int(input('\nPlease select start value of range: ').replace(',',''))
                rng2 = int(input('Please select ending value of range: ').replace(',',''))
                factor = int(input('Please enter factor you want to train by: '))
                if rng2 <= rng1:
                    print('**ERROR** | Invalid Range, please try again')
                elif rng1 <0 or rng2 > 42586:
                    print('**ERROR** | Invalid Range, please try again')
                else:
                    if coachType == 'a':
                        NetworkTrain_V3.factor_train(neuralNet, rng1, rng2, factor, True)
                        print("\n...Finished Training")
                        switch = True

                    elif coachType == 'b':
                        NetworkTrain_V2.factor_train(neuralNet, rng1, rng2, factor, True)
                        print("\n...Finished Training")
                        switch = True

                    elif coachType == 'c':
                        NetworkTrain_V1.factor_train(neuralNet, rng1, rng2, factor, True)
                        print("\n...Finished Training")
                        switch = True
            else:
                print('**ERROR** | Incorrect response, please try again')

        elif opt == '3':
            print("\n__Extra Details__")
            print("-Regular train will go through the data range one by one backwards propagating wrong playcalls")
            print("-Factor train will go through the data range in groups of the factor number")
            print(" ~Factor Train ex:range = 0 - 15, factor = 5, training -> 1-5, 5-10, 10-15")

        else:
            print('**ERROR** | Incorrect response, please try again')

def load():
    filename = input("Please enter file name similar to 'filename' without quotes, leave out file type as well: ")
    print("\nLoading...")
    neuralNet = PickleLS.loadObj(filename)
    print("...Done")
    return neuralNet
    
def save(neuralNet):
    filename = input("Please enter file name similar to 'filename' without quotes, leave out file type as well: ")
    print("\nSaving...")
    PickleLS.saveObj(neuralNet, filename)
    print("...Done")
            
menu()
neuralNet = ''
while switch != True:
    print("\noption 1: Train")
    print("option 2: Play Drive")
    print("option 3: Save")
    print("option 4: Load")
    print("option 5: Show Neural Network Weights")
    print("option 6: Show Neural Networks Recent Sigmoid Values")
    print("option X: Exit")
    print("option M: Print Menu again")
    
    inp = input('\nWhat process would you like to run: ')

    if inp == '1':
        switch1 = False
        while switch1 != True:
            print("\noption a: Load; load an existing neural network object")    
            print("option b: Create; create a neural network and enter establish its architecture and values")
            print("option c: Continue; continue with current neural network")
            
            inp1 = input('\nSelect a, b, or c: ').lower()
            if inp1 == 'a':
                neuralNet = load()
                learnRateSet(neuralNet, True)
                switch1 = True
                
            elif inp1 == 'b':
                num2 = int(input("How many perceptrons do you want in the input layer: "))##make print statement
                num3 = int(input("How many perceptrons do you want in the hidden layer: "))##make print statement
                typeSw = False
                while typeSw != True:
                    print("\noption a: Full backwards propagation neural network")
                    print("option b: Two perceptron backwards propagation neural network")
                    print("option c: Extra Details")
                    nntype = input('\nSelect a, b, or c: ').lower()
                    if nntype == 'a':
                        neuralNet = nn3.NeuralNetwork(5, num2, num3, ['43 blitz zone','43 blitz man','43 cover zone', '43 cover man',
                                             'nickel blitz zone','nickel blitz man','nickel cover zone','nickel cover man',
                                             'dime blitz zone','dime blitz man','dime cover zone','dime cover man'])
                        learnRateSet(neuralNet, False)
                        typeSw = True
                    elif nntype == 'b':
                        neuralNet = nn4.NeuralNetwork(5, num2, num3, ['43 blitz zone','43 blitz man','43 cover zone', '43 cover man',
                                             'nickel blitz zone','nickel blitz man','nickel cover zone','nickel cover man',
                                             'dime blitz zone','dime blitz man','dime cover zone','dime cover man'])
                        learnRateSet(neuralNet, False)
                        typeSw = True

                    elif nntype == 'c':
                        print("\n__Extra Details__")
                        print('-Full backprop or backwards propagation will calculate the error for every output layer perceptron')
                        print('-Two perceptron backprop will change only calculate the error of the perceptron that misfired and the perceptron that we wanted to fire') 
                              
                    else:
                        print('**ERROR** | Incorrect response, please enter again')
                switch1 = True

            elif inp1 == 'c':
                if neuralNet != '':
                    learnRateSet(neuralNet, True)
                    switch1 = True
                else:
                    print('**ERROR** | No current Neural Network being used')
                    
            else:
                print('**ERROR** | Incorrect response, please enter again')
                
        coach = False        
        while coach != True:
            print("\noption a: High School Coach Training(grades of 2's, 3's, and 4's,)") 
            print("option b: College Coach Training(grades 3's and 4's,)")
            print("option c: NFL Coach Training(grades of 4's,)")
            
            coachType = input('\nSelect a, b, or c: ').lower()
            if coachType == 'a':
                trainType(neuralNet, coachType)
                coach = True
                          
            elif coachType == 'b':
                trainType(neuralNet, coachType)
                coach = True

            elif coachType == 'c':
                trainType(neuralNet, coachType)
                coach = True
                          
            else:
                print('**ERROR** | Incorrect response, please enter again')

    elif inp == '2':
        switchP = False
        while switchP != True:
            print("\n__Difficulty Levels__")
            print("Difficulty 1: AI NFL Coach")
            print("Difficulty 2: AI College Coach")
            print("Difficulty 3: AI High School Coach")

            print("\n__Test AI__")
            print("option a: load a neural network to test")
            print("option b: use currently loaded neural network\n")
            
            opp = input("Select Difficuly: 1, 2, or 3 or select Test option: a or b: ")
            if opp == '1':
                NFLcoach = PickleLS.loadObj(NFLcoach)
                driveSim.driveSim(NFLcoach)
                switchP = True

            elif opp == '2':
                COLcoach = PickleLS.loadObj(COLcoach)
                driveSim.driveSim(COLcoach)
                switchP = True
                
            elif opp == '3':
                HScoach = PickleLS.loadObj(HScoach)
                driveSim.driveSim(HScoach)
                switchP = True

            elif opp == 'a':
                neuralNet = load()
                driveSim.driveSim(neuralNet)
                switchP = True

            elif opp == 'b':
                if neuralNet != '':
                    driveSim.driveSim(neuralNet)
                    switchP = True
                    
                else:
                    print('**ERROR** | No current Neural Network being used')
                    
            else:
                print('**ERROR** | Incorrect response, please enter again')

    elif inp == '3':
        save(neuralNet)

    elif inp == '4':
        neuralNet = load()
        
    elif inp == '5':
        if neuralNet != '':
            neuralNet.current_weights()
        else:
            print('**ERROR** | No current Neural Network being used\n')
        
    elif inp == '6':
        if neuralNet != '':
            if neuralNet.variation == 1:
                print("**ERROR** | You have to train before seeing sigmoid values")
            else:
                neuralNet.sigmoid_values()
            
        else:
            print('**ERROR** | No current Neural Network being used')
        
       
    elif inp == 'M' or inp == 'm':
        menu()

    elif inp == 'X' or inp == 'x':
        print('Goodbye')
        break

    else:
        print('**ERROR** | Incorrect response, please enter again')
