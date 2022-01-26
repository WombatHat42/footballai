# Artifical Inteligence: Defensive Coordinator

## Overview
This system is designed to run a simulation of a drive in a football game between the user(offense) and the AI agent(Defense).

Things that you will be able to do in this system are:
* Train your own Artifical Intelligence agent
   * There will be already trained AI agents in the repository
* Save and load the agent you've trained
* Be able to play a drive against the AI agent

## Installation
You will need to install the lastest version of [python](https://www.python.org/downloads/).

You will also need to use the package manager [pip](https://www.w3schools.com/python/python_pip.asp) to install [numpy](https://numpy.org/install/).

```bash
pip install numpy
```

## How to Start
1. Download all the files in the repository to the same directory on your computer 
   1. This could or could not include the .obj files(These are already trained AI agents)
1. Run the FballUserInterface.py
1. Select an option
   1. To train an AI agent
   1. Load or save a .obj file(Already trained agent or what you chose to name your own trained agent)
   1. Play a drive against an AI agent of your choosing

## Example Run 
When you run FballUserInterface.py you should see this:

```python
Hello, this interface is used to train, save, and load neural network objects
along with playing a football drive against an AI defense
Also expand your window until menu is a rectangle for best view of print statements
//////////////////////////////////////////////////////////////////////////////////////////////////
|OPTIONS:                                                                                        |
|NOTE -- SUB OPTIONS OCCUR AFTER THE OPTION MENTIONED                                            |
|option 1: Train                                                                                 |
|-----option 1 a: Load: load an existing neural network object                                   |
|-----option 1 b: Create: create a neural network and enter establish its architecture and values|
|----------option 1b1 a: full backwards propagation neural network                               |
|----------option 1b2 b: two perceptron backwards propagation neural network                     |
|----------option 1b2 c: extra details                                                           |
|-----option 1 c: Continue with current neural network                                           |
|----------option 1c 1: Change Learning Rate:                                                    |
|----------option 1c 2: No change:                                                               |
|sub option 1: Train Type                                                                        |
|-----option s1 a: High School Coach Training(grades of 2's, 3's, and 4's,)                      |
|----------option s1a 1: Regular train                                                           |
|---------------option s1a1 a: Continuous Run                                                    |
|---------------option s1a1 b: Escape Run                                                        |
|----------option s1a 2: Factor train                                                            |
|---------------option s1a2 a: Continuous Run                                                    |
|---------------option s1a2 b: Escape Run                                                        |
|-----option s1 b: College Coach Training(grades 3's and 4's,)                                   |
|----------option s1b 1: Regular train                                                           |
|---------------option s1b1 a: Continuous Run                                                    |
|---------------option s1b1 b: Escape Run                                                        |
|----------option s1b 2: Factor train                                                            |
|---------------option s1b2 a: Continuous Run                                                    |
|---------------option s1b2 b: Escape Run                                                        |
|-----option s1 c: NFL Coach Training(grades of 4's,)                                            |
|----------option s1c 1: Regular train                                                           |
|---------------option s1c1 a: Continuous Run                                                    |
|---------------option s1c1 b: Escape Run                                                        |
|----------option s1c 2: Factor train                                                            |
|---------------option s1c2 a: Continuous Run                                                    |
|---------------option s1c2 b: Escape Run                                                        |
|option 2: Play Drive                                                                            |
|-----option 2 a: AI Player Difficulty Level                                                     |
|----------Difficulty 1: AI NFL Coach                                                            |
|----------Difficulty 2: AI College Coach                                                        |
|----------Difficulty 3: AI High School Coach                                                    |
|-----option 2 b: Test Your AI                                                                   |
|----------Test a: load a neural network to test                                                 |
|----------Test b: Use currently loaded neural network                                           |
|option 3: Save                                                                                  |
|option 4: Load                                                                                  |
|option 5: Show Neural Network Weights                                                           |
|option 6: Show Neural Networks recent sigmoid values                                            |
|option X: Exit                                                                                  |
|option M: Print Menu again                                                                      |
//////////////////////////////////////////////////////////////////////////////////////////////////

option 1: Train
option 2: Play Drive
option 3: Save
option 4: Load
option 5: Show Neural Network Weights
option 6: Show Neural Networks recent sigmoid values
option X: Exit
option M: Print Menu again

What process would you like to run:
```

Then lets load in an existing trained AI. So type in the number 4, for the process you want to run then it will ask for the file name. Lets go with the college coach object. 

```python
What process would you like to run: 4
Please enter file name similar to 'filename' without quotes, leave out file type as well: COLcoach

Loading...
...Done

option 1: Train
option 2: Play Drive
option 3: Save
option 4: Load
option 5: Show Neural Network Weights
option 6: Show Neural Networks recent sigmoid values
option X: Exit
option M: Print Menu again

What process would you like to run:
```

From here you can select option 2 and then option b to load in the currently loaded AI. Then the drive will begin.
```python
What process would you like to run: 2

__Difficulty Levels__
Difficulty 1: AI NFL Coach
Difficulty 2: AI College Coach
Difficulty 3: AI High School Coach

__Test AI__
option a: load a neural network to test
option b: use currently loaded neural network

Select Difficuly: 1, 2, or 3 or select Test option: a or b: b
Down: 1
To Go: 10
Yard Line: 79
 
+--------------------------------------------------+
| 1: shortThrowL | 2: shortThrowR | 3: shortThrowM |
|----------------|----------------|----------------|
| 4: deepThrowL  | 5: deepThrowR  | 6: deepThrowR  |
|----------------|----------------|----------------|
| 7: runL        | 8: runM        | 9: runR        |
+--------------------------------------------------+
Select a number from the Offensive Playbook:
```

