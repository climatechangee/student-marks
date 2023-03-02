import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mydata = pd.read_excel('C:\\Users\\Ahmed\\Desktop\\statstic\\studentMarks.xlsx')

mydata.hist(figsize=(20,30))

import seaborn as sns

sns.boxplot(x="gender", y="math score", data=mydata)

pd.crosstab(mydata['reading score'],mydata['gender'] )

sns.countplot(x="test preparation course", hue="reading score", data=mydata)


pd.pivot_table(mydata, index=['test preparation course', 'gender'], columns=[ 'math score'], aggfunc=len)

sns.pairplot(mydata)

mydata['math score'].mean()

sns.distplot(mydata['math score'])

mydata.hist(by='gender',column = 'test preparation course')

mydata.hist(by='gender',column = 'math score', figsize=(20,30))

corr = mydata.corr()
sns.heatmap(corr, annot=True)