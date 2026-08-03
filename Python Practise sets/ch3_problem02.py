letter = ''' Dear <|Name|>
         You Are Selected
         As the Chief Executive of 
         \'KYZIN Motors\'
         on <|Date|>'''



print(letter.replace("<|Name|>", "Bhoomick").replace("<|Date|>" , "09 December 2099"))