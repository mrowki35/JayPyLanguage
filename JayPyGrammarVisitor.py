# Generated from C:/Javalib/test/JayPyGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .JayPyGrammarParser import JayPyGrammarParser
else:
    from JayPyGrammarParser import JayPyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by JayPyGrammarParser.

class JayPyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JayPyGrammarParser#program.
    def visitProgram(self, ctx:JayPyGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:JayPyGrammarParser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:JayPyGrammarParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#variableDeclaratorId.
    def visitVariableDeclaratorId(self, ctx:JayPyGrammarParser.VariableDeclaratorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#variableInitializer.
    def visitVariableInitializer(self, ctx:JayPyGrammarParser.VariableInitializerContext):
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


    # Visit a parse tree produced by JayPyGrammarParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:JayPyGrammarParser.IntegerLiteralContext):
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#blockStatement.
    def visitBlockStatement(self, ctx:JayPyGrammarParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx:JayPyGrammarParser.LocalVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#identifier.
    def visitIdentifier(self, ctx:JayPyGrammarParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#typeIdentifier.
    def visitTypeIdentifier(self, ctx:JayPyGrammarParser.TypeIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#statement.
    def visitStatement(self, ctx:JayPyGrammarParser.StatementContext):
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
    def visitMethodCall(self, ctx:JayPyGrammarParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JayPyGrammarParser#expression.
    def visitExpression(self, ctx:JayPyGrammarParser.ExpressionContext):
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



del JayPyGrammarParser