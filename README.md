# CSLords-Project2-PT1
Forward Selection and Backward Elimination

1. Greedy Forward Selection
    Initial State: {} 
    At each lvl it adds the remaining features one at a time 
    Each candidate set calls the evaluation function that returns a random score 
    Pick the feature with the best accuracy at that level 
    Add that feature permanently to your current set 
    Keeps track of the best feature throughout the entire process (all levels)
    Stop after you have tried all features 