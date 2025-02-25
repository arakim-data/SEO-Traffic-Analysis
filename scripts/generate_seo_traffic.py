import pandas as pd
import numpy as np
import os 

# generate randome traffic data 

np.random.seed(42)

data = {
    "Session Source": ["Direct", "Organic Search", "Referral", "Email", "Paid Search", "Social"],  
    "Sessions": np.random.randint(5000, 20000, 6), 
    "Engaged Sessions": np.random.randint(1000, 15000, 6),
    "Engagement Rate": np.random.uniform(40, 80, 6).round(2) 
}

df = pd.DataFrame(data) 

# CSV save
output_path = "../data/sameple_seo_traffic_data.csv"
df.to_csv(output_path, index = False)

print(f"sameple SEO traffic data save to {output_path}")