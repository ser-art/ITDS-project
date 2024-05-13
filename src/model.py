import xgboost as xgb
import pandas as pd


def run(features, threshold=0.5) -> int:
    # Load the model
    loaded_model = xgb.Booster()
    loaded_model.load_model("model.json")

    # Convert the features argument to a DataFrame
    input_df = pd.DataFrame([features])

    # Convert the DataFrame to DMatrix
    cols = list(input_df.columns)
    data_dmatrix = xgb.DMatrix(input_df, feature_names=cols)

    # Make predictions
    predictions = loaded_model.predict(data_dmatrix)

    # Convert probabilities to binary outcome
    prediction_output = [1 if x >= threshold else 0 for x in predictions]
    return prediction_output[0]
