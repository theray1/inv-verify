from TransitionSystem import TransitionSystem
from LogicalProposition import LogicalProposition
from util import isIncluded

t = TransitionSystem()



def verify(ts: TransitionSystem, phi: LogicalProposition):
    set_R = []
    stack_U = []
    b = True
    i = ts.get_initial_nodes()
    
    #I \ R = {} <=> isIncluded(i, set_R) === True
    while(b and isIncluded(i, set_R)):
        pass

verify(t);