# -*- coding: utf-8 -*-
"""
Programming Python using an IDE Course at Pluralsight Data Science Demo

"""
#%%
import pandas as pd 
def splitDataFrameList(df,target_column,separator):
    ''' df = dataframe to split,
    target_column = the column containing the values to split
    separator = the symbol used to perform the split
    returns: a dataframe with each entry for the target column separated, with each element moved into a new row. 
    The values in the other columns are duplicated across the newly divided rows.
    '''
    def splitListToRows(row,row_accumulator,target_column,separator):
        split_row = row[target_column].split(separator)
        for s in split_row:
            new_row = row.to_dict()
            new_row[target_column] = s
            row_accumulator.append(new_row)
    new_rows = []
    df.apply(splitListToRows,axis=1,args = (new_rows,target_column,separator))
    new_df = pd.DataFrame(new_rows)
    return new_df
#%%
# Read data from file 'posts-100-header.csv' 
data = pd.read_csv("posts-100-header.csv") 
# Check the top 3 rows 
print(data.head(3))
#%%
# Drop NAs from 2 columns
clean_data = data.dropna(subset=['AnswerCount', 'Score'])
# Split Tags into new rows
tag_separated = splitDataFrameList(clean_data, 'Tags', "><")
# Clean the Tags names removing '<' and '>'
tag_separated['Tags'] = tag_separated['Tags'].map(lambda x: x.lstrip('<').rstrip('>'))
#%%
# May take some time to display
import matplotlib.pyplot as plt
tag_separated.boxplot(by='Tags', column='Score', grid=False, rot=85)
plt.show()
#%%
import matplotlib.pyplot as plt
x = clean_data['AnswerCount']
y = clean_data['Score']

# Plot AnswerCount vs ViewCounts
plt.scatter(x, y)
plt.title('Scatter plot')
plt.xlabel('AnswerCount')
plt.ylabel('Score')
plt.show()

# Plot AnswerCount vs ViewCounts
y = clean_data['ViewCount']
plt.scatter(x, y)
plt.title('Scatter plot')
plt.xlabel('AnswerCount')
plt.ylabel('ViewCount')
plt.show()
