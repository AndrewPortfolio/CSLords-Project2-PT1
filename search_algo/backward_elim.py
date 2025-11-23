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
    best_score = rando_eval()

    # keep track of removed features
    removed_features = list()

    while len(current_features) > 1:
        # every iteration, see if we improved in performance
        feature_to_remove = None
        best_temp_score = best_score

        # try to remove each feature at once
        for f in current_features:
            candidate = [x for x in current_features if x != f]
            score = rando_eval() # for now, it is random

            if score > best_score_after_removal:
                best_score_after_removal = score
                feature_to_remove = f

        if feature_to_remove is not None:
            removed_features.append(feature_to_remove)
            current_features.remove(feature_to_remove)
        else:
            # if no feature is identified, break
            print("No more features to remove, finishing the Backward Elimination")
            break



    # after all, return the result of backward elimination
    return {
        "current_features": current_features,
        "best_score": best_score,
        "removed_features": removed_features,
    }