# EDA: Airplanes - Q1

print("Unique airplanes:\n",df_airpl["Aircraft Series"].unique())
print("---------------------------------------")
print("Most enganged airplanes:\n",df_airpl["Aircraft Series"].value_counts())
print("---------------------------------------")
df_airpl["Aircraft Series"].value_counts().plot.bar(rot=0);