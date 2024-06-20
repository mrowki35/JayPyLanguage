import re
class ScopeHandler:
    def __init__(self):
        self.local_scope = {}

    def mergeAllScopes(self):
        return self.local_scope

    def addToLocalScope(self, var, value, value_type):
        self.local_scope[var] = value


def translate_java_to_python(java_function):

    def_pattern = re.compile(r'\b(\w+)\s+(\w+)\s*\(([^)]*)\)\s*{')
    def_match = def_pattern.search(java_function)
    
    if not def_match:
        raise ValueError("Invalid Java function syntax")
    
    return_type, function_name, params = def_match.groups()
    params = re.sub(r'\b\w+\s+', '', params)  

    python_function = f"def {function_name}({params}):\n"
    
    body = java_function[def_match.end():].strip()
    
    body = re.sub(r'\b\w+\s+(\w+)\s*=', r'\1 =', body)
    

    body = re.sub(r'return', 'return', body)
    body = re.sub(r'(\w+)\(', r'\1(', body) 

    body = body.replace('{', '').replace('}', '')
    body = re.sub(r'if\s*\((.*?)\)', r'if \1:', body)
    body = re.sub(r'else if\s*\((.*?)\)', r'elif \1:', body)
    body = re.sub(r'else\s*', 'else:', body)
    body = re.sub(r'for\s*\((.*?);(.*?);(.*?)\)', r'for \1; \2; \3:', body)
    body = re.sub(r'while\s*\((.*?)\)', r'while \1:', body)

    body = re.sub(r'println\((.*?)\);', r'print(\1)', body)
    body = re.sub(r'print\((.*?)\);', r'print(\1, end="")', body)
    
    body = re.sub(r'"\s*\+\s*(\w+)\s*\+\s*"', r'\" \1 \"', body)

    body_lines = body.split(';')
    for line in body_lines:
        line = line.strip()
        if line:
            python_function += f"    {line}\n"

    return python_function

def execute_translated_function(python_function, function_name, scopes):

    local_scope = scopes.mergeAllScopes()
    exec_globals = {}


    exec_globals[function_name] = None

    exec(python_function, exec_globals, local_scope)

    func = local_scope[function_name]
    local_scope[function_name] = func
    exec_globals[function_name] = func

    return func

def execute_translated_function(python_function, function_name, scopes):

    local_scope = scopes.mergeAllScopes()
    exec_globals = {}


    exec_globals[function_name] = None


    
    exec(python_function, exec_globals, local_scope)
    


    func = local_scope[function_name]
    local_scope[function_name] = func
    exec_globals[function_name] = func

    return func
