import pandas as pd
from pathlib import Path
#given to me by AI bc it wasn't working for some reason
folder = Path(__file__).resolve().parent
games = pd.read_csv(folder / "video_games_raw.csv")

print("Video game catalog manager")

row_num = int(input("Enter a row number to view: "))
#locating the row in the DataFrame using iloc
selected_game = games.iloc[row_num]
#now that row is selected, we can print out the information for that game
print("Selected Game:")
print(f"Title: {selected_game['Title']}")
print(f"Platform: {selected_game['Platform']}")
print(f"Genre: {selected_game['Genre']}")
print(f"Rating: {selected_game['Rating']}")
print(f"Current Status: {selected_game['Status']}")

new_status = input("Enter a new status for this game: ")
#we use the .at function to update the status of the selected game in the DataFrame
games.at[row_num, "Status"] = new_status
#set default value for the "Recommended" column to "No"
games["Recommended"] = "No"
#set the condition for it to be recommended, which is a rating of 8 or higher and a price of $40 or less
recommended = (
    (games["Rating"] >= 8) &
    (games["Price"] <= 40)
)
#apply the condition to the "Recommended" column
games.loc[recommended, "Recommended"] = "Yes"

print("\nRecommended Games:")
#use a query to filter the DataFrame for games that are recommended and display the relevant columns
print(
    games.query("Recommended == 'Yes'")[
        ["Title", "Platform", "Price", "Rating"]
    ]
)
#lowkey learned from AI below that index=false is used to prevent the index from being written to the CSV file
#folder also is used to specify the path to save the cleaned CSV file in the same directory as the script
games.to_csv(folder / "video_games_cleaned.csv", index=False)
print("\nThe catalog has been updated.")
print("Saved as video_games_cleaned.csv.")