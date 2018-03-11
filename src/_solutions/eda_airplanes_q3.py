# EDA: Airplanes - Q3

fig, ax = plt.subplots(2,1, figsize=(16,12))

df_airpl.columns
(df_airpl.groupby('Aircraft Series')['High Explosives Weight (Tons)'].
 max().
 dropna().
 sort_values(ascending=False).
 plot.bar(ax=ax[0]))
ax[0].set_title("Aircrafs carring the heaviest explosives weights")

# compute most devastating aircrafts
list_ten_dangerous = (df_airpl.groupby('Aircraft Series')['High Explosives Weight (Tons)'].
                      max().sort_values(ascending=False).
                      dropna()[:10].index)
ten_dangerous = df_airpl.loc[df_airpl["Aircraft Series"].isin(list_ten_dangerous)]

sns.boxplot(x="Aircraft Series", y="High Explosives Weight (Tons)", data=ten_dangerous, ax=ax[1]);
plt.tight_layout()