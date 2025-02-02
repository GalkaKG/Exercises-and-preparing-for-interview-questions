import numpy as np


# Python function to calculate the moving average of a time series:
def moving_average(series, window_size):
    """
    Calculate the moving average of a time series.

    Parameters:
        series (list or np.array): The input time series data.
        window_size (int): The number of data points to include in the moving average.

    Returns:
        np.array: The moving average values.
    """
    if not series or window_size <= 0:
        raise ValueError("Series must not be empty and window_size must be greater than 0")
    
    return np.convolve(series, np.ones(window_size) / window_size, mode='valid')

# Example usage
time_series = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
window = 3
print(moving_average(time_series, window))   # [20. 30. 40. 50. 60. 70. 80. 90.]
