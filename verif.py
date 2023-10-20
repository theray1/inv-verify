from TransitionSystem import TransitionSystem
from LogicalProposition import AndOperator
from LogicalProposition import OrOperator
from LogicalProposition import NotOperator
from LogicalProposition import IdentityOperator
from LogicalProposition import LogicalProposition
from TransitionSystem import Node
from util import is_included_in
from util import content_of_without
from util import print_trace

def verify(ts: TransitionSystem, phi: LogicalProposition) -> tuple[bool, list[Node]]:
    stack_U: list[Node] = []
    set_R: list[Node] = []
    flag_bool = True
    i = ts.get_initial_nodes()

    def visit(node: Node, phi: LogicalProposition):
        stack_U.append(node)
        set_R.append(node)

        #begin do while loop
        print_trace(stack_U)
        explore(phi)

        while len(stack_U)>0 and flag_bool :
            print_trace(stack_U)
            explore(phi)
        #end do while loop
        print_trace(stack_U)

        return flag_bool

    def explore(phi: LogicalProposition):
        nonlocal flag_bool #idk why i need to use that, but not using it causes "UnboudnLocalError: local variable 'flag_bool' reference before assignement"
        s_1 = stack_U[len(stack_U)-1]
        succesors = s_1.get_next_nodes()
        if(is_included_in(succesors, set_R)):
            stack_U.pop()
            flag_bool = flag_bool and phi.evaluate(s_1.get_labels())
            
        else:
            s_2 = content_of_without(succesors, set_R)[0]
            stack_U.append(s_2)
            set_R.append(s_2)

            #this update of flag_bool is not present in the original algorithm; 
            #it was added in order for the stack to contain all the states of a trace leading
            #to an invalid state, ***includind the invalid state***, which would be absent without the line below
            flag_bool = flag_bool and phi.evaluate(s_2.get_labels())
        

    i_without_r = content_of_without(i, set_R)

    while(i_without_r != [] and flag_bool):
        s = i_without_r[0]
        
        flag_bool = visit(s, phi)

        i_without_r = content_of_without(i, set_R)

    return flag_bool, stack_U 
    
#EXAMPLES 
node1 = Node(["nc1", "nc2", "y=1"])
node2 = Node(["p1", "nc2", "y=1"])
node3 = Node(["c1", "nc2", "y=0"])
node4 = Node(["nc1", "p2", "y=1"])
node5 = Node(["nc1", "c2", "y=0"])
node6 = Node(["p1", "p2", "y=1"])
node7 = Node(["c1", "p2", "y=0"])
node8 = Node(["p1", "c2", "y=0"])

node1.set_next_nodes([node2, node4])
node2.set_next_nodes([node3, node6])
node3.set_next_nodes([node1, node7])
node4.set_next_nodes([node5, node6])
node5.set_next_nodes([node1, node8])
node6.set_next_nodes([node7, node8])
node7.set_next_nodes([node4])
node8.set_next_nodes([node2])

ts1 = TransitionSystem([node1])
phi1 = NotOperator(AndOperator(IdentityOperator("c1"), IdentityOperator("c2")))

worked, example = verify(ts1, phi1)

print("Invariant is respected" if worked else "Invariant is not respected, below shows a trace leading to invalid state")
print_trace(example)