letter = ''' 
    Dear <|NAME|>, 
    You are selected! 
    <|DATE|> 
    '''
    
str=letter.replace("<|NAME|>","shailesh",).replace("<|DATE|>","20/12/2222")
print(str)
print(letter)