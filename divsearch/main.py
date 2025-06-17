from .core import ADSRunner

def run_ads(dataframe, target_column):
    ads = ADSRunner(dataframe, target_column)
    result = ads.execute()
    return result
