import os
import pandas as pd

def get_string_dict(dict_, sep=',', d_dot='='):
    return sep.join([f'{key}{d_dot}{value}' for key, value in dict_.items()])

def get_csvs_list_from_dir(dir, endswith='.csv'):
    return [file for file in os.listdir(dir) if file.endswith(endswith)]

def get_df_from_csv_list(csvs_list, dir):
	if isinstance(csvs_list, list):
		df = pd.concat([pd.read_csv(dir+csv) for csv in csvs_list])
	else:
		ValueError('`csvs_list` shut be a list')
	return df