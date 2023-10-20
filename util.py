from TransitionSystem import Node


def content_of_without(array1: [], array2: []):
    res = [i for i in array1 if i not in array2]
    return res

def is_included_in(array1, array2):
    return len(content_of_without(array1, array2)) == 0

def print_trace(trace: list[Node]):
    print("----------BEGIN TRACE----------")
    for n in trace:
        print(" | ")
        print(" | ")
        print(" V ")
        print(n.get_labels())
    print("-----------END TRACE-----------")    

    