Live Cricket Score & Prediction Dashboard

This is a Streamlit-based web app that fetches live cricket match data from the [CricAPI](https://www.cricapi.com/) and predicts top-performing players based on basic statistics. It also allows users to enter custom player stats to estimate their potential performance.

1.Features

- Live Matches: View currently ongoing cricket matches with basic details like venue, status, teams, and score.
- Top 11 Predictor: Predicts the top 11 players who are likely to perform well in a selected live match.
- Match Details: Shows detailed JSON data of selected live matches.
- Custom Player Prediction: Allows users to input their own player stats and receive a potential performance score.

2.Project Structure

├── main.py                        # Streamlit app with UI and routing
├── cricket_api.py                # Module to fetch live match data from CricAPI
├── cricket_prediction_engine.py  # Module containing simple player prediction logic

3.Requirements
Make sure you have the following installed:

->Python(Python 3.7 or higher)
->Python Libraries
    You can install the required libraries using pip:
    ```
     pip install -r requirements.txt
    ```

     Or manually install the essentials:
    ```
    pip install streamlit requests
    ````
->Internet Access
->Required to fetch live data from [CricAPI](https://www.cricapi.com/)
   * Sign up at [https://www.cricapi.com/](https://www.cricapi.com/) to get your free API key.
->Ensure that the API key is valid and you are not exceeding the request limits
->streamlit
->requests

4. Run the App

```bash
streamlit run main.py
```
5.Limitations

* The prediction logic in this version is mocked/dummy and for demonstration purposes only.
* For real predictive analytics, consider integrating historical datasets and machine learning models.

6.Contact
For questions, suggestions, or collaborations, feel free to reach out:
Email: hiranmaye128@gmail.com
GitHub: Hiranmayee-ABSN
