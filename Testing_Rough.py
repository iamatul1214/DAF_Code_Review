import pandas as pd
from Operations import back_Operations
df=pd.read_excel('Testing files/Resource.xlsm')
print(df.columns)

properties=df['Properties'].tolist()
print(type(properties))
df['Auto code review']=''
df['Review Suggestions']=''
# for i in range(len(properties)):
#     count_round_brackets = 0
#     count_square_brackets = 0
#     count_round_brackets = count_round_brackets + properties[i].count('(')
#     count_round_brackets = count_round_brackets+properties[i].count(')')
#     count_square_brackets = count_square_brackets + properties[i].count('[')
#     count_square_brackets = count_square_brackets + properties[i].count(']')
#
#     if count_round_brackets % 2 == 0 and count_square_brackets % 2 == 0:
#         df['Auto code review'][i] = "pass"
#         print(df['Auto code review'])
#     else:
#         df['Auto code review'][i] = "xpath broken"
#         print(df['Auto code review'])
bo=back_Operations()
for i in range(len(properties)):
   x= bo.round_Brackets_Check(Testable_property=properties[i])
   y= bo.square_Brackets_Check(Testable_property=properties[i])
   z=bo.asterisk_Check(Testable_property=properties[i])
   w=bo.single_Quotes_Check(Testable_property=properties[i])
   t=bo.double_Quotes_Check(Testable_property=properties[i])
   q=bo.single_Slash_Start_Check(Testable_property=properties[i])
   # if x and y and z and w is True:
   #     df['Auto code review'][i] = "pass"
   # else:
   #     df['Auto code review'][i] = "fail"
   # print(df['Auto code review'])
   # if p >3:
   #    df['Auto code review'][i] = "too many slashes used, looks like an absolute xpath"
   review_column_name='Auto code review'
   review_suggestion='Review Suggestions'
   m1,m2=bo.review_Decider(round_bracket_check=x,square_bracket_check=y,single_quotes_check=3,double_quotes_check=t,asterisk_check=z,single_slash_start_check=q)
   bo.review_Writer(m1,m2,df,review_column_name,review_suggestion,i)

print(df['Auto code review'])
print(df['Review Suggestions'])
print(df)
# pip

