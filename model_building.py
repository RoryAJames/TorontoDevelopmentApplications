import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('data\predict_page.csv')

#Establish X and y

X = df.drop("Status", axis=1)
y = df["Status"]

#Establish the hold out set to test cross val after fitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

#Create an instance of income scaler to be passed to pickle file
income_scaler = StandardScaler()
X_train['Average_Income'] = income_scaler.fit_transform(X_train['Average_Income'].values.reshape(-1,1))
X_train['Average_Income'] = income_scaler.transform(X_train['Average_Income'].values.reshape(-1,1))

#Since the dataset is imbalanced use stratified KFold to make equal size sets
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

pipelines = {
    'Logistic': make_pipeline(LogisticRegression(random_state=42, max_iter=1000)),
    'RandomForest': make_pipeline(RandomForestClassifier(random_state=42))
    }

#Establish hyperparameter dictionary for each model

hyperparameters = {
    
'Logistic' : {
    'logisticregression__C': [0.01, 0.1, 1, 10], 
    'logisticregression__penalty' : ['none','l1', 'l2'],
    'logisticregression__solver' : ['lbfgs','liblinear']
    },

'RandomForest' : {
     'randomforestclassifier__n_estimators' : [50, 100, 150, 200],
     'randomforestclassifier__max_depth' : [3, 5, 10, 15], 
     'randomforestclassifier__min_samples_split' : [2, 5, 10],
     'randomforestclassifier__min_samples_leaf' : [3, 5, 10, 15]
    }
}

fitted_models = {} #Establishes a dictionary that will hold the model and its best performing hyperparameters

# Grid search each model and hyperparameter with the stratified five fold  cross validation sets

for name, pipeline in pipelines.items():
    model = GridSearchCV(pipeline, 
                         hyperparameters[name], 
                         cv=cv,
                         scoring='roc_auc',
                         return_train_score = False)
    model.fit(X_train, y_train)
    fitted_models[name] = model

for name, model in fitted_models.items():
   pred = model.predict(X_test)
   print(name)
   print(' — — — — ')
   print('Accuracy:', accuracy_score(y_test, pred))
   print('Precision:', precision_score(y_test, pred))
   print('Recall:', recall_score(y_test, pred))
   print('ROC AUC:', roc_auc_score(y_test, pred))
   print() 
   print('This models best performing parameters are ' + str(model.best_params_))
   print()

print(model.best_params_)

#Dump the best performing model to pickle file

data = {"model": model, "income_scaler": income_scaler}
with open('prediction_model.pkl', 'wb') as file:
    pickle.dump(data, file)