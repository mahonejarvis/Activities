# Create a new Python file -- make sure it has a `.py` extension

# Type this code into your Python file, open the terminal, and run the file ...

''' python
import pandas as pd
age = [20, 40, 60]
years = pd.Series(age)
print(years)
'''

import pandas as pd 
age = [20,40,60]
years = pd.Series(age)
print(years)


# you can combine multiple series along a particular axis (column-wise or row-wise)
import pandas as pd

# Create pandas Series
courses = pd.Series(["Spark","PySpark","Hadoop"])
fees = pd.Series([22000,25000,23000])
discount  = pd.Series([1000,2300,1000])

# Combine two Series
df = pd.concat([courses, fees], axis=1)
print("Concat 2 lists ...\n", df)

# Combine multiple Series
df = pd.concat([courses, fees, discount], axis=1)
print("\nConcat 3 lists ...\n", df)


# Create Series by assigning names to each column
import pandas as pd

courses = pd.Series(["Spark","PySpark","Hadoop"], name='courses')
fees = pd.Series([22000,25000,23000], name='fees')
discount  = pd.Series([1000,2300,1000],name='discount')

df = pd.concat([courses,fees,discount],axis=1)
print(df)

# Create Series with assigned indexes and provide custom column names
import pandas as pd

courses = pd.Series(["Spark","PySpark","Hadoop"], name='courses')
fees = pd.Series([22000,25000,23000], name='fees')
discount  = pd.Series([1000,2300,1000],name='discount')

# Assign Index to Series
index_labels=['r1','r2','r3']
courses.index = index_labels
fees.index = index_labels
discount.index = index_labels


# Concat Series by Changing Names
df = pd.concat({'Courses': courses,
                'Course_Fee': fees,
                'Course_Discount': discount},axis=1)
print(df)