if 'timestamp' in df.columns:
    df.set_index('timestamp', inplace=True)

def get_most_frequent(x):
    if len(x) == 0: return None
    return x.mode()[0] 

df_resampled = df.resample('1min').agg({
    'state': get_most_frequent,  
    'acc_magnitude': 'mean'      
}).dropna()

df_resampled = df_resampled.reset_index()

df_resampled['group_id'] = (df_resampled['state'] != df_resampled['state'].shift()).cumsum()

summary_df = df_resampled.groupby('group_id').agg({
    'timestamp': ['min', 'max'],    
    'state': 'first',               
    'acc_magnitude': 'count'        
})

summary_df.columns = ['start_time', 'end_time', 'activity', 'duration_min']

print("시간대별 요약 데이터")
print(summary_df.to_string())
