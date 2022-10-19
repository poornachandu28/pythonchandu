import pandas as pd

# read by default 1st sheet of an excel file
df = pd.read_excel('python.xlsx')
d = df.sort_values('Years of Experience', ascending=False)


print(d)





###########  output  #######

Name  Years of Experience         Job Title Date of Birth
3   Naresh                    5    Java Developer    1996-12-02
2   lokesh                    4  Python Developer    1998-11-02
0   chandu                    3  Devops Developer    2000-09-28
1   poorna                    2         AWS cloud    2001-01-01

Process finished with exit code 0
