import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = '/mnt/data/comparison_stats.csv'
df = pd.read_csv(file_path)

df['pass_rate_difference'] = df['pass_rate_with_changes'] - df['pass_rate_no_changes']

model_avg_diff = df.groupby('model')['pass_rate_difference'].mean().reset_index()
model_avg_diff.columns = ['Model', 'Average Pass Rate Difference']

language_avg_diff = df.groupby('language')['pass_rate_difference'].mean().reset_index()
language_avg_diff.columns = ['Language', 'Average Pass Rate Difference']

model_avg_rates = df.groupby('model').agg({
    'pass_rate_with_changes': 'mean',
    'pass_rate_no_changes': 'mean'
}).reset_index()
model_avg_rates.columns = ['Model', 'Pass Rate', 'Pass Rate After Removals']

language_avg_rates = df.groupby('language').agg({
    'pass_rate_with_changes': 'mean',
    'pass_rate_no_changes': 'mean'
}).reset_index()
language_avg_rates.columns = ['Language', 'Pass Rate', 'Pass Rate After Removals']


plt.figure(figsize=(10, 6))
sns.barplot(data=model_avg_rates.melt(id_vars='Model', var_name='Condition', value_name='Pass Rate'),
            x='Model', y='Pass Rate', hue='Condition')
plt.title('Model Average Pass Rates')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=language_avg_rates.melt(id_vars='Language', var_name='Condition', value_name='Pass Rate'),
            x='Language', y='Pass Rate', hue='Condition')
plt.title('Language Average Pass Rates')
plt.xticks(rotation=45)
plt.show()

model_styled_table = model_avg_rates.style.background_gradient(cmap="Blues").set_caption("Model Average Pass Rates")
language_styled_table = language_avg_rates.style.background_gradient(cmap="Greens").set_caption("Language Average Pass Rates")

tools.display_dataframe_to_user(name="Model Average Pass Rates Styled", dataframe=model_avg_rates)
tools.display_dataframe_to_user(name="Language Average Pass Rates Styled", dataframe=language_avg_rates)

model_avg_rates_corrected = model_avg_rates.rename(columns={
    'Pass Rate': 'Pass Rate After Removals',
    'Pass Rate After Removals': 'Pass Rate'
})

language_avg_rates_corrected = language_avg_rates.rename(columns={
    'Pass Rate': 'Pass Rate After Removals',
    'Pass Rate After Removals': 'Pass Rate'
})

plt.figure(figsize=(10, 6))
sns.barplot(data=model_avg_rates_corrected.melt(id_vars='Model', var_name='Condition', value_name='Pass Rate'),
            x='Model', y='Pass Rate', hue='Condition')
plt.title('Model Average Pass Rates')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=language_avg_rates_corrected.melt(id_vars='Language', var_name='Condition', value_name='Pass Rate'),
            x='Language', y='Pass Rate', hue='Condition')
plt.title('Language Average Pass Rates')
plt.xticks(rotation=45)
plt.show()
