# ============================================================
# Hypothesis test: do anime movies and series have different
# average ratings?
#   H0: mean(TV rating) == mean(Movie rating)
#   H1: mean(TV rating) != mean(Movie rating)
#   Dataset: Anime Recommendation Database (Kaggle)
# ============================================================

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# ---- 1. Load ----
df = pd.read_csv("anime.csv")

# ---- 2. Explore ----
print(f"{df.head()}\n")
df.info()
print(f"\nShape: {df.shape}")
print(f"\nTypes:\n{df['type'].value_counts()}")
print(f"\nNulls before cleaning:\n{df.isnull().sum()}")

# ---- 3. Clean ----
df = df.dropna(subset=['genre', 'type', 'rating'])
print(f"\nNulls after cleaning:\n{df.isnull().sum()}")

# Keep only the two groups being compared
df = df[df['type'].isin(['TV', 'Movie'])]
rating = df['rating']

# ---- 4. Central tendency ----
print(f"\nMean:   {rating.mean():.2f}")
print(f"Median: {rating.median():.2f}")
print(f"Mode:   {rating.mode()[0]:.2f}")
print("\nBy type:")
print(df.groupby('type')['rating'].agg(['mean', 'median']))

# ---- 5. Dispersion ----
print(f"\nVariance:           {rating.var():.2f}")
print(f"Std deviation:      {rating.std():.2f}")
print(f"Range:              {rating.max() - rating.min():.2f}")
print(f"IQR:                {rating.quantile(0.75) - rating.quantile(0.25):.2f}")
print(f"Coef. of variation: {rating.std() / rating.mean():.2f}")

groups = df.groupby('type')['rating']
print("\nCoef. of variation by type:")
print(groups.std() / groups.mean())

# ---- 6. Visualize ----
sns.histplot(data=df, x='rating')
plt.title("Rating distribution")
plt.show()

sns.boxplot(data=df, x='type', y='rating')
plt.title("Rating by type")
plt.show()

# ---- 7. Check assumptions ----
tv = df[df['type'] == 'TV']['rating']
movie = df[df['type'] == 'Movie']['rating']
print(f"\nShapiro (TV):    {stats.shapiro(tv)}")
print(f"Shapiro (Movie): {stats.shapiro(movie)}")
print(f"Levene:          {stats.levene(tv, movie)}")

# ---- 8. Hypothesis test (Welch's t-test) ----
stat, p = stats.ttest_ind(tv, movie, equal_var=False)
print(f"\nt = {stat:.3f}, p-value = {p:.4g}")

alpha = 0.05
if p < alpha:
    print("Reject H0: there is evidence that the average ratings differ.")
else:
    print("Do not reject H0: no evidence of a difference.")