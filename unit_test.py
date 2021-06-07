import pandas as pd

def unit_test(df):
    if not set(['subject_uid','audio_path','audio_type','country','source','pcr_test_result','pcr_test_result_inferred']).issubset(df.columns):
        print("Some columns are missing")
        return False
    string={'positive','negative','recovered','unknown'}
    for s in df['pcr_test_result_inferred']:
        if not set([s]).issubset(string):
            print("Invalid string included")
            return False
    return True
    