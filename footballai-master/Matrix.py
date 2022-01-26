
global offPlays
global defPlays
    
offPlays = [None,'shortThrowL', 'shortThrowR','shortThrowM','deepThrowL', 'deepThrowR','deepThrowM','runL','runM','runR']
defPlays = [['43 blitz zone',0,0,1,0,1,0,3,4,3],['43 blitz man',1,1,0,1,0,1,4,3,4],['43 cover zone',1,1,2,1,2,1,2,3,2],
            ['43 cover man',2,2,1,2,1,2,3,2,3],['nickel blitz zone',2,2,3,1,2,1,2,3,2],['nickel blitz man',3,3,2,2,1,2,3,2,3],
            ['nickel cover zone',3,3,4,2,3,2,1,2,1],['nickel cover man',4,4,3,3,2,3,2,1,2],
            ['dime blitz zone',1,1,2,2,3,2,1,2,1],['dime blitz man',2,2,1,3,2,3,2,1,2],['dime cover zone',2,2,3,3,4,3,0,1,0],
            ['dime cover man',3,3,2,4,3,4,1,0,1]]

def fitness(offPlay):
    z = 0
    for x in range(len(offPlays)):
        if offPlays[x]==offPlay:
            for y in range(len(defPlays)):
                if defPlays[y][x] == 4:
                    return defPlays[y][0]
                z += 1

def expected(offPlay):
    expectedList = []
    for x in range(len(offPlays)):
        if offPlays[x]==offPlay:
            for y in range(len(defPlays)):
                expectedList.append(defPlays[y][x])
    return expectedList

def grade(offPlay, defPlay):
    z = 0
    for x in range(len(offPlays)):
        if offPlays[x]==offPlay:
            for y in range(len(defPlays)):
                if defPlays[y][0] == defPlay:
                    return defPlays[y][x]

    

