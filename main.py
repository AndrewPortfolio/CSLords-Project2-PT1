from search_algo.forward_selection import forward_selection
from search_algo.backward_elim import backward_elim
from search_algo.cs_lords_special import special
from utils.eval_func import rando_eval


print("Welcome to CS Lords Feature Selection Algorithm!")

num_features = int(input("Please enter total number of features: "))

print("Type the number of the algorithm you want to run!")

selection_block = """
1. Forward Selection 
2. Backward Elimination 
3. CS Lords Special
"""
print(selection_block)

algorithm_choice = int(input("Enter your choice (1-3): ")) 

if algorithm_choice == 1:
    print("You have selected Forward Selection.")
    final_feats = forward_selection(num_features)
    accuracy = rando_eval()
    print("Accuracy: ", accuracy)
elif algorithm_choice == 2:
    print("You have selected Backward Elimination.")
    final_feats = backward_elim(num_features)
    accuracy = rando_eval()
    print("Accuracy: ", accuracy)
else:
    print("You have selected CS Lords Special.")
    final_feats = special(num_features) 
    accuracy = rando_eval()
    print("Accuracy: ", accuracy)   
