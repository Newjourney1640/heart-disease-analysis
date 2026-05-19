import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'

# Define column names manually since raw data file has no headers
cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
        'restecg', 'thalach', 'exang', 'oldpeak',
        'slope', 'ca', 'thal', 'target']

df = pd.read_csv('/Users/congxiao/Desktop/New Journey/heart+disease/processed.cleveland.data',
                  names=cols,
                  na_values='?')  # Treat '?' as missing values

print(df.shape)
print(df.head())

print("=== Missing Values ===")
print(df.isnull().sum())

print("\n=== Basic Statistics ===")
print(df.describe())

# Drop rows with missing values — only 6 rows affected, minimal impact
df = df.dropna()
print("Records after cleaning:", df.shape)

# Convert target into binary: 0 = no heart disease, 1 = heart disease (original values 1-4)
df['target'] = (df['target'] > 0).astype(int)

# Map sex column from numeric to text labels for better readability in charts
df['sex_label'] = df['sex'].map({1: 'Male', 0: 'Female'})

# Verify data after cleaning
print("\nHeart Disease vs Healthy:")
print(df['target'].value_counts())
print("\nMale vs Female:")
print(df['sex_label'].value_counts())

fig, ax = plt.subplots(figsize=(8, 5))

# Plot overlapping histograms to compare age distribution between
# heart disease and healthy groups, alpha=0.6 to show overlap clearly
ax.hist(df[df['target']==0]['age'], bins=15, alpha=0.6,
        color='steelblue', label='No Disease')
ax.hist(df[df['target']==1]['age'], bins=15, alpha=0.6,
        color='tomato', label='Heart Disease')

ax.set_xlabel('Age')
ax.set_ylabel('Number of Patients')
ax.set_title('Age Distribution: Heart Disease vs Healthy')
ax.legend()

plt.tight_layout()
plt.savefig('01_age_distribution.png', dpi=150)
plt.show()

# Split patients by age 55 — identified as a key risk threshold from the histogram
older = df[df['age'] >= 55]
younger = df[df['age'] < 55]

# Calculate heart disease rate for each group and the percentage increase
rate_older = older['target'].mean() * 100
rate_younger = younger['target'].mean() * 100
increase = (rate_older - rate_younger) / rate_younger * 100

print(f"Heart disease rate (55+): {rate_older:.1f}%")
print(f"Heart disease rate (<55): {rate_younger:.1f}%")
print(f"Rate increase: {increase:.0f}%")

fig, ax = plt.subplots(figsize=(7, 5))

# Calculate heart disease rate by sex to compare risk between male and female patients
sex_disease = df.groupby('sex_label')['target'].mean() * 100

bars = ax.bar(sex_disease.index, sex_disease.values,
              color=['salmon', 'steelblue'], width=0.5)

for bar, val in zip(bars, sex_disease.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{val:.1f}%', ha='center', fontsize=12, fontweight='bold')

ax.set_xlabel('Sex')
ax.set_ylabel('Heart Disease Rate (%)')
ax.set_title('Heart Disease Rate by Sex')
ax.set_ylim(0, 70)

plt.tight_layout()
plt.savefig('02_disease_by_sex.png', dpi=150)
plt.show()

fig, ax = plt.subplots(figsize=(8, 5))

# Map numeric chest pain codes to descriptive labels
cp_labels = {1: 'Typical Angina', 2: 'Atypical Angina',
             3: 'Non-anginal Pain', 4: 'Asymptomatic'}
df['cp_label'] = df['cp'].map(cp_labels)

# Calculate disease rate by chest pain type, sorted high to low for clarity
cp_disease = df.groupby('cp_label')['target'].mean() * 100
cp_disease = cp_disease.sort_values(ascending=False)

bars = ax.bar(cp_disease.index, cp_disease.values, color='steelblue', width=0.5)

for bar, val in zip(bars, cp_disease.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{val:.1f}%', ha='center', fontsize=11, fontweight='bold')

ax.set_xlabel('Chest Pain Type')
ax.set_ylabel('Heart Disease Rate (%)')
ax.set_title('Heart Disease Rate by Chest Pain Type')
ax.set_ylim(0, 90)

plt.tight_layout()
plt.savefig('03_disease_by_cp.png', dpi=150)
plt.show()