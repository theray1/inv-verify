from TransitionSystem import State

#content_of_without is used to compute content of an array from which we remove the content of another array
#It it used to compute the set difference of two sets represented by arrays
def content_of_without(array1: [], array2: []):
    res = [i for i in array1 if i not in array2]
    return res

#is_included_in is used to check if all elements of an array are present in another array
#It is used to check if a set is a subset of another set, with both of them represented by arrays
def is_included_in(array1: [], array2: []):
    return len(content_of_without(array1, array2)) == 0

def print_trace(trace: list[State]):
    print("----------BEGIN TRACE----------")
    for n in trace:
        print(" | ")
        print(" | ")
        print(" V ")
        print(n.get_labels())
    print("-----------END TRACE-----------")    

    
