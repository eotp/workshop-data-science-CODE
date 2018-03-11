# EDA: Airplanes - Q2

fig, ax = plt.subplots(3,1, figsize=(16,18))
# get operating height
print("Operating height for each aircraft:\n",df_airpl.groupby("Aircraft Series")["Altitude (meters)"].agg(["mean", "min", "max"]).dropna())
df_airpl.groupby("Aircraft Series")["Altitude (meters)"].mean().dropna().sort_values(ascending=False).plot.bar(rot=0, ax=ax[0])
plt.ylabel("Mean altitude (meters)");
print("---------------------------------------")
# compute 10 most common airplane types
list_ten_most_common = df_airpl["Aircraft Series"].value_counts()[:10].index
print("10 most common airplane types:\n", list_ten_most_common)

ten_most_common = df_airpl.loc[df_airpl["Aircraft Series"].isin(list_ten_most_common)]
print(ten_most_common.shape)
print("---------------------------------------")
sns.boxplot(x="Aircraft Series", y="Altitude (meters)", data=ten_most_common, ax=ax[1])
sns.violinplot(x="Aircraft Series", y="Altitude (meters)", hue="Country", split=True, data=ten_most_common, ax=ax[2]);