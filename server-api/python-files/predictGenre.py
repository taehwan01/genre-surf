# 라이브러리
import sys
import zipfile
import time
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def unzipDataset():
    datasetZip = zipfile.ZipFile('./python-files/gtzan-dataset-music-genre-classification.zip')
    datasetZip.extractall('./python-files')
    datasetZip.close()

def trainByXGB():
    # print('\nGetting training data from csv...')
    data = pd.read_csv('./python-files/Data/features_3_sec.csv')

    # print('\nSplitting data to X, Y...')
    data = data.drop('filename', axis = 'columns')
    data = data.drop('length', axis = 'columns')
    X = data.loc[:, data.columns != 'label' ]
    Y = data['label']
    
    # 음악적 특성 값의 범위 정규화
    # print('\nNormalizing data...')
    cols = X.columns
    min_max_scaler = preprocessing.MinMaxScaler()
    np_scaled = min_max_scaler.fit_transform(X)
    
    # 범위 정규화를 거친 데이터에 대한 데이터 프레임
    X = pd.DataFrame(np_scaled, columns = cols)

    # print('\nSplitting training data(70%) and test data(30%)...')
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # print('\nChanging genre labels to numbers...')
    le = LabelEncoder()
    Y_train = le.fit_transform(Y_train)

    # print('\nTraining model...')
    xgb = XGBClassifier(n_estimators=1000, learning_rate=0.05)
    xgb.fit(X_train.values, Y_train)

    # print('\nTesting...')
    # prediction = xgb.predict(X_test)

    # Y_test = le.fit_transform(Y_test)
    # print('\nAccuracy: ', round(accuracy_score(Y_test, prediction) * 100, 5), '%')

    return xgb


def getGenre(audioFeatures, xgb):
    genreLabels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
    
    newAudioDataFrame = pd.DataFrame.from_dict([audioFeatures])
    genreIndex = xgb.predict(newAudioDataFrame)

    index = genreIndex[0]
    genre = genreLabels[index]

    return genre


def main(audioFeat):
    unzipDataset()
    time.sleep(5)
    audioFeatures = eval(audioFeat)
    xgb = trainByXGB()
    genre = getGenre(audioFeatures, xgb)
    print(genre, end = '')


if __name__ == '__main__':
    main(sys.argv[1])