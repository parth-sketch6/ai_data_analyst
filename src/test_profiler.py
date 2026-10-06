from data_loader import load_data
from data_profiler import profile_data


df = load_data("data/students.csv")

profile = profile_data(df)

print(profile)