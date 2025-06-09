# cricket_prediction_engine.py


class CricketPredictionEngine:

    def predict_top_players(self, match_data):
        # Dummy top 11 players prediction
        return [f"Player {i+1}" for i in range(11)]

    def predict_custom_player(self, player_data):
        # Simple scoring logic for mock prediction
        score = (player_data["runs"] * 0.05 + player_data["wickets"] * 5 +
                 (50 - player_data["age"]) * 0.3)
        return {
            "Player":
            player_data["name"],
            "Potential Score":
            round(score, 2),
            "Recommendation":
            "High Potential" if score > 50 else "Moderate Potential"
        }
