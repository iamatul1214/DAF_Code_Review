from Result_Analysis import Result_Analysis

r=Result_Analysis()

data=r.read_Excel()
r.create_Count_Plot(dataframe=data)