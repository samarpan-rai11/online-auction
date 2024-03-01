import pickle
import pandas as pd

# Load your model
loaded_model = pickle.load(open('LRModel.pkl', 'rb'))

# New data for prediction
new_data = pd.DataFrame({
    'bid': [12000, 76.00],
    'bidtime': [5, 6.359294],
    'openbid': [12020, 0.01],
    'item': ['Cartier Watch', 'Xbox Console'],
    'auction_type': ['5 day auction', '7 day auction'],
})

# Ensure that the new data is preprocessed in the same way as the training data
# (e.g., one-hot encoding for categorical variables)

# Make predictions
def predict_price(rawdata):
    auction_type = f"{rawdata['auction_type']} day auction"
    data_to_predict = pd.DataFrame({
    'bid': [rawdata['bid']],
    'bidtime': [rawdata['bidtime']],
    'openbid': [rawdata['openbid']],
    'item': [rawdata['item']],
    'auction_type': [ auction_type ],
})
    predictions = loaded_model.predict(data_to_predict)
    return predictions

# Print or use the predictions as needed
