# EDA: Target - Q2

list_most_frequent_cities = most_frequent_cities.index
df_cities = df_tar.loc[df_tar["Target City"].isin(list_most_frequent_cities)]
print("Summed high explosives (in tons) per city:\n", 
      df_cities.groupby("Target City")["High Explosives Weight (Tons)"].sum().sort_values(ascending=False))
# plot
df_cities.groupby("Target City")["High Explosives Weight (Tons)"].sum().sort_values(ascending=False).plot.bar()
plt.ylabel("High Explosives in tons", size=12);