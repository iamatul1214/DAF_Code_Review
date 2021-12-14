import pandas as pd
df=pd.read_excel('Resource.xlsm')
print(df.columns)
properties=df['Properties']
df['Auto code review']=''
for i in range(len(properties)):
    count_round_brackets = 0
    count_square_brackets = 0
    count_round_brackets = count_round_brackets + properties[i].count('(')
    count_round_brackets = count_round_brackets+properties[i].count(')')
    count_square_brackets = count_square_brackets + properties[i].count('[')
    count_square_brackets = count_square_brackets + properties[i].count(']')

    if count_round_brackets % 2 == 0 and count_square_brackets % 2 == 0:
        df['Auto code review'][i] = "pass"
        print(df['Auto code review'])
    else:
        df['Auto code review'][i] = "xpath broken"
        print(df['Auto code review'])


print(df['Auto code review'])
print(df)
# pip
