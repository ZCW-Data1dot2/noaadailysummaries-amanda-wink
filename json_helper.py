import os
import json
import pandas as pd



def read_all_json_files(JSON_ROOT):
    df2=pd.DataFrame()
    ind = 0
    for i in range(2):
        file_path = JSON_ROOT + '/daily_summaries_FIP10003_dec_2018_' + str(i) + '.json'
        file_name = 'daily_summaries_FIP10003_dec_2018_' + str(i) + '.json'
        with open(file_path) as f:
            j_file = json.load(f)
            df3 = pd.DataFrame.from_dict(j_file['results'])
            ind += len(df3)
            df3 = pd.concat([df3, pd.Series([file_name]*len(df3), name="file_name")], axis=1)
            df2 = pd.concat([df2, df3], ignore_index=True)
    return df2

