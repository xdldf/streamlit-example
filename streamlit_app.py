import pickle
# Импортируем все пакеты, которые необходимы для вашей модели
import numpy as np
import sys
from sklearn.neighbors import KNeighborsClassifier

# Импортируем Flask для создания API
from flask import Flask, request

# Загружаем обученную модель из текущего каталога
with open('./model.pkl', 'rb') as model_pkl:
   knn = pickle.load(model_pkl)

# Инициализируем приложение Flask
app = Flask(__name__)

# Создайте конечную точку API
@app.route('/predict')
def predict_iris():
   # Считываем все необходимые параметры запроса
   sl = request.args.get('sl')
   sw = request.args.get('sw')
   pl = request.args.get('pl')
   pw = request.args.get('pw')

# Используем метод модели predict для
# получения прогноза для неизвестных данных
   unseen = np.array([[sl, sw, pl, pw]])
   result = knn.predict(unseen)
  # возвращаем результат 
   return 'Predicted result for observation ' + str(unseen) + ' is: ' + str(result)
if __name__ == '__main__':
   app.run()
