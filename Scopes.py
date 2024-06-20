from collections import deque
from collections import deque

class Scope:
    def __init__(self):
        self.scopes = deque()  
        self.local_scopes_types = deque()

    def enterLocalScope(self):
        self.scopes.appendleft({})
        self.local_scopes_types.appendleft({})
        
    def getMainScope(self):
        if self.scopes:
            return self.scopes[-1]
        else:
            return {}

    def addToLocalScope(self, variable, value, vartype):
        if self.scopes:
            current_scope = self.scopes[0]
            current_scope[variable] = value
        if self.local_scopes_types:
            current_scope = self.local_scopes_types[0]
            current_scope[variable] = vartype

    def exitLocalScope(self):
        if self.scopes:
            self.scopes.popleft()
        if self.local_scopes_types:
            self.local_scopes_types.popleft() 

    def addToCurrentScope(self, name, value):
        if self.scopes:
            self.scopes[0][name] = value  

    def getCurrentScope(self):
        if self.scopes:
            return self.scopes[0]
        else:
            return {}
    def getCurrentTypesScope(self):
        if self.local_scopes_types:
            return self.local_scopes_types[0]
        else:
            return {}
    def mergeAllScopes(self):
        merged_scope = {}

        for scope in reversed(self.scopes):
            merged_scope.update(scope)
        return merged_scope
    def mergeAllTypesScopes(self):
        merged_scope = {}

        for scope in reversed(self.local_scopes_types):
            merged_scope.update(scope)
        return merged_scope
