import pandas as pd


# this function reads the tracks and splits it according to the threshold
# return two dataframes, one containing the pop song, the other without
def get_split_dfs(threshold=90, drop_columns=[]):
    data = pd.read_csv("../dat/tracks.csv")
    pop = data['popularity'] >= threshold
    non_pop = data['popularity'] < threshold
    data = data.drop(columns=['Unnamed: 0'] + drop_columns)
    pop_songs = data[pop]
    non_pop_songs = data[non_pop] 
    return pop_songs, non_pop_songs