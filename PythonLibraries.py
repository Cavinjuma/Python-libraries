#Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

#1. Create a NumPy array from 1 to 10 and calculate the mean
array = np.arange(1, 11)
mean_value = np.mean(array)
print("1. NumPy Array:", array)
print("Mean of array:", mean_value)

#2. Load a small dataset into a pandas DataFrame and display summary statistics
#Using a sample dictionary to simulate a small dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
print("\n2. DataFrame Summary Statistics:")
print(df.describe())

#3. Fetch data from a public API using requests
#Example: Fetch a random joke from the official joke API
response = requests.get("https://official-joke-api.appspot.com/jokes/random")
if response.status_code == 200:
    joke_data = response.json()
    print("\n3. Random Joke from API:")
    print(f"{joke_data['setup']} - {joke_data['punchline']}")
else:
    print("\n3. Failed to fetch data from the API")

#4. Plot a simple line graph using matplotlib
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
