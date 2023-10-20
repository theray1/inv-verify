from TransitionSystem import TransitionSystem
from LogicalProposition import LogicalProposition
from TransitionSystem import Node
from util import is_included
from util import array1_without_array2

ts1 = TransitionSystem()
phi1 = LogicalProposition()

def verify(ts: TransitionSystem, phi: LogicalProposition):
    set_R = []
    stack_U = []
    b = True
    i = ts.get_initial_nodes()

    def visit(node: Node, node_stack: [], node_set: [], phi: LogicalProposition):
        node_stack.append(node)
        node_set.append(node)

        s_1 = node_stack[len(node_stack)-1]
        succesors = s_1.get_next_nodes()
        if(is_included(succesors, node_set)):
            node_stack.pop()
            b = b and False
            #False should be replaced by (s_1 |= phi)
        else:
            s_2 = array1_without_array2(succesors, node_set)
            node_stack.append(s_2)
            node_set.append(s_2)

        while False :
            #False should be replaced (U = epsilon) or !b
            s_1 = node_stack[len(node_stack)-1]
            succesors = s_1.get_next_nodes()
            if(is_included(succesors, node_set)):
                node_stack.pop()
                b = b and False
                #False should be replaced by (s_1 |= phi)
            else:
                s_2 = array1_without_array2(succesors, node_set)
                node_stack.append(s_2)
                node_set.append(s_2)

    #I \ R = {} <=> isIncluded(i, set_R) === True
    while(b and is_included(i, set_R)):
        s = array1_without_array2(i, set_R)
        visit(s)

    return True, stack_U 
    

verify(ts1, phi1);