import pandas as pd

game_durations = [1234, 5678, 4321, 6789]

df_game_durations = pd.DataFrame(game_durations, columns=["gameDuration"])

df_game_durations.head()