# Generated from C:/Javalib/test/JayPyGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
import ast
import re
import sys
import numpy as np
from Scopes import Scope
from CallStack import CallStack
from ScopeHandler import ScopeHandler
from ScopeHandler import execute_translated_function
from ScopeHandler import translate_java_to_python
if "." in __name__:
    from .JayPyGrammarParser import JayPyGrammarParser
else:
    from JayPyGrammarParser import JayPyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by JayPyGrammarParser.

class JayPyGrammarVisitor(ParseTreeVisitor):

    def __init__(self,function_dictionary,function_return_type_dictionary,function_arguments_dictionary, function_ctx_dictionary,functions):
        self.function_dictionary=function_dictionary
        self.function_return_type_dictionary=function_return_type_dictionary
        self.function_arguments_dictionary=function_arguments_dictionary
        self.function_ctx_dictionary=function_ctx_dictionary
        self.scopes=Scope()
        self.call_stack = CallStack()
        self.functions=functions
        

    # Visit a parse tree produced by JayPyGrammarParser#program.
    def visitProgram(self, ctx:JayPyGrammarParser.ProgramContext):
        #THE LAST SCOPE is the one
        self.scopes.enterLocalScope()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:JayPyGrammarParser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:JayPyGrammarParser.MethodDeclarationContext):
        return # self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#methodBody.
    def visitMethodBody(self, ctx:JayPyGrammarParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#typeTypeOrVoid.
    def visitTypeTypeOrVoid(self, ctx:JayPyGrammarParser.TypeTypeOrVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#typeTypeOrVar.
    def visitTypeTypeOrVar(self, ctx:JayPyGrammarParser.TypeTypeOrVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:JayPyGrammarParser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#variableDeclarators.
    def visitVariableDeclarators(self, ctx:JayPyGrammarParser.VariableDeclaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:JayPyGrammarParser.VariableDeclaratorContext):
        if "[" in ctx.parentCtx.parentCtx.getText() and "]" in ctx.parentCtx.parentCtx.getText():
            var=ctx.variableDeclaratorId().identifier().getText()
            #print(ctx.variableInitializer().arrayInitializer().getText().replace("{","").replace("}",""))
           # lista=[]
           # for i in ctx.variableInitializer().arrayInitializer().getText().replace("{","").replace("}","").split(','):
              #  lista.append(float(i))
            try:
                matrix = self.create_matrix_from_text(ctx.variableInitializer().arrayInitializer().getText())
                self.scopes.addToLocalScope(var,matrix,type(matrix).__name__)
                return
            except:
                try:
                    matrix = self.visit(ctx.variableInitializer().expression())
                    self.scopes.addToLocalScope(var,matrix,type(matrix).__name__)
                    return
                except AttributeError as e:
                    print("Error: " + str(e)+ " at line "+ str(ctx.start.line))
                    sys.exit(1)
                except:
                    print("Unexpected Error: " + " at line "+ str(ctx.start.line))
                    sys.exit(1)
                #print(self.scopes.mergeAllScopes()[var])
                
                #matrix=self.visit()

        if ctx.variableInitializer().expression().methodCall():
            if ctx.variableInitializer().expression().methodCall().identifier().getText() in self.function_dictionary:
                function_returned_type=self.function_return_type_dictionary[ctx.variableInitializer().expression().methodCall().identifier().getText()].getText()
                if function_returned_type==ctx.parentCtx.parentCtx.typeType().getText():
                    type_=ctx.parentCtx.parentCtx.typeType().getText()
                    var=ctx.variableDeclaratorId().identifier().getText()
                    result=self.visit(ctx.variableInitializer().expression())
                    self.scopes.addToLocalScope(var,result,type_)

                elif function_returned_type in ["float","double"] and ctx.parentCtx.parentCtx.typeType().getText()=="int":
                    type_=ctx.parentCtx.parentCtx.typeType().getText()
                    var=ctx.variableDeclaratorId().identifier().getText()
                    result=self.visit(ctx.variableInitializer().expression())
                    self.scopes.addToLocalScope(var,result,type_)
                elif ctx.parentCtx.parentCtx.typeType().getText() in ["float", "double"] and function_returned_type=="int":
                    type_=ctx.parentCtx.parentCtx.typeType().getText()
                    var=ctx.variableDeclaratorId().identifier().getText()
                    result=self.visit(ctx.variableInitializer().expression())
                    self.scopes.addToLocalScope(var,result,type_)
                else:
                    print("ERROR: Wrong type of returned value by the function: "+ '"'+ 
                    self.function_return_type_dictionary[ctx.variableInitializer().expression().methodCall().identifier().getText()].getText() + 
                    '"'+" should be " +'"'+ctx.parentCtx.parentCtx.typeType().getText() +'"' + " "+ str(ctx.start.line))
                    sys.exit(1)
            else:
                print("ERROR: Function " + '"'+ ctx.variableInitializer().expression().methodCall().identifier().getText()
                +'"'+ " not declared at line "+ str(ctx.start.line))
                sys.exit(1)
            return 




        convert_to_int=False
        convert_to_float=False
        if type(eval(self.pre_processString(ctx.variableInitializer().expression().getText()),{},self.scopes.mergeAllScopes())).__name__=="str":
            value_type="String"
        else:
            value_type=type(eval(self.pre_processString(ctx.variableInitializer().expression().getText()),{},self.scopes.mergeAllScopes())).__name__
        if ctx.parentCtx.parentCtx.typeType().getText()=="int" and value_type=="float":
            convert_to_int=True
        elif ctx.parentCtx.parentCtx.typeType().getText() in ["double","float"] and value_type=="int":
            convert_to_float=True

        if ctx.variableDeclaratorId().identifier().getText() in self.scopes.getCurrentScope(): 
            print("ERROR redeclaration: Variable with name " + ctx.variableDeclaratorId().identifier().getText() 
            + " already exists in the current scope at line:"
            + str(ctx.start.line))
            sys.exit(1)
        elif ctx.variableInitializer():
            try:
                if convert_to_int:
                    self.scopes.addToLocalScope(ctx.variableDeclaratorId().identifier().getText(),
                    int(eval(self.pre_processString(ctx.variableInitializer().expression().getText()),{},self.scopes.mergeAllScopes())),
                    ctx.parentCtx.parentCtx.typeType().getText())
                elif convert_to_float:
                    self.scopes.addToLocalScope(ctx.variableDeclaratorId().identifier().getText(),
                    float(eval(self.pre_processString(ctx.variableInitializer().expression().getText()),{},self.scopes.mergeAllScopes())),
                    ctx.parentCtx.parentCtx.typeType().getText())
                else:
                    self.scopes.addToLocalScope(ctx.variableDeclaratorId().identifier().getText(),
                    eval(self.pre_processString(ctx.variableInitializer().expression().getText()),{},self.scopes.mergeAllScopes()),
                    ctx.parentCtx.parentCtx.typeType().getText())
            except NameError as e:
                message = str(e)
                start_index = message.find("'") + 1
                end_index = message.find("'", start_index)
                undefined_variable = message[start_index:end_index]
                print("ERROR Variable not defined: Variable " + undefined_variable
                + " is not defined at line: "
                + str(ctx.start.line))
                sys.exit(1)
            except TypeError as e:
                print("ERROR Type missmatch: "
                + " at line: "
                + str(ctx.start.line))
                sys.exit(1)

        else:
            self.scopes.addToLocalScope(ctx.variableDeclaratorId().identifier().getText(),None,ctx.parentCtx.parentCtx.typeType().getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#variableDeclaratorId.
    def visitVariableDeclaratorId(self, ctx:JayPyGrammarParser.VariableDeclaratorIdContext):
      #  print("ID")
     #   print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#variableInitializer.
    def visitVariableInitializer(self, ctx:JayPyGrammarParser.VariableInitializerContext):
      #  self.scopes.addToCurrentScope(ctx.parentCtx.variableDeclaratorId().identifier().getText(),eval(ctx.expression().getText()))
    #    print("BENC")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#arrayInitializer.
    def visitArrayInitializer(self, ctx:JayPyGrammarParser.ArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#qualifiedNameList.
    def visitQualifiedNameList(self, ctx:JayPyGrammarParser.QualifiedNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#formalParameters.
    def visitFormalParameters(self, ctx:JayPyGrammarParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#receiverParameter.
    def visitReceiverParameter(self, ctx:JayPyGrammarParser.ReceiverParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#formalParameterList.
    def visitFormalParameterList(self, ctx:JayPyGrammarParser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#formalParameter.
    def visitFormalParameter(self, ctx:JayPyGrammarParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#lastFormalParameter.
    def visitLastFormalParameter(self, ctx:JayPyGrammarParser.LastFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#qualifiedName.
    def visitQualifiedName(self, ctx:JayPyGrammarParser.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#literal.
    def visitLiteral(self, ctx:JayPyGrammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#floatLiteral.
    def visitFloatLiteral(self, ctx:JayPyGrammarParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#elementValuePairs.
    def visitElementValuePairs(self, ctx:JayPyGrammarParser.ElementValuePairsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#elementValuePair.
    def visitElementValuePair(self, ctx:JayPyGrammarParser.ElementValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#elementValue.
    def visitElementValue(self, ctx:JayPyGrammarParser.ElementValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#elementValueArrayInitializer.
    def visitElementValueArrayInitializer(self, ctx:JayPyGrammarParser.ElementValueArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#block.
    def visitBlock(self, ctx:JayPyGrammarParser.BlockContext):
        self.scopes.enterLocalScope()
        self.visitChildren(ctx)
        self.scopes.exitLocalScope()
       # return result

    # Visit a parse tree produced by JayPyGrammarParser#blockStatement.
    def visitBlockStatement(self, ctx:JayPyGrammarParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx:JayPyGrammarParser.LocalVariableDeclarationContext):
        convert_to_int=False
        convert_to_float=False
        if type(eval(self.pre_processString(ctx.expression().getText()),{},self.scopes.mergeAllScopes())).__name__=="str":
            value_type="String"
        else:
            value_type=type(eval(self.pre_processString(ctx.expression().getText()),{},self.scopes.mergeAllScopes())).__name__
        if ctx.typeTypeOrVar().typeType().getText()=="int" and value_type=="float":
            convert_to_int=True
        elif ctx.typeTypeOrVar().typeType().getText() in ["double","float"] and value_type=="int":
            convert_to_float=True

        if ctx.identifier().getText() in self.scopes.getCurrentScope(): 
            print("ERROR redeclaration: Variable with name " + ctx.identifier().getText() 
            + " already exists in the current scope at line: "
            + str(ctx.start.line))
            sys.exit(1)
        elif ctx.expression():
            try:
                if convert_to_float:
                    self.scopes.addToLocalScope(ctx.identifier().getText(),
                    float(eval(self.pre_processString(ctx.expression().getText()),{},self.scopes.mergeAllScopes()),ctx.typeTypeOrVar().getText()))
                elif convert_to_int:
                    self.scopes.addToLocalScope(ctx.identifier().getText(),
                    int(eval(self.pre_processString(ctx.expression().getText()),{},self.scopes.mergeAllScopes()),ctx.typeTypeOrVar().getText()))
                else:
                    self.scopes.addToLocalScope(ctx.identifier().getText(),
                    eval(self.pre_processString(ctx.expression().getText()),{},self.scopes.mergeAllScopes()),ctx.typeTypeOrVar().getText())
            except NameError as e:
                message = str(e)
                start_index = message.find("'") + 1
                end_index = message.find("'", start_index)
                undefined_variable = message[start_index:end_index]
                print("ERROR Variable not defined: Variable " + undefined_variable
                + " is not defined at line: "
                + str(ctx.start.line))
                sys.exit(1)
            except TypeError as e:
                print("ERROR Type missmatch: "
                + " at line: "
                + str(ctx.start.line))
                sys.exit(1)
        else:
            self.scopes.addToLocalScope(ctx.identifier().getText(),None,ctx.typeTypeOrVar().getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#identifier.
    def visitIdentifier(self, ctx:JayPyGrammarParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#typeIdentifier.
    def visitTypeIdentifier(self, ctx:JayPyGrammarParser.TypeIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#printStatement.
    def visitPrintStatement(self, ctx:JayPyGrammarParser.PrintStatementContext):
        try:
            print(self.visit(ctx.expression()),end="")
        except TypeError as e:
            print(e)
            sys.exit(1)
        
        
        #return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#printlnStatement.
    def visitPrintlnStatement(self, ctx:JayPyGrammarParser.PrintlnStatementContext):
        try:
            print(self.visit(ctx.expression()))
        except TypeError as e:
            print(e)
            sys.exit(1)


    # Visit a parse tree produced by JayPyGrammarParser#statement.
    def visitStatement(self, ctx:JayPyGrammarParser.StatementContext):
       # print(ctx.parentCtx.getText())
        if ctx.IF():
            if self.visitExpression(ctx.parExpression().expression()):
               self.visit(ctx.statement(0))
            elif ctx.ELSE():
                self.visit(ctx.statement(1))
        elif ctx.FOR() and ctx.IN():
            var =ctx.identifier().getText()
            type_=ctx.typeTypeOrVar().getText()
            lista=ctx.expression().getText()

            if type_!="float":
               # print(type(self.scopes.mergeAllScopes()[lista][0][0]).__name__)
                print("Error wrong type variable to list: at line "+ str(ctx.start.line))
                sys.exit(1)
                #print(self.scopes.mergeAllScopes()[lista])
            for i in self.scopes.mergeAllScopes()[lista][0]:
                self.scopes.addToLocalScope(var,i,type_)
                self.visit(ctx.statement(0))
            #print(ctx.getText())
            pass
        elif ctx.FOR():
            self.scopes.enterLocalScope()
            self.visit(ctx.forControl().forInit())
           # print(ctx.forControl().expression().getText())
            while self.visit(ctx.forControl().expression()):
                self.visit(ctx.statement(0))
                self.visit(ctx.forControl().forUpdate)
            self.scopes.exitLocalScope()
        elif ctx.WHILE():
            while self.visit(ctx.parExpression().expression()):
                self.visit(ctx.statement(0))
        elif ctx.RETURN():
            return self.visit(ctx.expression())
        elif ctx.BREAK():
            return
        elif ctx.CONTINUE():
            return
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#switchBlockStatementGroup.
    def visitSwitchBlockStatementGroup(self, ctx:JayPyGrammarParser.SwitchBlockStatementGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#switchLabel.
    def visitSwitchLabel(self, ctx:JayPyGrammarParser.SwitchLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#forControl.
    def visitForControl(self, ctx:JayPyGrammarParser.ForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#forInit.
    def visitForInit(self, ctx:JayPyGrammarParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#enhancedForControl.
    def visitEnhancedForControl(self, ctx:JayPyGrammarParser.EnhancedForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#parExpression.
    def visitParExpression(self, ctx:JayPyGrammarParser.ParExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#expressionList.
    def visitExpressionList(self, ctx:JayPyGrammarParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#methodCall.
    def visitMethodCall(self, ctx):
        method_name = ctx.methodCall().identifier().getText()

       # print(self.function_return_type_dictionary[method_name].getText()+" "+ method_name+ " "+ self.function_arguments_dictionary[method_name].getText()+ " "+ self.function_dictionary[method_name].getText())
        if method_name not in self.function_arguments_dictionary:
            print("Error method not declared: "+ method_name+ctx.start.line)
            sys.exit(1)

        if self.function_return_type_dictionary[method_name].getText()=="void":
            arguments = [self.visit(arg) for arg in ctx.methodCall().arguments().expressionList().expression()]
           # print(len(arguments))
            #print(len(self.function_arguments_dictionary[method_name].getText().split(",")))
            if len(arguments)!=self.function_arguments_dictionary[method_name].getText().split(",") and len(arguments)!=1 and len(self.function_arguments_dictionary[method_name].getText().split(","))!=1:
                #print(len(arguments)!=self.function_arguments_dictionary[method_name].getText().split(",")
                print(f"Error: wrong number of parameters: {method_name} at line {ctx.start.line}")
                sys.exit(1)

            for i in range(len(arguments)):
                var = self.function_arguments_dictionary[method_name].formalParameterList().formalParameter(i).variableDeclaratorId().identifier().getText()
                type_ = self.function_arguments_dictionary[method_name].formalParameterList().formalParameter(i).typeType().getText()
                self.scopes.addToLocalScope(var, arguments[i], type_)
            self.visit(self.function_dictionary[method_name])

            return

        if self.function_arguments_dictionary[method_name].getText() == "()":
            if not ctx.methodCall().arguments().expressionList():
                scope_handler = ScopeHandler()
                body=self.functions[method_name]
               # print(body)
                translated=translate_java_to_python(body)
                function_name=method_name
                fibonacci_func = execute_translated_function(translated, function_name, scope_handler)
                result = fibonacci_func()
                return result
                #scope_handler.addToLocalScope('n', 10, 'int')


            else:
                print(f"Error: arguments were given to a method {method_name} which doesn't have one at line {ctx.start.line}")
                sys.exit(1)

        elif len(self.function_arguments_dictionary[method_name].getText().split(",")) != len(ctx.methodCall().arguments().expressionList().getText().split(",")):
            print(f"Error: wrong number of parameters: {method_name} at line {ctx.start.line}")
            sys.exit(1)

        else:
            arguments = [self.visit(arg) for arg in ctx.methodCall().arguments().expressionList().expression()]
            if self.process_function_arguments(self.function_arguments_dictionary[method_name], ctx.methodCall().arguments().expressionList())==True:
                return self.execute_function(method_name,arguments)
            else:
                answer = self.process_function_arguments(self.function_arguments_dictionary[method_name],ctx.methodCall().arguments().expressionList())
                print(f"Error: wrong arguments types: {answer[1]} should be {answer[2]} at line {ctx.start.line}")
                sys.exit(1)
        #return self.execute_function(method_name, arguments)

    def execute_function(self, method_name, arguments):
        scope_handler = ScopeHandler()
        body=self.functions[method_name]
        values=[]
        
        for i in range(len(arguments)):
            var = self.function_arguments_dictionary[method_name].formalParameterList().formalParameter(i).variableDeclaratorId().identifier().getText()
            type_ = self.function_arguments_dictionary[method_name].formalParameterList().formalParameter(i).typeType().getText()
            self.scopes.addToLocalScope(var, arguments[i], type_)
            scope_handler.addToLocalScope(var, arguments[i], type_)
            values.append(arguments[i])
        #print(body)
        translated=translate_java_to_python(body)
        function_name=method_name
        try:
            fibonacci_func = execute_translated_function(translated, function_name, scope_handler)
            result = fibonacci_func(*values)
        except:
            result=self.visit(self.function_dictionary[function_name])

        return result


    # Visit a parse tree produced by JayPyGrammarParser#expression.
    def visitExpression(self, ctx:JayPyGrammarParser.ExpressionContext):
        try:
            variables= self.extract_variables(self.pre_processString(ctx.getText().replace("DOT","+")))
        except:
            print("Error occured while parsing an expression: at line "+ str(ctx.start.line))
            sys.exit(1)
        found_keys = [var for var in variables if var in self.scopes.mergeAllTypesScopes()]

        if any(self.scopes.mergeAllTypesScopes()[var] == 'ndarray' for var in found_keys):
            if not found_keys:
                print("Error: variable not declared at line "+str(ctx.start.line))
                sys.exit(1)
            all_lists = all(self.scopes.mergeAllTypesScopes()[var] == 'ndarray' for var in found_keys)
            if all_lists and "DOT" in ctx.getText():
                h=ctx.expression(0).primary().identifier().getText()
                g=ctx.expression(1).primary().identifier().getText()
                try:
                    return np.dot(self.scopes.mergeAllScopes()[h],self.scopes.mergeAllScopes()[g])
                except ValueError as e:
                    print("Error" + str(e)+ " "+ "at line "+ str(ctx.start.line))
                    sys.exit(1)
            elif all_lists:
                return self.evaluate_expression(ctx.getText(),self.scopes.mergeAllScopes(),ctx)
            else:
                print("Error: wrong calculations: different variables types "+ str(ctx.start.line))
                sys.exit(1)

        if ctx.ASSIGN() and ctx.expression(1).methodCall():
            result=self.visit(ctx.expression(1))
            var=ctx.expression(0).primary().identifier().getText()
            for scope in self.scopes.scopes:
                if var in scope:
                    scope[var]=result

        elif ctx.ASSIGN() and "[" in ctx.getText() and "]" in ctx.getText():
            var=ctx.expression(0).primary().identifier().getText()
            print(var)
            type_=ctx.parentCtx.typeType().getText()
            print(type_)
           # print("MOre or less")
            pass
        elif ctx.ASSIGN():
            #print(eval(ctx.expression().ge))
           # print(ctx.expression(0).primary().identifier().getText())
            value=eval(ctx.expression(1).getText(),{},self.scopes.mergeAllScopes())
            value_type = type(value).__name__
            if value_type=="str":
                value_type="String"
            if ctx.expression(0).primary().identifier().getText() not in self.scopes.mergeAllTypesScopes():
                print("ERROR: Variable " + "'"+ ctx.expression(0).primary().identifier().getText() +"'"
                 + " not declared in this scope at line: " +str(ctx.start.line))
                sys.exit(1)
            elif self.scopes.mergeAllTypesScopes().get(ctx.expression(0).primary().identifier().getText())==value_type:
                for scope in self.scopes.scopes:
                    if ctx.expression(0).primary().identifier().getText() in scope:
                        scope[ctx.expression(0).primary().identifier().getText()]=value
            else:
                print("ERROR: Wrong type, variable " + "'"+ ctx.expression(0).primary().identifier().getText() +"'" " declared as " 
                +self.scopes.mergeAllTypesScopes().get(ctx.expression(0).primary().identifier().getText()) + " where assigned value is type " 
                + value_type + " at line " +str(ctx.start.line))
        elif ctx.methodCall():
            try:
                return self.visitMethodCall(ctx)
            except RecursionError:
                print("Error: maximum RecursionError: at line "+ str(ctx.start.line))
                sys.exit(1)

        elif "+=" in ctx.getText():
            for scope in self.scopes.scopes:
                if ctx.expression(0).getText() in scope:
                    scope[ctx.expression(0).getText()]=scope[ctx.expression(0).getText()]+self.visit(ctx.expression(1))
        elif "-=" in ctx.getText():
            for scope in self.scopes.scopes:
                if ctx.expression(0).getText() in scope:
                    scope[ctx.expression(0).getText()]=scope[ctx.expression(0).getText()]-self.visit(ctx.expression(1))
        elif "*=" in ctx.getText():
            for scope in self.scopes.scopes:
                if ctx.expression(0).getText() in scope:
                    scope[ctx.expression(0).getText()]=scope[ctx.expression(0).getText()]*self.visit(ctx.expression(1))
        elif "/=" in ctx.getText():
            for scope in self.scopes.scopes:
                if ctx.expression(0).getText() in scope:
                    scope[ctx.expression(0).getText()]=scope[ctx.expression(0).getText()]/self.visit(ctx.expression(1))
        elif "++" in ctx.getText():
            for scope in self.scopes.scopes:
                if ctx.expression(0).getText() in scope:
                    scope[ctx.expression(0).getText()]=scope[ctx.expression(0).getText()]+1
        elif "--" in ctx.getText():
            for scope in self.scopes.scopes:
                if ctx.expression(0).getText() in scope:
                    scope[ctx.expression(0).getText()]=scope[ctx.expression(0).getText()]-1
        else:
            try:
               # print(eval(self.pre_processString(ctx.getText()),{},self.scopes.mergeAllScopes()))
                return eval(self.pre_processString(ctx.getText()),{},self.scopes.mergeAllScopes())
            except NameError:
                print("ERROR: Variable " + "'"+ ctx.getText() +"'"
                 + " not declared in this scope at line: " +str(ctx.start.line))
                sys.exit(1)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#lambdaParameters.
    def visitLambdaParameters(self, ctx:JayPyGrammarParser.LambdaParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#lambdaExpression.
    def visitLambdaExpression(self, ctx:JayPyGrammarParser.LambdaExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#lambdaBody.
    def visitLambdaBody(self, ctx:JayPyGrammarParser.LambdaBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#lambdaLVTIList.
    def visitLambdaLVTIList(self, ctx:JayPyGrammarParser.LambdaLVTIListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#lambdaLVTIParameter.
    def visitLambdaLVTIParameter(self, ctx:JayPyGrammarParser.LambdaLVTIParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#pattern.
    def visitPattern(self, ctx:JayPyGrammarParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#primary.
    def visitPrimary(self, ctx:JayPyGrammarParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#switchExpression.
    def visitSwitchExpression(self, ctx:JayPyGrammarParser.SwitchExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#switchLabeledRule.
    def visitSwitchLabeledRule(self, ctx:JayPyGrammarParser.SwitchLabeledRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#guardedPattern.
    def visitGuardedPattern(self, ctx:JayPyGrammarParser.GuardedPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#switchRuleOutcome.
    def visitSwitchRuleOutcome(self, ctx:JayPyGrammarParser.SwitchRuleOutcomeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#arrayCreatorRest.
    def visitArrayCreatorRest(self, ctx:JayPyGrammarParser.ArrayCreatorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#primitiveType.
    def visitPrimitiveType(self, ctx:JayPyGrammarParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#typeArguments.
    def visitTypeArguments(self, ctx:JayPyGrammarParser.TypeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#arguments.
    def visitArguments(self, ctx:JayPyGrammarParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#typeArgument.
    def visitTypeArgument(self, ctx:JayPyGrammarParser.TypeArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#typeList.
    def visitTypeList(self, ctx:JayPyGrammarParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#typeType.
    def visitTypeType(self, ctx:JayPyGrammarParser.TypeTypeContext):
        return self.visitChildren(ctx)

    
    def extract_variables(self,expr):
        tree = ast.parse(expr, mode='eval')
        
        variables = set()

        class VariableVisitor(ast.NodeVisitor):
            def visit_Name(self, node):
                variables.add(node.id)
                self.generic_visit(node)
        
        visitor = VariableVisitor()
        visitor.visit(tree)
        
        return variables

    def replace_variables(self,expr, variables, values):
        for var in variables:
            if var in values:
                expr = re.sub(rf'\b{var}\b', str(values[var]), expr)
        return expr

    def preprocess_expression(self,expr):
        # Find all integers in the expression and wrap them with str()
        processed_expr = re.sub(r'(\b\d+\b)', r'str(\1)', expr)
        return processed_expr
    def pre_processString(self,string):
        return string.replace("&&", " and ").replace("||", " or ").replace("!", " not ").replace("TRUE", " True ").replace("FALSE", " False ").replace("++", "+1").replace("--", "-1").replace(" not =","!=")
    

    def process_function_arguments(self,parameters,arguments):
        arg_list = arguments.getText().split(',')
        param_list = parameters.getText().split(',')
        if len(param_list) == len(arg_list):
            for i in range(0,len(arguments.expression())):
                if type(eval(self.pre_processString(arguments.expression(i).getText()),{},self.scopes.mergeAllScopes())).__name__!=parameters.formalParameterList().formalParameter(i).typeType().getText() and not (type(eval(self.pre_processString(arguments.expression(i).getText()),{},self.scopes.mergeAllScopes())).__name__=="str" and parameters.formalParameterList().formalParameter(i).typeType().getText()=="String"):
                    return [False,type(eval(self.pre_processString(arguments.expression(i).getText()),{},self.scopes.mergeAllScopes())).__name__,parameters.formalParameterList().formalParameter(i).typeType().getText()]
        return True
    def evaluate_expression(self, expr, variables_dict, ctx):
        for var in variables_dict:
            if not isinstance(variables_dict[var], np.ndarray):
                variables_dict[var] = np.array(variables_dict[var])
        
        try:
            result = eval(expr, {}, variables_dict)
        except Exception as e:
            print(f"Error evaluating expression: {e}at line "+ str(ctx.start.line))
            sys.exit(1)
            return None
        
        return result
    def create_matrix_from_text(self,matrix_text):
        # Remove the curly braces and split into rows
        rows = matrix_text.strip('{}').split('},{')
        
        # Process each row
        matrix = []
        for row in rows:
            # Split the row into individual elements and convert to float
            matrix.append([float(x) for x in row.split(',')])
        
        # Optionally convert to a NumPy array
        matrix = np.array(matrix)
        
        return matrix




del JayPyGrammarParser