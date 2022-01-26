def statList(num1, num2):
    inputFile = open('SimplfiedStats-2019.csv','r')
    inputFile.readline()
    master_list = []
    word = "RIGHT"
    word1 = "LEFT"
    word2 = "MIDDLE"
    word3 = "CENTER"
    distance = "SHORT"
    distance1 = "DEEP"
    yardLine = 0

    for line in inputFile:
        quarter,minute,second,down,togo,seriesFirstDown,yards,formation,playType,PassType,rushDirection,yardLineFixed,lineDirection = line.split(',')
        playCall = ""
        if playType == "PASS" or playType == "RUSH":
            if playType == "PASS":
                if distance in PassType:
                    if word in PassType:
                        playCall = "shortThrowR"

                    if word1 in PassType:
                        playCall = "shortThrowL"

                    if word2 in PassType:
                        playCall = "shortThrowM"
                        
                if distance1 in PassType:
                    if word in PassType:
                        playCall = "deepThrowR"

                    if word1 in PassType:
                        playCall = "deepThrowL"

                    if word2 in PassType:
                        playCall = "deepThrowM"


            if playType == "RUSH":
                if word in rushDirection:
                    playCall = "runR"

                if word1 in rushDirection:
                    playCall = "runL"

                if word3 in rushDirection:
                    playCall = "runM"

        if lineDirection == "OWN":
            yardLine = (50 - int(yardLineFixed)) + 50

        else:
            yardLine = int(yardLineFixed)
      

        if playCall != "":
            master_list.append([(float(quarter),float(minute),float(down),float(togo),float(yardLine)),playCall])


    return master_list[num1:num2]
    

