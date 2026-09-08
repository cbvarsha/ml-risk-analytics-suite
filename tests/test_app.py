from src.app import probability_default, confusion, population_stability
def test_risk_monotonicity(): assert probability_default(40000,.7,2,.9)>probability_default(90000,.2,0,.2)
def test_metrics(): assert confusion([0,1],[.1,.9])=={"tp":1,"tn":1,"fp":0,"fn":0}; assert population_stability([.5,.5],[.5,.5])==0
