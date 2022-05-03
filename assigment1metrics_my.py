def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification
    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels
    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    TP, TN, FP, FN = 0, 0, 0, 0
    for i in range(len(prediction)):
      if (prediction[i] == True) and (ground_truth[i] == True):
        TP += 1
      if (prediction[i] == False) and (ground_truth[i] == False):
        TN += 1
      if (prediction[i] == False) and (ground_truth[i] == True):
        FP += 1
      if (prediction[i] == True) and (ground_truth[i] == False):
        FN += 1
    precision = TP /(TP + FP)
    recall = TP / (TP + FN)
    accuracy = TP / (TP + TN + FN + FP)
    f1 = 2 * (precision * recall) / (precision + recall)
    return precision, recall, f1, accuracy

def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification
    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels
    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    return 0
