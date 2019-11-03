# importing pandas as pd
import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({'Weight':[45, 88, 56, 15, 71],
				'Name':['Sam', 'Andrea', 'Alex', 'Robin', 'Kia'],
				'Age':[14, 25, 55, 8, 21]})

# Print the DataFrame
print(df)

#    Weight    Name  Age
# 0      45     Sam   14
# 1      88  Andrea   25
# 2      56    Alex   55
# 3      15   Robin    8
# 4      71     Kia   21

values = df['Name']
print(values[0])
#Sam


def print_row(row):
    print('Weight:', row.loc['Weight'])
    print('Name:', row.loc['Name'])
    print('Age:', row.loc['Age'])


for index, row in df.iterrows():
    print('-----------',index,'-----------')
    print_row(row)