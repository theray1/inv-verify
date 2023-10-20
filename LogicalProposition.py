#A logical proposition is any combination of And, Or (Binary), Not or Identity (Unary) operators
class LogicalProposition:

    #A logical proposition can be evaluated thanks to a variable mapping.
    #Here, label_list fullfils that role in the following way: 
    #Every string in label_list is to be interpreted as having its value set to True
    #For example : evaluating a logical proposition phi ((not a and b) or (c and d)) with label_list ["a", "b", "d"]
    #is equivalent to computing ((not True and True) or (False and true))
    #That is because a, b and d are all contained in label_list, and thus are treated as False
    #and c is not in label_list, and as such is implicitely treated as False
    def evaluate(self, label_list: list[str]):
        pass
        
    def __init__(self):
        pass

#Logical And
class AndOperator(LogicalProposition):

    term1: LogicalProposition
    term2: LogicalProposition

    def __init__(self, term1, term2):
        self.term1 = term1
        self.term2 = term2

    def evaluate(self, label_list: list[str]):
        return self.term1.evaluate(label_list) and self.term2.evaluate(label_list)

#Logical Or
class OrOperator(LogicalProposition):

    term1: LogicalProposition
    term2: LogicalProposition

    def __init__(self, term1, term2):
        self.term1 = term1
        self.term2 = term2

    def evaluate(self, label_list: list[str]):
        return self.term1.evaluate(label_list) or self.term2.evaluate(label_list)

#Logical Not
class NotOperator(LogicalProposition):

    term1: LogicalProposition

    def __init__(self, term1):
        self.term1 = term1

    def evaluate(self, label_list: list[str]):
        return not self.term1.evaluate(label_list)

#Boolean Variable
class IdentityOperator(LogicalProposition):

    term1: str

    def __init__(self, term1):
        self.term1 = term1

    #The evaluation of a simple boolean variable consists in checking the label_list parameter for an element equal to the variable's term
    #If such an element exists, then the boolean variable is True, False otherwise
    #This check is similar to a traditional variable mapping
    def evaluate(self, label_list: list[str]):
        for l in label_list:
            if(l == self.term1):
                return True 
            
        return False