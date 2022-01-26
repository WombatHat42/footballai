import random

def driveSim(neuralNet):
    def yardsGained(grade):
        ##Basically the lottery function
        outputList = []

        ##CODED FROM THE MATRIX SOREADSHEET
        if grade == 0:
            for x in range(65):
                yardsGained = random.randint(30,100)
                outputList.append(yardsGained)
                
            for y in range(20):
                yardsGained = random.randint(20,29)
                outputList.append(yardsGained)

            for z in range(10):
                yardsGained = random.randint(10,19)
                outputList.append(yardsGained)

            for i in range(5):
                yardsGained = random.randint(6,9)
                outputList.append(yardsGained)

            yardsGained = random.randint(2,5)
            outputList.append(yardsGained)
            yardsGained = random.randint(-2,1)
            outputList.append(yardsGained)

        if grade == 1:
            for x in range(9):
                yardsGained = random.randint(30,100)
                outputList.append(yardsGained)
                
            for y in range(65):
                yardsGained = random.randint(20,29)
                outputList.append(yardsGained)

            for z in range(20):
                yardsGained = random.randint(10,19)
                outputList.append(yardsGained)

            for i in range(3):
                yardsGained = random.randint(6,9)
                outputList.append(yardsGained)
                
            for h in range(2):
                yardsGained = random.randint(2,5)
                outputList.append(yardsGained)
                
            yardsGained = random.randint(-2,1)
            outputList.append(yardsGained)

        if grade == 2:
            for x in range(5):
                yardsGained = random.randint(30,100)
                outputList.append(yardsGained)
                
            for y in range(15):
                yardsGained = random.randint(20,29)
                outputList.append(yardsGained)

            for z in range(24):
                yardsGained = random.randint(10,19)
                outputList.append(yardsGained)

            for i in range(33):
                yardsGained = random.randint(6,9)
                outputList.append(yardsGained)
                
            for h in range(18):
                yardsGained = random.randint(2,5)
                outputList.append(yardsGained)
                
            for l in range(5):   
                yardsGained = random.randint(-2,1)
                outputList.append(yardsGained)
                
        if grade == 3:
            for x in range(1):
                yardsGained = random.randint(30,100)
                outputList.append(yardsGained)
                
            for y in range(2):
                yardsGained = random.randint(20,29)
                outputList.append(yardsGained)

            for z in range(3):
                yardsGained = random.randint(10,19)
                outputList.append(yardsGained)

            for i in range(20):
                yardsGained = random.randint(6,9)
                outputList.append(yardsGained)
                
            for h in range(65):
                yardsGained = random.randint(2,5)
                outputList.append(yardsGained)
                
            for l in range(9):
                yardsGained = random.randint(-2,1)
                outputList.append(yardsGained)

        if grade == 4:
            for x in range(1):
                yardsGained = random.randint(30,100)
                outputList.append(yardsGained)
                
            for y in range(1):
                yardsGained = random.randint(20,29)
                outputList.append(yardsGained)

            for z in range(5):
                yardsGained = random.randint(10,19)
                outputList.append(yardsGained)

            for i in range(8):
                yardsGained = random.randint(6,9)
                outputList.append(yardsGained)
                
            for h in range(20):
                yardsGained = random.randint(2,5)
                outputList.append(yardsGained)
                
            for l in range(65):  
                yardsGained = random.randint(-2,1)
                outputList.append(yardsGained)
            ##CODED FROM THE MATRIX SPREADSHEET
        RanIndex = random.randint(0,len(outputList)-1)        
        return outputList[RanIndex]

    def kickoff():
        output = []
        for x in range(80):
            Kreturn = random.randint(75,80)         
            output.append(Kreturn)
        for x in range(5):
            Kreturn = random.randint(80,99)
            output.append(Kreturn)
        for x in range(15):
            Kreturn = 100
            output.append(Kreturn)
            
        randIndex = random.randint(0,len(output)-1)
        start = output[randIndex]
        if start == 100:
            return 75
        else:
            return start

    def grade(offPlay,defPlay):
        defPlays = [['43 blitz zone',0,0,1,0,1,0,3,4,3],['43 blitz man',1,1,0,1,0,1,4,3,4],['43 cover zone',1,1,2,1,2,1,2,3,2],
                ['43 cover man',2,2,1,2,1,2,3,2,3],['nickel blitz zone',2,2,3,1,2,1,2,3,2],['nickel blitz man',3,3,2,2,1,2,3,2,3],
                ['nickel cover zone',3,3,4,2,3,2,1,2,1],['nickel cover man',4,4,3,3,2,3,2,1,2],
                ['dime blitz zone',1,1,2,2,3,2,1,2,1],['dime blitz man',2,2,1,3,2,3,2,1,2],['dime cover zone',2,2,3,3,4,3,0,1,0],
                ['dime cover man',3,3,2,4,3,4,1,0,1]]
        offPlays = [None,'shortThrowL', 'shortThrowR','shortThrowM','deepThrowL', 'deepThrowR','deepThrowM','runL','runM','runR']

        z = 0
        for x in range(len(offPlays)):
            if offPlays[x]==offPlay:
                for y in range(len(defPlays)):
                    if defPlays[y][0] == defPlay:
                        return defPlays[y][x]
                

    def drive():
        ##THIS IS WHERE THE NN WOULD COME INTO PLACE
        ##PUTTING IN RANDOM PLAYS AGAINST EACH OTHER TO SEE IF IT WORKS
        offPlays = ['shortThrowL', 'shortThrowR','shortThrowM','deepThrowL', 'deepThrowR','deepThrowM','runL','runM','runR']
        defPlays = ['43 blitz zone','43 blitz man','43 cover zone','43 cover man','nickel blitz zone','nickel blitz man','nickel cover zone',
                    'nickel cover man','dime blitz zone','dime blitz man','dime cover zone','dime cover man']
        ##THIS IS WHERE THE NN WOULD COME INTO PLACE
        ##PUTTING IN RANDOM PLAYS AGAINST EACH OTHER TO SEE IF IT WORKS
        quarter = random.randint(0,4)
        minute = random.randint(0,15)
        yardline = kickoff()
        down = 1
        toGo = 10
        plays = 0
        yards = 0
        driveSummary = []
  

        while down <= 4:
            outcome = ''
            offensivePlayStr = ""
            selectNo = 1
            scenario = quarter,minute,down,toGo,yardline
            ##THIS IS WHERE THE NN WOULD COME INTO PLACE
            ##PUTTING IN RANDOM PLAYS AGAINST EACH OTHER TO SEE IF IT WORKS
            
           
            ##THIS IS WHERE THE NN WOULD COME INTO PLACE
            ##PUTTING IN RANDOM PLAYS AGAINST EACH OTHER TO SEE IF IT WORKS
            
            print("Down:",down)
            print("To Go:",toGo)
            print("Yard Line:",yardline)
            print(" ")
            for offensivePlay in offPlays:
                selectNo = str(selectNo)
                offensivePlay = selectNo + " - " + offensivePlay
                offensivePlayStr =  offensivePlayStr + ", " +  offensivePlay
                selectNo = int(selectNo)
                selectNo += 1
                
            print('+--------------------------------------------------+')
            print('| 1: shortThrowL | 2: shortThrowR | 3: shortThrowM |')
            print('|----------------|----------------|----------------|')
            print('| 4: deepThrowL  | 5: deepThrowR  | 6: deepThrowR  |')
            print('|----------------|----------------|----------------|')
            print('| 7: runL        | 8: runM        | 9: runR        |')
            print('+--------------------------------------------------+')
            currentPlay = input("Select a number from the Offensive Playbook: ")
            playGrade = grade(offPlays[int(currentPlay)-1],neuralNet.feedforward(scenario))
            yardsGainedPlay = yardsGained(playGrade)

            
            if yardsGainedPlay >= yardline:
                outcome = "TOUCHDOWN"
                yardsGainedPlay = yardline
                plays += 1
                yards += yardsGainedPlay
                print("Yards Gained on the Play:",yardsGainedPlay)
                driveSummary.append(playSummary(offPlays[int(currentPlay)-1],yardsGainedPlay,down,toGo))
                break
            else:
                driveSummary.append(playSummary(offPlays[int(currentPlay)-1],yardsGainedPlay,down,toGo))
                if yardsGainedPlay > toGo:
                    yardline -= yardsGainedPlay
                    if yardline >= 10:
                        down = 1
                        toGo = 10
                    else:
                        down = 1
                        toGo = yardline

                else:
                    yardline -= yardsGainedPlay
                    down += 1
                    toGo -= yardsGainedPlay
                plays += 1
                yards += yardsGainedPlay
                if plays % 2 == 0 and minute == 0 and quarter == 4:
                    minute == 0
                elif plays % 2 == 0 and minute == 0 and quarter != 4:
                    minute = 15
                    quarter += 1
                elif plays % 2 and minute!= 0:
                    minute -= 1
                print("Yards Gained on the Play:",yardsGainedPlay)
                
        if outcome == 'TOUCHDOWN':
            driveSummary[-1] = driveSummary[-1] + ' ' + 'TOUCHDOWN'
            print("TOUCHDOWN")

        else:
            driveSummary[-1] = driveSummary[-1] + ' ' + 'TOD'
            print("Turnover on Downs")

        print("DRIVE SUMMARY:")
        for x in driveSummary:
            print(x)
        print(plays,'','Plays','',yards,'','Yards')
        

    def playSummary(offPlay,yardsGained,down,toGo):
        down = str(down)
        toGo = str(toGo)
        yardsGained = str(yardsGained)
        playSummary = ''
        if offPlay == 'shortThrowL':
            playSummary = down + ' & ' + toGo + ' ' + 'Short Throw Left' + ' ' + yardsGained + ' yards'

        elif offPlay == 'shortThrowR':
            playSummary = down + ' & ' + toGo + ' ' + 'Short Throw Right' + ' ' + yardsGained + ' yards'

        elif offPlay == 'shortThrowM':
            playSummary = down + ' & ' + toGo + ' ' + 'Short Throw Middle' + ' ' + yardsGained + ' yards'

        elif offPlay == 'deepThrowL':
            playSummary = down + ' & ' + toGo + ' ' + 'Deep Throw Left' + ' ' + yardsGained + ' yards'

        elif offPlay == 'deepThrowR':
            playSummary = down + ' & ' + toGo + ' ' + 'Deep Throw Right' + ' ' + yardsGained + ' yards'

        elif offPlay == 'deepThrowM':
            playSummary = down + ' & ' + toGo + ' ' + 'Deep Throw Middle' + ' ' + yardsGained + ' yards'

        elif offPlay == 'runL':
            playSummary = down + ' & ' + toGo + ' ' + 'Run Left' + ' ' + yardsGained + ' yards'

        elif offPlay == 'runR':
            playSummary = down + ' & ' + toGo + ' ' + 'Run Right' + ' ' + yardsGained + ' yards'

        elif offPlay == 'runM':
            playSummary = down + ' & ' + toGo + ' ' + 'Run Middle' + ' ' + yardsGained + ' yards'

        return playSummary

    drive()



        
        
        
        

    
        
        
        
    
