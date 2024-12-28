letter = '''
        Dear <|Name|>,
        You Are Selected
        <|Date|>'''
print(letter.replace("<|Name|>","Manjot").replace("<|Date|>","25 june 2005"))