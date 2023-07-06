import pandas as pd

df = pd.read_csv('users.csv')
print(df.shape)

# new_data = pd.DataFrame({
#                 'userId': 'a1b',
#                 'name': 'TheRock',
#                 'city': 'Los Angeles',
#                 'locations': [[]]
#             })

new_data = pd.DataFrame({
    'userId': ['xyz'],
    'name': ['John'],
    'city': ['London'],
    'locations': ["['0010', '0011', '0012']"]
})

# df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
df = pd.concat([df, new_data], ignore_index=True)
print(df.shape)
