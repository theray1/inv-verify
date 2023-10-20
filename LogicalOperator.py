class LogicalOperator:
    def evaluate(self):
        pas
        
    def __init__(self):
        pass

    class AndOperator(LogicalOperator):

        term1: LogicalOperator
        term2: LogicalOperator

        def evaluate(self):
            return self.term1.evaluate() and self.term2.evaluate()
    
    class OrOperator(LogicalOperator):

        term1: LogicalOperator
        term2: LogicalOperator

        def evaluate(self):
            return self.term1.evaluate() or self.term2.evaluate()

    class NotOperator(LogicalOperator):

        term1: LogicalOperator

        def evaluate(self):
            return not self.term1.evaluate()

    class IdentityOperator(LogicalOperator):

        term1: LogicalOperator

        def evaluate(self):
            return self.term1