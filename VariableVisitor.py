import ast

def extract_variables(expr):

    tree = ast.parse(expr, mode='eval')
    
    variables = set()


    class VariableVisitor(ast.NodeVisitor):
        def visit_Name(self, node):
            variables.add(node.id)
            self.generic_visit(node)
    
    visitor = VariableVisitor()
    visitor.visit(tree)
    
    return variables

