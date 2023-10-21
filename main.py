from TransitionSystem import TransitionSystem
from LogicalProposition import AndOperator
from LogicalProposition import OrOperator
from LogicalProposition import NotOperator
from LogicalProposition import IdentityOperator
from LogicalProposition import LogicalProposition
from TransitionSystem import State
from util import print_trace
from verify import verify

#EXAMPLES 

#1 - Concurrent processes, critical section, mutex 
state1 = State(["nc1", "nc2", "y=1"])
state2 = State(["p1", "nc2", "y=1"])
state3 = State(["c1", "nc2", "y=0"])
state4 = State(["nc1", "p2", "y=1"])
state5 = State(["nc1", "c2", "y=0"])
state6 = State(["p1", "p2", "y=1"])
state7 = State(["c1", "p2", "y=0"])
state8 = State(["p1", "c2", "y=0"])

state1.set_next_states([state2, state4])
state2.set_next_states([state3, state6])
state3.set_next_states([state1, state7])
state4.set_next_states([state5, state6])
state5.set_next_states([state1, state8])
state6.set_next_states([state7, state8])
state7.set_next_states([state4])
state8.set_next_states([state2])

ts1 = TransitionSystem([state1])
phi1 = NotOperator(
    AndOperator(
        IdentityOperator("c1"), 
        IdentityOperator("c2")
    )
)


#2 Random Transition System and Invariant
state9 = State(["d", "b", "w"])
state10 = State(["d", "e", "w"])
state11 = State(["q", "j", "i"])
state12 = State(["j", "k", "d"])
state13 = State(["w", "a", "d"])
state14 = State(["p", "q", "r"])
state15 = State(["j", "t", "u"])
state16 = State(["v", "w", "d"])

state9.set_next_states([state9, state14])
state10.set_next_states([state16, state12])
state11.set_next_states([state13, state9])
state12.set_next_states([state14, state6])
state13.set_next_states([state12, state10])
state14.set_next_states([state16, state14])
state15.set_next_states([state11])
state16.set_next_states([state15, state10])

ts2 = TransitionSystem([state9, state16])
phi2 = OrOperator(
    AndOperator(
        NotOperator(
            IdentityOperator("w")),
            IdentityOperator("j")), 
    AndOperator(
        OrOperator(
            IdentityOperator("a"), 
            IdentityOperator("d")
        ),
        NotOperator(
            IdentityOperator("a")
        )
    )
)

res = True
example = []
#Uncomment whichever example you want to try the algorithm on!
#res, example = verify(ts1, phi1)
#res, example = verify(ts2, phi2)


if(res):
    print("Invariant is respected (, or you didn't uncomment any of the two examples!)")
else:
    print("Invariant is not respected, below shows a trace leading to invalid state")
    print_trace(example)