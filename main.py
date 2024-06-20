from antlr4 import *
from JayPyGrammarLexer import JayPyGrammarLexer
from JayPyGrammarParser import JayPyGrammarParser
from JayPyGrammarListener import JayPyGrammarListener
from JayPyGrammarVisitor import JayPyGrammarVisitor
from extract_functions import extract_functions

def main():

    input_string = """


        int factorial(int n) {
            int a=3;
            if (n <= 1) 
            {
            return 1;  
            } else 
            {
            return n * factorial(n - 1); 
        }
    }


    

    int main() {
    
    println(factorial(5));
   
        return 0;}
        """
        
    functions=extract_functions(input_string)
    input_stream = InputStream(input_string)

    lexer = JayPyGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)


    parser = JayPyGrammarParser(token_stream)
    tree = parser.program()

    listener = JayPyGrammarListener()

    walker = ParseTreeWalker()
    walker.walk(listener, tree)


   # print(tree.toStringTree(recog=parser))
    
    


    visitor = JayPyGrammarVisitor(listener.function_dictionary,listener.function_return_type_dictionary,listener.function_arguments_dictionary,listener.function_ctx_dictionary,functions)
    visitor.visit(tree)



if __name__ == '__main__':
    main()
