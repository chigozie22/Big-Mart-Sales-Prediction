import pandas as pd 
from sklearn.model_selection import train_test_split
from dagster import multi_asset, AssetOut, asset, MetadataValue, AutoMaterializePolicy
from sklearn import preprocessing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
import seaborn
from io import BytesIO
import base64
import matplotlib.pyplot as plt
# from sklearn.metrics import r2_score, mean_absolute_error

@asset
def training_data():
    train_data = pd.read_csv('C:/Users/J.C/Desktop/PROJECTS-CHINONSO/Data-Science-Projects/Projects/4/tutorial/train_kOBLwZA.csv')
    data = pd.DataFrame(train_data)
    return data

@asset
def process_training_data(training_data):
    trainer = training_data
    trainer['Item_Weight'] = trainer['Item_Weight'].fillna(trainer.groupby('Item_Identifier')['Item_Weight'].transform('max'))
    trainer['Outlet_Size'] = trainer['Outlet_Size'].fillna('Small')
    df = trainer[trainer['Item_Weight'].notna()]
    df.replace({'Item_Fat_Content':{'low fat': 'Low Fat', 'LF': 'Low Fat', 'reg': 'Regular' }}, inplace=True)
    df['Outlet_Age'] = 2024 - df['Outlet_Establishment_Year']
    df.drop(columns='Outlet_Establishment_Year')

    
    return df

@asset
def feature_engineering(process_training_data):
    dataset = process_training_data
    labels = preprocessing.LabelEncoder()
    cols_to_encode = ['Item_Fat_Content', 'Outlet_Identifier', 'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type' ]
    
    for i in cols_to_encode:
        dataset[i] = labels.fit_transform(dataset[i])

    df_new = dataset.drop(columns=['Item_Identifier'])
    df_new = pd.get_dummies(df_new)

    return df_new

@multi_asset(outs={"training_data_X": AssetOut(), "training_data_y": AssetOut()})
def splitting_data(feature_engineering):
    csv = feature_engineering
    X = csv.drop(columns=['Item_Outlet_Sales'])
    y = csv['Item_Outlet_Sales']

    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22222)

    return X, y


# def make_plot(scores):
#     plt.clf()
#     training_plot = seaborn.lineplot(scores)
#     fig = training_plot.get_figure()
#     buffer = BytesIO()
#     fig.savefig(buffer)
#     image_data = base64.b64encode(buffer.getvalue())
#     return MetadataValue.md(f"![img](data:image/png;base64, {image_data.decode()})")



@multi_asset(outs={"gbm": AssetOut(),  "prediction_data": AssetOut()})
def training_model(training_data_X, training_data_y):
    X_train, X_test, y_train, y_test = train_test_split(training_data_X, training_data_y, test_size=0.2, random_state=22222)
    gbm = GradientBoostingRegressor()

    gbm.fit(X_train, y_train)

    return gbm, (X_test, y_test)





@multi_asset(outs={"predictions" : AssetOut(), "score": AssetOut()})
def testing_score(gbm, prediction_data):
    X_test_1, y_test_1 = prediction_data
    gbm_model = gbm
    score = cross_val_score(gbm_model, X_test_1, y_test_1, cv=5)

    #
    y_pred = gbm_model.predict(X_test_1)
    return y_pred, score


# def test_data():
#     test_data =  pd.read_csv('C:/Users/J.C/Desktop/PROJECTS-CHINONSO/Data-Science-Projects/Projects/4/tutorial/test_t02dQwI.csv')
   