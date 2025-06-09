# main.py
import streamlit as st
from cricket_api import CricketAPI
from cricket_prediction_engine import CricketPredictionEngine

# Replace this with your CricAPI key
API_KEY = "YOUR_API_KEY_HERE"

# Initialize API and prediction engine
cricket_api = CricketAPI(API_KEY)
prediction_engine = CricketPredictionEngine()

st.set_page_config(page_title="Cricket Dashboard", layout="wide")
st.title("🏏 Live Cricket Score & Player Prediction")

# Sidebar navigation
st.sidebar.title("Navigate")
selected_page = st.sidebar.radio("Select Page", [
    "Live Matches", "Top 11 Predictor", "Match Details", "Custom Player Prediction"
])

@st.cache_data(ttl=60)
def fetch_live_matches():
    return cricket_api.get_live_matches()

def render_live_matches():
    st.header("📺 Ongoing Matches")
    matches = fetch_live_matches()

    if not matches:
        st.info("No live matches available.")
        return

    for match in matches:
        st.subheader(match.get("name", "Unnamed Match"))
        st.markdown(f"**Status:** {match.get('status', 'N/A')}")
        st.markdown(f"**Venue:** {match.get('venue', 'Unknown')}")
        team_info = match.get("teamInfo", [])
        if len(team_info) == 2:
            st.markdown(f"**Teams:** {team_info[0].get('name')} vs {team_info[1].get('name')}")
        else:
            st.markdown("**Teams:** Info not available")

        if 'score' in match:
            st.markdown(f"**Score:** {match['score']}")
        elif 'scorecard' in match:
            st.json(match['scorecard'])
        else:
            st.markdown("**Score:** Not Available")

        with st.expander("Show Full Match JSON"):
            st.json(match)
        st.divider()

def render_top_11():
    st.header("🔮 Predict Top 11 Players")
    matches = fetch_live_matches()

    if not matches:
        st.warning("No match data available for prediction.")
        return

    match_map = {match.get("name", "Unknown Match"): match for match in matches}
    chosen_match = st.selectbox("Choose a Match", list(match_map.keys()))
    match_data = match_map[chosen_match]

    try:
        top_players = prediction_engine.predict_top_players(match_data)
        st.success("Top 11 players predicted:")
        st.write(top_players)
    except Exception as e:
        st.error(f"Prediction Error: {e}")

def render_match_details():
    st.header("📊 Detailed Match Information")
    matches = fetch_live_matches()

    if not matches:
        st.warning("No data to show.")
        return

    match_map = {match.get("name", "Unnamed Match"): match for match in matches}
    selected_match = st.selectbox("Choose a Match", list(match_map.keys()))
    match = match_map[selected_match]

    st.subheader(match.get("name", "Match Details"))
    st.markdown(f"**Status:** {match.get('status', 'N/A')}")
    st.markdown(f"**Venue:** {match.get('venue', 'Unknown')}")
    st.markdown(f"**Format:** {match.get('format', 'Unknown')}")

    if 'teamInfo' in match and len(match['teamInfo']) == 2:
        st.markdown(f"**Teams:** {match['teamInfo'][0].get('name')} vs {match['teamInfo'][1].get('name')}")

    if 'score' in match:
        st.code(match['score'])
    else:
        st.info("Live score not available.")

    with st.expander("Raw JSON Data"):
        st.json(match)

def render_custom_prediction():
    st.header("✍️ Custom Player Potential Calculator")

    with st.form("player_form"):
        name = st.text_input("Player Name")
        age = st.slider("Age", 15, 50, 25)
        matches = st.number_input("Matches Played", min_value=0, value=10)
        runs = st.number_input("Total Runs", min_value=0, value=500)
        wickets = st.number_input("Total Wickets", min_value=0, value=10)
        batting = st.selectbox("Batting Style", ["Right-hand bat", "Left-hand bat"])
        bowling = st.selectbox("Bowling Style", ["Right-arm fast", "Left-arm spin", "None"])
        submit = st.form_submit_button("Predict Potential")

    if submit:
        player_input = {
            "name": name,
            "age": age,
            "matches": matches,
            "runs": runs,
            "wickets": wickets,
            "batting_style": batting,
            "bowling_style": bowling,
        }
        try:
            result = prediction_engine.predict_custom_player(player_input)
            st.success("Prediction Result:")
            st.write(result)
        except Exception as e:
            st.error(f"Error: {e}")

# Routing based on selected page
if selected_page == "Live Matches":
    render_live_matches()
elif selected_page == "Top 11 Predictor":
    render_top_11()
elif selected_page == "Match Details":
    render_match_details()
elif selected_page == "Custom Player Prediction":
    render_custom_prediction()
