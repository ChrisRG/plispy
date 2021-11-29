### Types
Symbol = str
List = list
Number = (int, float)

### Parser
def tokenize(chars: str) -> list:
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()
