
# Importing the libraries
import warnings
warnings.filterwarnings("ignore")
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
import pandas as pd

interim_data = pd.read_csv('innercity.csv')

#converting dayhours into date time format
interim_data['dayhours']=pd.to_datetime(interim_data['dayhours'])
interim_data['dayhours']=interim_data['dayhours'].apply(lambda x: x.strftime('%d%m%Y'))

#Converting dayhours into int data type
interim_data['dayhours']=interim_data.dayhours.astype(int)

interim_data=interim_data.round({"room_bath":0})


# Splitting the data into train, test and validation
X= interim_data.drop(["price"], axis=1)
y= interim_data[['price']] 

X_train, X_test, y_train, y_test= train_test_split(X,y, test_size=0.30, random_state=0)
X_train, X_val, y_train, Y_val= train_test_split(X_train, y_train, test_size=0.30,random_state=1)


# Gradient Descent Regressor
gbcl = GradientBoostingRegressor(n_estimators = 50, learning_rate = 0.09, max_depth=5)
gbcl = gbcl.fit(X_train, y_train)


# Hyperparameter Tuning
parameters= {'learning_rate': [0.01, 0.02], 'subsample': [0.9, 0.5], 'n_estimators': [100,500], 'max_depth': [4,6]}
grid5= GridSearchCV(estimator=gbcl, param_grid= parameters, cv=3, n_jobs=-1)
grid5.fit(X_train,y_train)
    


# Dumping the model object
pickle.dump(grid5,open("grid5.pkl",'wb'))

# Reloading the model object
grid5=pickle.load(open('grid5.pkl','rb'))
print(grid5.predict([[3034200666,2014-11-7,4,3,3020,13457,1,0,0,5,9,3020,0,1956,0,98133,47,-122,2120,7553,1,16477]]))