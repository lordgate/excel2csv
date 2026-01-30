import pandas as pd
from datetime import datetime

# Create data for Sheet1
data1 = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob, "The Builder"', 'Charlie\nNewline'],
    'Date': [datetime(2023, 1, 1), datetime(2023, 1, 2), datetime(2023, 1, 3)],
    'Korean': ['안녕하세요', '반갑습니다', '테스트']
}
df1 = pd.DataFrame(data1)

# Create data for Sheet2 (Data)
data2 = {
    'Col A': ['A1', 'A2'],
    'Col B': ['B1', 'B2']
}
df2 = pd.DataFrame(data2)

# Write to Excel
with pd.ExcelWriter('test_data.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Data', index=False)

print("Created test_data.xlsx")
