# EDA: Target - Q1

print("Number of unique cities in the data set:\n", df_tar['Target City'].nunique())
print("---------------------------------------")
most_frequent_cities = df_tar['Target City'].value_counts().sort_values(ascending=False)[:15]
print("Most frequent cities:\n", most_frequent_cities)
print("---------------------------------------")