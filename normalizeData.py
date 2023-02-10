import json

# Since I am allowed to alter the data, I will normalize the values in order to improve the speed of the quicksort algorithm
def normalize(arr):
    x_min = min(arr)
    x_max = max(arr)
    return [ (x - x_min) / (x_max - x_min) for x in arr ]

# Load the original data
with open('ex2.json', 'r') as f:
    data = json.load(f)

for i in data:
    #normalize the data in each list while perserving the format
    i[:] = normalize(i)
    
# Normalize the data

# Save the normalized data
with open('ex2.5.json', 'w') as f:
    json.dump(data, f)