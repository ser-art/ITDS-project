import streamlit as st
import fire

from src import model
from src import mapping


def main():
    # Streamlit interface
    st.title("Airline Satisfaction Prediction")

    # Create inputs for each feature
    AirlineName = st.selectbox("Airline Name", mapping.airline.keys())
    AirlineName = mapping.airline[AirlineName]

    CabinType = st.selectbox("Cabin Type", mapping.cabin_type.keys())
    CabinType = mapping.cabin_type[CabinType]

    EntertainmentRating = st.slider("Entertainment Rating", 0, 5, 3)
    FoodRating = st.slider("Food Rating", 0, 5, 3)
    GroundServiceRating = st.slider("Ground Service Rating", 0, 5, 3)

    OriginCountry = st.selectbox("Origin Country", mapping.country.keys())
    OriginCountry = mapping.country[OriginCountry]

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
