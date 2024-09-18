import pandas as pd
import numpy as np
# Pandas Series - Like a Table Column - 1 Dimensional Array Holding Any Type of Data
my_series = [5,9,12,27]
my_var = pd.Series(my_series)


# Print specific value
my_var[2]

# Labels using the index argument
my_index = ["A", "B", "C", "D"]
my_var2 = pd.Series(my_series, index=my_index)

my_var2["C"]

# Key Value Dictionary
cars = {"Tesla":12, "Mercedes":42, "BMW":3}
my_var3 = pd.Series(cars)

my_var3["Tesla"]

