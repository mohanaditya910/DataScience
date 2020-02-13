import pandas as pd

##provide path for the specified files

df=pd.read_csv('Correct_cities.csv')
df_v= pd.read_csv('Misspelt_cities.csv')




# A Dynamic Programming based Python program for edit 
# distance problem 
def editDistDP(str1, str2, m, n): 
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m + 1): 
        for j in range(n + 1): 
  
            # If first string is empty, only option is to 
            # insert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    return dp[m][n] 


###get the query
#choose among these numbers
query_number=int(input('enter the value you want to check({})'.format(len(df_v))))
query=df_v.iloc[query_number]
print(query['misspelt_name'])



city_name_to_match=query['misspelt_name']
length=len(city_name_to_match)
country_to_search= query['country']
print (country_to_search)
##form interest_df
interest_df=df[df.country == country_to_search]



list_of_indices = interest_df.index.values.astype(int)


matched_indices=[]
for i in range(len(list_of_indices)):
  if len(interest_df.iloc[i]['name'])== length:
    matched_indices.append(i)



if len(matched_indices)==0:
  pass ##make it to raise error...since the spelling should match with the length of one of the cities..

###now if len(matched_indices)>1 then you have to perform some other option to find the id...else makethe decision..
if len(matched_indices)==1:
  print(interest_df.iloc[matched_indices[0]]['id'])
   

#complete the pass
else:
  edit_distance,locations=[],[]
  for i in matched_indices:
    print(i)
    str1=city_name_to_match
    str2=interest_df.iloc[i]['name']
    edit_distance.append(editDistDP(str1, str2, len(str1), len(str2)))
    locations.append(i)


print(interest_df.iloc[locations[edit_distance.index(min(edit_distance))]]['id'])
