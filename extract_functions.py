import re

def extract_functions(code):

    function_chunks = re.split(r'}\n{2,}', code)
    

    functions = {}
    

    function_name_pattern = re.compile(r'\b(int|void|float|double|char|long|short|bool)\s+(\w+)\s*\([^)]*\)\s*{')
    
    for chunk in function_chunks:
        chunk = chunk.strip()
        if not chunk:
            continue

        if not chunk.endswith('}'):
            chunk += '}'
            
        open_braces = chunk.count('{')
        close_braces = chunk.count('}')
        

        while open_braces > close_braces:
            chunk += '}'
            close_braces += 1

        match = function_name_pattern.search(chunk)
        if match:
            function_name = match.group(2)
            functions[function_name] = chunk
    
    return functions

