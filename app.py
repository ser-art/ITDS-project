import streamlit as st
import fire

from src import model


def main():
    # Streamlit interface
    st.title("Airline Satisfaction Prediction")

    # Create inputs for each feature
    AirlineName = st.slider("Airline Name", 0, 5, 3)
    CabinType = st.slider("Cabin Type", 0, 5, 3)
    EntertainmentRating = st.slider("Entertainment Rating", 0, 5, 3)
    FoodRating = st.slider("Food Rating", 0, 5, 3)
    GroundServiceRating = st.slider("Ground Service Rating", 0, 5, 3)
    OriginCountry = st.number_input("Origin Country", 1, 31, 15)
    OverallScore = st.slider("Overall Score", 0, 10, 5)
    SeatComfortRating = st.slider("Seat Comfort Rating", 0, 5, 3)
    ServiceRating = st.slider("Service Rating", 0, 5, 3)
    ValueRating = st.slider("Value Rating", 0, 5, 3)
    WifiRating = st.slider("Wifi Rating", 0, 5, 3)
    Day = st.number_input("Day", 1, 31, 15)
    Month = st.number_input("Month", 1, 12, 6)
    Year = st.number_input("Year", 2000, 2030, 2022)

    # Button to make prediction
    if st.button("Predict"):
        features = {
            "AirlineName": AirlineName,
            "CabinType": CabinType,
            "EntertainmentRating": EntertainmentRating,
            "FoodRating": FoodRating,
            "GroundServiceRating": GroundServiceRating,
            "OriginCountry": OriginCountry,
            "OverallScore": OverallScore,
            "SeatComfortRating": SeatComfortRating,
            "ServiceRating": ServiceRating,
            "ValueRating": ValueRating,
            "WifiRating": WifiRating,
            "Day": Day,
            "Month": Month,
            "Year": Year,
        }

        print(features)

        # Run the prediction
        result = model.run(features)

        # Display the result
        st.write("Recommended: Yes" if result == 1 else "Recommended: No")


if __name__ == "__main__":
    fire.Fire(main)
