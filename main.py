from TransitionSystem import TransitionSystem
from LogicalProposition import AndOperator
from LogicalProposition import OrOperator
from LogicalProposition import NotOperator
from LogicalProposition import IdentityOperator
from LogicalProposition import LogicalProposition
from TransitionSystem import Node
from util import print_trace
from verify import verify

#EXAMPLES 

#1 - Concurrent processes, critical section, mutex 
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
phi1 = NotOperator(
    AndOperator(
        IdentityOperator("c1"), 
        IdentityOperator("c2")
    )
)


#2 Random Transition System and Invariant
node9 = Node(["d", "b", "w"])
node10 = Node(["d", "e", "w"])
node11 = Node(["q", "j", "i"])
node12 = Node(["j", "k", "d"])
node13 = Node(["w", "a", "d"])
node14 = Node(["p", "q", "r"])
node15 = Node(["j", "t", "u"])
node16 = Node(["v", "w", "d"])

node9.set_next_nodes([node9, node14])
node10.set_next_nodes([node16, node12])
node11.set_next_nodes([node13, node9])
node12.set_next_nodes([node14, node6])
node13.set_next_nodes([node12, node10])
node14.set_next_nodes([node16, node14])
node15.set_next_nodes([node11])
node16.set_next_nodes([node15, node10])

ts2 = TransitionSystem([node9, node16])
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