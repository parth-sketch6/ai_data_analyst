from data_loader import load_data
from data_profiler import profile_data


df = load_data("data/sales_test_dataset.csv")

profile = profile_data(df)

print(profile)