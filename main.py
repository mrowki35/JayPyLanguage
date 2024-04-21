from antlr4 import *
from JayPyGrammarLexer import JayPyGrammarLexer
from JayPyGrammarParser import JayPyGrammarParser
from JayPyGrammarListener import JayPyGrammarListener
from VariablesList import VariablesList

def main():

    input_string = """String main() {
    ///jestem tutaj
    i=0; 
    boolean z=true;
    String imie="Przemek";
    String name=null;
    String imie2="Arek";
    imie2=imie;
    float z=10.0;
    boolean alpha=False;
    return "0";}"""

    

    input_string = """ 
        int main() {
    ///jestem tutaj
    //int i;
    boolean y=False;
    y=True;
    float z=10.0;
    z+7.0;
    String imie="Przemek";
    //String name=null;
    String imie2="Arek";
    //imie2=imie;
    //duuble t=90;
   // float z=10.0;
    //boolean alpha=False;
    return "0";}"""



    input_stream = InputStream(input_string)

    lexer = JayPyGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    parser = JayPyGrammarParser(token_stream)
    tree = parser.program()
    listener = JayPyGrammarListener()

    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    for i in listener.my_variable_list.variablesList:
        print(i)

if __name__ == '__main__':
    main()
