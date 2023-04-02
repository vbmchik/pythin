from pprint import pprint
import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
exams = pd.DataFrame(exam_data, index=labels)
pprint(exams[(exams.score > 12) & (exams.score < 15)])
pprint(exams.attempts.sum())
exams.sort_values(by=['name', 'score'], ascending=[False,True])
exams['name'] = exams['name'].replace('James', 'Matteo')
exams['name']['a'] = 'BooBoo'
pprint(exams)