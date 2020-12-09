import seaborn as sns
import pandas as pd
import numpy as np
import math

# diamonds_url = "https://raw.githubusercontent.com/TrainingByPackt/Interactive-Data-Visualization-with-Python/master/datasets/diamonds.csv"
#
# diamonds_df = pd.read_csv(diamonds_url)

# diamonds_df = sns.load_dataset('diamonds')
#
# diamonds_df['price_per_carat'] = diamonds_df['price']/diamonds_df['carat']
#
# diamonds_df['price_per_carat_is_high'] = np.where(diamonds_df['price_per_carat'] > 3500,1,0)
#
# diamonds_df['price'] = diamonds_df['price'] * 1.3
#
# diamonds_df['rounded_price'] = diamonds_df['price'].apply(math.ceil)
#
# diamonds_df['rounded_price_to_100multiple'] = diamonds_df['price'].apply(lambda x: math.ceil(x/100)*100)
#
# diamonds_df_exercise = sns.load_dataset('diamonds')
#
# def is_desired(x):
#     bool_var = 'yes' if (x['cut'] == 'Ideal' and x['color'] == 'D') else 'no'
#
#     return bool_var
#
# diamonds_df_exercise['desired'] = diamonds_df_exercise.apply(is_desired, axis=1)
#
# print(diamonds_df_exercise.head())

diamonds_df = sns.load_dataset('diamonds')

diamonds_df.hist(column='carat')