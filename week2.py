def predictor_case(row, pred, target):
    actual = row[target]
    prediction = row[pred]
    if actual == 0 and prediction == 0:
        case = 'true_negative'
    elif actual == 1 and prediction == 1:
        case = 'true_positive'
    elif actual == 1 and prediction == 0:
        case = 'false_negative'
    else:
        case = 'false_positive'
    return case

def f1(cases):
    #the heart of the matrix
    tp = cases['true_positive']
    fn = cases['false_negative']
    tn = cases['true_negative']
    fp = cases['false_positive']
    
    #other measures we can derive
    recall = 1.0*tp/(tp+fn)  # positive correct divided by total positive in the table
    precision = 1.0*tp/(tp+fp) # positive correct divided by all positive predictions made
    f1 = 2/(1/recall + 1/precision)
    return f1

def informedness(cases):
    tp = cases['true_positive']
    fn = cases['false_negative']
    tn = cases['true_negative']
    fp = cases['false_positive']
    recall = 1.0*tp/(tp+fn)  # positive correct divided by total positive in the table
    specificty = 1.0*tn/(tn+fp) # negative correct divided by total negative in the table
    J = (recall + specificty) - 1
    return J

def accuracy(cases):
    tp = cases['true_positive']
    tn = cases['true_negative']
    fp = cases['false_positive']
    fn = cases['false_negative']
    return 1.0*(tp + tn)/(tp+tn+fp+fn)