import pandas as pd
 

data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18],'Qualification':['MCA', 'MTech', 'MBA', 'MBBS']}
 

df = pd.DataFrame(data)
 
print(df)