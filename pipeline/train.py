from src.datasplit import Split
from model import Models
import pickle

split = Split()
models = Models()

x_train, x_test, y_train, y_test = split.spliter()
grid = models.sv_model()
grid.fit(x_train, y_train)
model = grid.best_estimator_

pickle.dump(model)