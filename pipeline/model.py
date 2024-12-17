from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

class Models:
    def __init__(self):
        pass
    def sv_model(self):
        sv = SVC()
        params = {
            'C': [1,10,100],
            'kernel': ['linear', 'rbf'],
            'gamma': ['scale', 'auto']
        }
        grid =  GridSearchCV(estimator=sv, cv=5, scoring='accuracy', param_grid=params)
        return grid