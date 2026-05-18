# Heart Disease Risk Factor Analysis

## Project Overview
This project analyzes key risk factors associated with heart disease using the 
UCI Cleveland Heart Disease Dataset (n=297). The analysis examines age, sex, 
and chest pain type as predictors of heart disease diagnosis.

## Key Findings
1. **Age**: Patients aged 55+ have nearly double the heart disease rate 
   compared to those under 55 (59.7% vs 30.4%)
2. **Sex**: Male patients show significantly higher disease rates than females 
   (55.7% vs 26.0%), making them 2.1x more likely to be diagnosed
3. **Symptoms**: 72.5% of diagnosed patients reported no chest pain symptoms, 
   highlighting the danger of symptom-based screening alone

## Recommendation
Patients aged 55+, especially males, should be prioritized for routine cardiac 
screening regardless of whether they report chest pain symptoms.

## Tools Used
- Python (pandas, matplotlib)
- Data Source: UCI Machine Learning Repository — Heart Disease Dataset

## Files
- `script.py` — Full analysis code
- `01_age_distribution.png` — Age distribution by diagnosis
- `02_disease_by_sex.png` — Disease rate by sex
- `03_disease_by_cp.png` — Disease rate by chest pain type
