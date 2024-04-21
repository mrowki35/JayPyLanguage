# Generated from C:/Javalib/test/JayPyGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .JayPyGrammarParser import JayPyGrammarParser
else:
    from JayPyGrammarParser import JayPyGrammarParser

from VariablesList import VariablesList

# This class defines a complete listener for a parse tree produced by JayPyGrammarParser.
class JayPyGrammarListener(ParseTreeListener):
    def __init__(self):
        self.my_variable_list = VariablesList()


    # Enter a parse tree produced by JayPyGrammarParser#program.
    def enterProgram(self, ctx:JayPyGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#program.
    def exitProgram(self, ctx:JayPyGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:JayPyGrammarParser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:JayPyGrammarParser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:JayPyGrammarParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:JayPyGrammarParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#methodBody.
    def enterMethodBody(self, ctx:JayPyGrammarParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#methodBody.
    def exitMethodBody(self, ctx:JayPyGrammarParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#typeTypeOrVoid.
    def enterTypeTypeOrVoid(self, ctx:JayPyGrammarParser.TypeTypeOrVoidContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#typeTypeOrVoid.
    def exitTypeTypeOrVoid(self, ctx:JayPyGrammarParser.TypeTypeOrVoidContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#typeTypeOrVar.
    def enterTypeTypeOrVar(self, ctx:JayPyGrammarParser.TypeTypeOrVarContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#typeTypeOrVar.
    def exitTypeTypeOrVar(self, ctx:JayPyGrammarParser.TypeTypeOrVarContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:JayPyGrammarParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:JayPyGrammarParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#variableDeclarators.
    def enterVariableDeclarators(self, ctx:JayPyGrammarParser.VariableDeclaratorsContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#variableDeclarators.
    def exitVariableDeclarators(self, ctx:JayPyGrammarParser.VariableDeclaratorsContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:JayPyGrammarParser.VariableDeclaratorContext):
        #print(ctx.getChild(0).getText())
        variable_name=ctx.variableDeclaratorId().getText()
        variable_type=ctx.parentCtx.parentCtx.typeType().getText()
        #print(ctx.parentCtx.__class__.__name__) -> VariableDeclaratorsContext
        try:
            variable_value=ctx.variableInitializer().getText()
        except (AttributeError):
            variable_value=None
        if variable_value==None:
            self.my_variable_list.variablesList.append({variable_name:[variable_value,variable_type]})
        elif variable_type=="float" or variable_type=='double':
            #self.my_variable_list.variablesList.append({variable_name:Float(variable_name,variable_value)})
            self.my_variable_list.variablesList.append({variable_name:[float(variable_value),variable_type]})
        elif variable_type in ('int','long','short'):
            self.my_variable_list.variablesList.append({variable_name:[int(variable_value),variable_type]})
        elif variable_type in ("String","string",'char'):
            self.my_variable_list.variablesList.append({variable_name:[variable_value.strip('"'),variable_type]})
        elif variable_type=='boolean' and variable_value in ('false','False','0'):
            self.my_variable_list.variablesList.append({variable_name:[False,variable_type]})
        elif variable_type=='boolean':
            self.my_variable_list.variablesList.append({variable_name:[bool(variable_value),variable_type]})
        else:
            self.my_variable_list.variablesList.append({variable_name:[variable_value,variable_type]})
        
        
        #self.my_variable_list.variablesList.append({variable_name,variable_value})
        #print(ctx.variableDeclaratorId().getText())
       # print(ctx.variableInitializer().getText())
        pass


    # Exit a parse tree produced by JayPyGrammarParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:JayPyGrammarParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:JayPyGrammarParser.VariableDeclaratorIdContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#variableDeclaratorId.
    def exitVariableDeclaratorId(self, ctx:JayPyGrammarParser.VariableDeclaratorIdContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#variableInitializer.
    def enterVariableInitializer(self, ctx:JayPyGrammarParser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#variableInitializer.
    def exitVariableInitializer(self, ctx:JayPyGrammarParser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#arrayInitializer.
    def enterArrayInitializer(self, ctx:JayPyGrammarParser.ArrayInitializerContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#arrayInitializer.
    def exitArrayInitializer(self, ctx:JayPyGrammarParser.ArrayInitializerContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#qualifiedNameList.
    def enterQualifiedNameList(self, ctx:JayPyGrammarParser.QualifiedNameListContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#qualifiedNameList.
    def exitQualifiedNameList(self, ctx:JayPyGrammarParser.QualifiedNameListContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#formalParameters.
    def enterFormalParameters(self, ctx:JayPyGrammarParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#formalParameters.
    def exitFormalParameters(self, ctx:JayPyGrammarParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#receiverParameter.
    def enterReceiverParameter(self, ctx:JayPyGrammarParser.ReceiverParameterContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#receiverParameter.
    def exitReceiverParameter(self, ctx:JayPyGrammarParser.ReceiverParameterContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#formalParameterList.
    def enterFormalParameterList(self, ctx:JayPyGrammarParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#formalParameterList.
    def exitFormalParameterList(self, ctx:JayPyGrammarParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#formalParameter.
    def enterFormalParameter(self, ctx:JayPyGrammarParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#formalParameter.
    def exitFormalParameter(self, ctx:JayPyGrammarParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#lastFormalParameter.
    def enterLastFormalParameter(self, ctx:JayPyGrammarParser.LastFormalParameterContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#lastFormalParameter.
    def exitLastFormalParameter(self, ctx:JayPyGrammarParser.LastFormalParameterContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#qualifiedName.
    def enterQualifiedName(self, ctx:JayPyGrammarParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#qualifiedName.
    def exitQualifiedName(self, ctx:JayPyGrammarParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#literal.
    def enterLiteral(self, ctx:JayPyGrammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#literal.
    def exitLiteral(self, ctx:JayPyGrammarParser.LiteralContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:JayPyGrammarParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:JayPyGrammarParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#floatLiteral.
    def enterFloatLiteral(self, ctx:JayPyGrammarParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#floatLiteral.
    def exitFloatLiteral(self, ctx:JayPyGrammarParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#elementValuePairs.
    def enterElementValuePairs(self, ctx:JayPyGrammarParser.ElementValuePairsContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#elementValuePairs.
    def exitElementValuePairs(self, ctx:JayPyGrammarParser.ElementValuePairsContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#elementValuePair.
    def enterElementValuePair(self, ctx:JayPyGrammarParser.ElementValuePairContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#elementValuePair.
    def exitElementValuePair(self, ctx:JayPyGrammarParser.ElementValuePairContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#elementValue.
    def enterElementValue(self, ctx:JayPyGrammarParser.ElementValueContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#elementValue.
    def exitElementValue(self, ctx:JayPyGrammarParser.ElementValueContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#elementValueArrayInitializer.
    def enterElementValueArrayInitializer(self, ctx:JayPyGrammarParser.ElementValueArrayInitializerContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#elementValueArrayInitializer.
    def exitElementValueArrayInitializer(self, ctx:JayPyGrammarParser.ElementValueArrayInitializerContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#block.
    def enterBlock(self, ctx:JayPyGrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#block.
    def exitBlock(self, ctx:JayPyGrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#blockStatement.
    def enterBlockStatement(self, ctx:JayPyGrammarParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#blockStatement.
    def exitBlockStatement(self, ctx:JayPyGrammarParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:JayPyGrammarParser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:JayPyGrammarParser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#identifier.
    def enterIdentifier(self, ctx:JayPyGrammarParser.IdentifierContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#identifier.
    def exitIdentifier(self, ctx:JayPyGrammarParser.IdentifierContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#typeIdentifier.
    def enterTypeIdentifier(self, ctx:JayPyGrammarParser.TypeIdentifierContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#typeIdentifier.
    def exitTypeIdentifier(self, ctx:JayPyGrammarParser.TypeIdentifierContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#statement.
    def enterStatement(self, ctx:JayPyGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#statement.
    def exitStatement(self, ctx:JayPyGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#switchBlockStatementGroup.
    def enterSwitchBlockStatementGroup(self, ctx:JayPyGrammarParser.SwitchBlockStatementGroupContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#switchBlockStatementGroup.
    def exitSwitchBlockStatementGroup(self, ctx:JayPyGrammarParser.SwitchBlockStatementGroupContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#switchLabel.
    def enterSwitchLabel(self, ctx:JayPyGrammarParser.SwitchLabelContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#switchLabel.
    def exitSwitchLabel(self, ctx:JayPyGrammarParser.SwitchLabelContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#forControl.
    def enterForControl(self, ctx:JayPyGrammarParser.ForControlContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#forControl.
    def exitForControl(self, ctx:JayPyGrammarParser.ForControlContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#forInit.
    def enterForInit(self, ctx:JayPyGrammarParser.ForInitContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#forInit.
    def exitForInit(self, ctx:JayPyGrammarParser.ForInitContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#enhancedForControl.
    def enterEnhancedForControl(self, ctx:JayPyGrammarParser.EnhancedForControlContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#enhancedForControl.
    def exitEnhancedForControl(self, ctx:JayPyGrammarParser.EnhancedForControlContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#parExpression.
    def enterParExpression(self, ctx:JayPyGrammarParser.ParExpressionContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#parExpression.
    def exitParExpression(self, ctx:JayPyGrammarParser.ParExpressionContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#expressionList.
    def enterExpressionList(self, ctx:JayPyGrammarParser.ExpressionListContext):
        pass


    # Exit a parse tree produced by JayPyGrammarParser#expressionList.
    def exitExpressionList(self, ctx:JayPyGrammarParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#methodCall.
    def enterMethodCall(self, ctx:JayPyGrammarParser.MethodCallContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#methodCall.
    def exitMethodCall(self, ctx:JayPyGrammarParser.MethodCallContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#expression.
    def enterExpression(self, ctx:JayPyGrammarParser.ExpressionContext):
       # print(ctx.getText())
        if ctx.ASSIGN() != None:
            for dictionary in self.my_variable_list.variablesList:
                if dictionary.get(ctx.expression()[0].getText())!=None:
                    dictionary.get(ctx.expression()[0].getText())[0]=ctx.expression()[1].getText()
        elif ctx.ADD_ASSIGN() !=None:
            pass
        elif ctx.SUB_ASSIGN() !=None:
            pass
        elif ctx.MUL_ASSIGN() !=None:
            pass
        elif ctx.DIV_ASSIGN() !=None:
            pass
        elif ctx.ADD() !=None:
            print(ctx.getText())
            print(ctx.expression()[0].getText())
            for dictionary in self.my_variable_list.variablesList:
                if dictionary.get(ctx.expression()[0].getText())!=None:
                    #print(dictionary.get(ctx.expression()[0].getText())[0])
                   # print("here")
                    value=dictionary.get(ctx.expression()[0].getText())[0]+float(ctx.expression()[1].getText())
                   # value=dictionary.get(ctx.expression()[0].getText())[0]+float(ctx.expression()[1].getText())
                   #=dictionary.get(ctx.expression()[0].getText())[0]
                    print(value)
        elif ctx.SUB() !=None:
            pass
        elif ctx.INC() !=None:
            pass
        elif ctx.DEC() !=None:
            pass
        elif ctx.MUL() !=None:
            pass
        elif ctx.DIV() !=None:
            pass
        elif ctx.MOD() !=None:
            pass
        elif ctx.MUL() !=None:
            pass        

        pass

    # Exit a parse tree produced by JayPyGrammarParser#expression.
    def exitExpression(self, ctx:JayPyGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#lambdaParameters.
    def enterLambdaParameters(self, ctx:JayPyGrammarParser.LambdaParametersContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#lambdaParameters.
    def exitLambdaParameters(self, ctx:JayPyGrammarParser.LambdaParametersContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#lambdaExpression.
    def enterLambdaExpression(self, ctx:JayPyGrammarParser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#lambdaExpression.
    def exitLambdaExpression(self, ctx:JayPyGrammarParser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#lambdaBody.
    def enterLambdaBody(self, ctx:JayPyGrammarParser.LambdaBodyContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#lambdaBody.
    def exitLambdaBody(self, ctx:JayPyGrammarParser.LambdaBodyContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#lambdaLVTIList.
    def enterLambdaLVTIList(self, ctx:JayPyGrammarParser.LambdaLVTIListContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#lambdaLVTIList.
    def exitLambdaLVTIList(self, ctx:JayPyGrammarParser.LambdaLVTIListContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#lambdaLVTIParameter.
    def enterLambdaLVTIParameter(self, ctx:JayPyGrammarParser.LambdaLVTIParameterContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#lambdaLVTIParameter.
    def exitLambdaLVTIParameter(self, ctx:JayPyGrammarParser.LambdaLVTIParameterContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#pattern.
    def enterPattern(self, ctx:JayPyGrammarParser.PatternContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#pattern.
    def exitPattern(self, ctx:JayPyGrammarParser.PatternContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#primary.
    def enterPrimary(self, ctx:JayPyGrammarParser.PrimaryContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#primary.
    def exitPrimary(self, ctx:JayPyGrammarParser.PrimaryContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#switchExpression.
    def enterSwitchExpression(self, ctx:JayPyGrammarParser.SwitchExpressionContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#switchExpression.
    def exitSwitchExpression(self, ctx:JayPyGrammarParser.SwitchExpressionContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#switchLabeledRule.
    def enterSwitchLabeledRule(self, ctx:JayPyGrammarParser.SwitchLabeledRuleContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#switchLabeledRule.
    def exitSwitchLabeledRule(self, ctx:JayPyGrammarParser.SwitchLabeledRuleContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#guardedPattern.
    def enterGuardedPattern(self, ctx:JayPyGrammarParser.GuardedPatternContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#guardedPattern.
    def exitGuardedPattern(self, ctx:JayPyGrammarParser.GuardedPatternContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#switchRuleOutcome.
    def enterSwitchRuleOutcome(self, ctx:JayPyGrammarParser.SwitchRuleOutcomeContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#switchRuleOutcome.
    def exitSwitchRuleOutcome(self, ctx:JayPyGrammarParser.SwitchRuleOutcomeContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#arrayCreatorRest.
    def enterArrayCreatorRest(self, ctx:JayPyGrammarParser.ArrayCreatorRestContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#arrayCreatorRest.
    def exitArrayCreatorRest(self, ctx:JayPyGrammarParser.ArrayCreatorRestContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#primitiveType.
    def enterPrimitiveType(self, ctx:JayPyGrammarParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#primitiveType.
    def exitPrimitiveType(self, ctx:JayPyGrammarParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#typeArguments.
    def enterTypeArguments(self, ctx:JayPyGrammarParser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#typeArguments.
    def exitTypeArguments(self, ctx:JayPyGrammarParser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#arguments.
    def enterArguments(self, ctx:JayPyGrammarParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#arguments.
    def exitArguments(self, ctx:JayPyGrammarParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#typeArgument.
    def enterTypeArgument(self, ctx:JayPyGrammarParser.TypeArgumentContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#typeArgument.
    def exitTypeArgument(self, ctx:JayPyGrammarParser.TypeArgumentContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#typeList.
    def enterTypeList(self, ctx:JayPyGrammarParser.TypeListContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#typeList.
    def exitTypeList(self, ctx:JayPyGrammarParser.TypeListContext):
        pass


    # Enter a parse tree produced by JayPyGrammarParser#typeType.
    def enterTypeType(self, ctx:JayPyGrammarParser.TypeTypeContext):
        pass

    # Exit a parse tree produced by JayPyGrammarParser#typeType.
    def exitTypeType(self, ctx:JayPyGrammarParser.TypeTypeContext):
        pass



del JayPyGrammarParser