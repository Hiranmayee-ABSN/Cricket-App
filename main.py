import streamlit as st
from cricket_api import CricketAPI
from cricket_prediction_engine import CricketPredictionEngine

# Replace with your actual API key
API_KEY = "YOUR_API_KEY_HERE"

cricket_api = CricketAPI(api_key=API_KEY)
prediction_engine = CricketPredictionEngine()

st.set_page_config(page_title="Live Cricket Dashboard", layout="wide")
st.title("🏏 Live Cricket Score & Prediction Dashboard")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Live Matches", "Top 11 Predictor", "Match Details", "Custom Player Prediction"])

@st.cache_data(ttl=60)
def get_cached_matches():
    return cricket_api.get_live_matches()

def show_live_matches():
    st.header("📺 Live Matches")
    matches = get_cached_matches()
    if not matches:
        st.warning("No live matches at the moment.")
        return
    for match in matches:
        st.subheader(match.get("name", "Unknown Match"))
        st.markdown(f"**Status:** {match.get('status', 'N/A')}")
        st.markdown(f"**Venue:** {match.get('venue', 'N/A')}")
        st.markdown(f"**Teams:** {match.get('teamInfo', [{}])[0].get('name')} vs {match.get('teamInfo', [{}])[1].get('name')}")
        if 'score' in match:
            st.markdown(f"**Score:** {match['score']}")
        elif 'scorecard' in match:
            st.json(match['scorecard'])
        else:
            st.markdown("**Score:** Not available")
        with st.expander("Show Raw Data"):
            st.json(match)
        st.divider()

def show_top11_predictor():
    st.header("🔮 Top 11 Player Predictor")
    matches = get_cached_matches()
    if not matches:
        st.warning("No matches available for prediction.")
        return

    match_dict = {match.get("name", "Unknown"): match for match in matches}
    selected_match_key = st.selectbox("Select a Match", list(match_dict.keys()))
    selected_match = match_dict[selected_match_key]

    try:
        prediction = prediction_engine.predict_top_players(selected_match)
        st.success("Top 11 players predicted successfully!")
        st.write(prediction)
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")

def show_match_details():
    st.header("📊 Match Details")

    matches = get_cached_matches()
    if not matches:
        st.warning("No matches available for detailed view.")
        return

    match_dict = {
        match.get("name", "Unknown"): match for match in matches
    }

    selected_match_key = st.selectbox("Select a Match", list(match_dict.keys()))
    selected_match = match_dict[selected_match_key]

    st.subheader(f"Details for: {selected_match.get('name', 'Unknown Match')}")
    st.markdown(f"**Status:** {selected_match.get('status', 'N/A')}")
    st.markdown(f"**Venue:** {selected_match.get('venue', 'Unknown')}")
    st.markdown(f"**Format:** {selected_match.get('format', 'Unknown')}")
    st.markdown(f"**Teams:** {selected_match.get('teamInfo', [{}])[0].get('name')} vs {selected_match.get('teamInfo', [{}])[1].get('name')}")

    if 'score' in selected_match:
        st.write("**Live Score:**")
        st.code(selected_match['score'])
    else:
        st.info("Live score not available.")

    with st.expander("🔍 Raw Match JSON Data"):
        st.json(selected_match)

def show_custom_prediction():
    st.header("✍️ Custom Player Prediction")

    with st.form("custom_form"):
        name = st.text_input("Player Name")
        age = st.number_input("Age", min_value=15, max_value=50, value=25)
        matches = st.number_input("Matches Played", min_value=0, value=10)
        runs = st.number_input("Total Runs", min_value=0, value=500)
        wickets = st.number_input("Total Wickets", min_value=0, value=10)
        batting_style = st.selectbox("Batting Style", ["Right-hand bat", "Left-hand bat"])
        bowling_style = st.selectbox("Bowling Style", ["Right-arm fast", "Left-arm spin", "None"])
        submit = st.form_submit_button("Predict")

    if submit:
        player_data = {
            "name": name,
            "age": age,
            "matches": matches,
            "runs": runs,
            "wickets": wickets,
            "batting_style": batting_style,
            "bowling_style": bowling_style,
        }
        try:
            prediction = prediction_engine.predict_custom_player(player_data)
            st.success("Prediction Successful!")
            st.write(prediction)
        except Exception as e:
            st.error(f"Failed to predict: {str(e)}")

# Routing
if page == "Live Matches":
    show_live_matches()
elif page == "Top 11 Predictor":
    show_top11_predictor()
elif page == "Match Details":
    show_match_details()
elif page == "Custom Player Prediction":
    show_custom_prediction()
