from utils.eval_func import rando_eval

# “If I remove this feature, does my model get worse?”

# Intuition:
#   1. Starting with all features.
#   2. Repeatedly evaluating the model while removing one feature at a time.
#   3. Choosing the feature whose removal hurts performance the least, then remove it.
#   4. Stopping when no further removals improve performance.

def backward_elim(num_features):
    # get all features and eval of it
    current_features = list(range(num_features))
    best_score = rando_eval(current_features)

    # flag of improvement
    improved = True

    # every iteration, see if we improved in performance
    feature_to_remove = None
    best_temp_score = best_score



    # after all, return the result of backward elimination
    return {
        "current_features": current_features,
        "best_score": best_score,
        "improved": improved,
        "feature_to_remove": feature_to_remove,
        "best_temp_score": best_temp_score
    }