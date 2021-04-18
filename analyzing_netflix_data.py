import pandas as pd
#import matplotlib

print("")
df = pd.read_csv("/Users/nikolaborska/PYTHON_projects/Analyzing_my_NETFLIX_data/netflix-report/CONTENT_INTERACTION"
                 "/ViewingActivity.csv")
print("Counting the rows:", df.shape)
print("")
print(df.head(5))

#======================================================
# Vyřazení zbytečných sloupců
df = df.drop(["Profile Name", "Attributes", "Supplemental Video Type", "Device Type", "Bookmark", "Latest Bookmark", "Country"], axis=1)
print("rehearsal:")
print(df)

#======================================================
# Převod řetězců na Datetime a Timedelta
print("Data types:")
print(df.dtypes)
print("")
df["Start Time"] = pd.to_datetime(df["Start Time"], utc=True)
df = df.set_index("Start Time")
df.index = df.index.tz_convert("Europe/Prague")
df = df.reset_index()
print("")
df["Duration"] = pd.to_timedelta(df["Duration"])
print("Data types after reformating:")
print(df)

#======================================================
# Filtrování podle podřetězce
ozark = df[df["Title"].str.contains("Ozark", regex=False)]
print("Counting the rows of Ozark:", ozark.shape)
moneyheist = df[df["Title"].str.contains("Money Heist", regex=False)]
print("Counting the rows of Money Heist:", moneyheist.shape)
orange_is_the_new_black = df[df["Title"].str.contains("Orange Is the New Black", regex=False)]
print("Counting the rows of Orange is the new black:", orange_is_the_new_black.shape)
lucifer = df[df["Title"].str.contains("Lucifer", regex=False)]
print("Counting the rows of Lucifer:", lucifer.shape)
friends = df[df["Title"].str.contains("Friends", regex=False)]
print("Counting the rows of Friends:", friends.shape)

#======================================================
# Filtrování krátkých trvání
print("")
ozark = ozark[(ozark["Duration"] > "0 days 00:01:00")]
print("Short Durations of Ozark:", ozark.shape)
moneyheist = moneyheist[(moneyheist["Duration"] > "0 days 00:01:00")]
print("Short Durations of Money Heist:", moneyheist.shape)
orange_is_the_new_black = orange_is_the_new_black[(orange_is_the_new_black["Duration"] > "0 days 00:01:00")]
print("Short Durations of Orange is the New Black:", orange_is_the_new_black.shape)
lucifer = lucifer[(lucifer["Duration"] > "0 days 00:01:00")]
print("Short Durations of Lucifer:", lucifer.shape)
friends = friends[(friends['Duration'] > "0 days 00:01:00")]
print("Short Durations of Friends:", friends.shape)
print("")

#======================================================
# Kolik času jsem ztrávila sledováním těchto seriálů:
print("How much time have I spent watching TV shows?")
print("Ozark:", ozark["Duration"].sum())
print("Money Heist:", moneyheist["Duration"].sum())
print("Orange is the New Black:", orange_is_the_new_black["Duration"].sum())
print("Lucifer:", lucifer["Duration"].sum())
print("Friends:", friends["Duration"].sum())

#======================================================
# Kdy se dívám na seriály?
print("")
print("Ozark:")
ozark["weekday"] = ozark["Start Time"].dt.weekday
ozark['hour'] = ozark['Start Time'].dt.hour
print(ozark)
print("")

print("Money Heist:")
moneyheist["weekday"] = moneyheist["Start Time"].dt.weekday
moneyheist['hour'] = moneyheist['Start Time'].dt.hour
print(moneyheist)
print("")

print("Orange is the New Black:")
orange_is_the_new_black["weekday"] = orange_is_the_new_black["Start Time"].dt.weekday
orange_is_the_new_black['hour'] = orange_is_the_new_black['Start Time'].dt.hour
print(orange_is_the_new_black)
print("")

print("Lucifer:")
lucifer["weekday"] = lucifer["Start Time"].dt.weekday
lucifer['hour'] = lucifer['Start Time'].dt.hour
print(lucifer)
print("")

print("Friends:")
friends["weekday"] = friends["Start Time"].dt.weekday
friends['hour'] = friends['Start Time'].dt.hour
print(friends)
print("")

#======================================================
# Graf podle dni v týdnu:

#ozark["weekday"] = pd.Categorical(ozark["weekday"], categories = [0,1,2,3,4,5,6],ordered=True)
#ozark_day = ozark["weekday"].value_counts()
#ozark_day = ozark_day.sort_index()
#matplotlib.rcParams.update({"font.size": 22})
#ozark_day.plot(kind = "bar", figsize = (20,10), title = "Ozark Episodes Watched by Day")














