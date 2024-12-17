from dataclean import Clean
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


clean = Clean()
df = clean.data_cleaner()

class Transform:
    def __init__(self):
        pass

    def transformer(self):
        encoder = LabelEncoder()
        df['diagnosis'] = encoder.fit_transform(df['diagnosis'])

        x = df.drop('diagnosis', axis = 1)
        y = df['diagnosis']

        sc = StandardScaler()
        x = sc.fit_transform(x)

        return x, y 


