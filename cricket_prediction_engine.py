# cricket_prediction_engine.py
class CricketPredictionEngine:

    def predict_top_players(self, match_data):
        # Placeholder logic to simulate top player prediction
        return [f"Player {i+1}" for i in range(11)]

    def predict_custom_player(self, player_data):
        # Basic scoring system based on input stats
        runs_score = player_data["runs"] * 0.05
        wickets_score = player_data["wickets"] * 5
        age_score = (50 - player_data["age"]) * 0.3

        total_score = runs_score + wickets_score + age_score
        result = {
            "Player": player_data["name"],
            "Potential Score": round(total_score, 2),
            "Recommendation": "High Potential" if total_score > 50 else "Moderate Potential"
        }
        return result


