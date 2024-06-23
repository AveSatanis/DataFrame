import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'Human':lst}) 
data.loc[:, "Robot"] = lst
data['Human'] = (data['Human']== 'human')
data['Robot'] = (data['Robot']== 'robot')
print(data.head())