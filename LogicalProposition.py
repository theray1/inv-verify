class LogicalProposition:
    def evaluate(self, label_list: list[str]):
        pass
        
    def __init__(self):
        pass

class AndOperator(LogicalProposition):

    term1: LogicalProposition
    term2: LogicalProposition

    def __init__(self, term1, term2):
        self.term1 = term1
        self.term2 = term2

    def evaluate(self, label_list: list[str]):
        return self.term1.evaluate(label_list) and self.term2.evaluate(label_list)
    
class OrOperator(LogicalProposition):

    term1: LogicalProposition
    term2: LogicalProposition

    def __init__(self, term1, term2):
        self.term1 = term1
        self.term2 = term2

    def evaluate(self, label_list: list[str]):
        return self.term1.evaluate(label_list) or self.term2.evaluate(label_list)

class NotOperator(LogicalProposition):

    term1: LogicalProposition

    def __init__(self, term1):
        self.term1 = term1

    def evaluate(self, label_list: list[str]):
        return not self.term1.evaluate(label_list)

class IdentityOperator(LogicalProposition):

    term1: str

    def __init__(self, term1):
        self.term1 = term1

    def evaluate(self, label_list: list[str]):
        for l in label_list:
            if(l == self.term1):
                return True 
            
        return False