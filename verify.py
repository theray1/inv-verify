from TransitionSystem import TransitionSystem
from LogicalProposition import LogicalProposition
from TransitionSystem import Node
from util import is_included_in
from util import content_of_without

def verify(ts: TransitionSystem, phi: LogicalProposition) -> tuple[bool, list[Node]]:
    stack_U: list[Node] = []
    set_R: list[Node] = []
    flag_bool = True
    i = ts.get_initial_nodes()

    def visit(node: Node, phi: LogicalProposition):
        stack_U.append(node)
        set_R.append(node)

        #equivalent of the "Répéter - Jusqu'à" loop

        #print_trace(stack_U)

        explore(phi)

        while len(stack_U)>0 and flag_bool :
            #print_trace(stack_U)
            explore(phi)

        #end of the "Répéter - Jusqu'à" loop equivalent


        #print_trace(stack_U)

        return flag_bool


    #corresponds to the content of loop "Répéter"
    def explore(phi: LogicalProposition):
        nonlocal flag_bool #not sure why this is needed, but not using it causes "UnboudnLocalError: local variable 'flag_bool' reference before assignement"
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
        

    #start of the while loop of the main algorithm

    i_without_r = content_of_without(i, set_R)

    while(i_without_r != [] and flag_bool):
        s = i_without_r[0]
        
        flag_bool = visit(s, phi)

        i_without_r = content_of_without(i, set_R)
    
    #end of the while loop of the main algorithm

    return flag_bool, stack_U 





