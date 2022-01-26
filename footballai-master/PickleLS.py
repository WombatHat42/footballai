import pickle
import os.path

def saveObj(obj, filename):
    filename = filename + '.obj'
    fileObj = open(filename, 'wb')
    pickle.dump(obj,fileObj)
    fileObj.close()
    
def loadObj(filename):
    fileSw = False
    fileCheck = True
    while fileSw != True:
        if fileCheck == False:
            print("\n**Error** | No such file exists")
            print("Enter name without file type and without quotes: filename")
            filename = input("\nPlease Re-enter file name: ")
            print("\nLoading...")
        filename = filename + '.obj'
        fileCheck = os.path.exists(filename)
        if fileCheck == True:
            fileObj = open(filename, 'rb')
            loadedObj = pickle.load(fileObj)
            fileObj.close()
            fileSw = True
    return loadedObj
