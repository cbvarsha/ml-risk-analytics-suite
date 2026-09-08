import math

def sigmoid(x): return 1/(1+math.exp(-max(min(x,30),-30)))
def probability_default(income, debt_ratio, missed_payments, utilisation):
    logit=-3.4 - income/180000 + 3.1*debt_ratio + .72*missed_payments + 1.4*utilisation
    return round(sigmoid(logit),4)
def confusion(y_true, probabilities, threshold=.5):
    out={"tp":0,"tn":0,"fp":0,"fn":0}
    for actual,p in zip(y_true,probabilities):
        predicted=int(p>=threshold); out["tp" if actual and predicted else "tn" if not actual and not predicted else "fp" if predicted else "fn"]+=1
    return out
def population_stability(expected, actual):
    total=0.0
    for e,a in zip(expected,actual):
        e=max(e,1e-6); a=max(a,1e-6); total+=(a-e)*math.log(a/e)
    return round(total,4)

if __name__ == "__main__":
    probs=[probability_default(62000,.31,0,.45), probability_default(39000,.58,2,.91)]
    print({"probabilities":probs,"confusion":confusion([0,1],probs),"psi":population_stability([.2,.5,.3],[.16,.48,.36])})
