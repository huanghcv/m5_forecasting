import pickle
# pd.set_option('display.max_colwidth', 100)

with open('train_data.pkl', 'rb') as f:
    data = pickle.load(f)
data.dropna(inplace=True)
data.head(2000).to_csv('test.csv')

print(data)
