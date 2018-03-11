# EDA: Target - Q3

df_daily_index=pd.date_range(start=df_cities["Mission Date"].min(), end=df_cities["Mission Date"].max(), freq="d")
df_cities.set_index("Mission Date", inplace=True)

fig, ax = plt.subplots(15,1,sharey=True, figsize=(10,32)) 
for e, city in enumerate(list_most_frequent_cities):
    s = df_cities.loc[df_cities["Target City"]==city, "High Explosives Weight (Tons)"].resample("d").sum()
    s = s.reindex(df_daily_index)
    s.cumsum().plot(ax=ax[e])
    ax[e].set_title(city.capitalize())
plt.tight_layout()
plt.suptitle("Accumulated high explosives weight (in Tons) due to arial attacks\nfor the 15 most frequent targeted cities in Germany", size=18)
plt.subplots_adjust(top=0.95)