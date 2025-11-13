##write a program to fill the template given below name and date.
'''
letter= Dear <|Name|>
        you are selected
        <|Date|>
         '''
letter= '''Dear, <|Name|>
        you are selected
        <|Date|>'''
print(letter.replace("<|Name|>","Harsh chauhan").replace("<|Date|>","9 novermber"))
