import pandas as pd 
import numpy as np 

voter_data = pd.read_csv(r"C:\Users\graha\Desktop\python_homework\PyPoll\election_data.csv")

#voter_data.drop_duplicates(inplace=True)

#get list out of column "Candidate" in .csv
candidates = voter_data.loc[:,'Candidate'].values

#get number of votes for total votes and percent votes
#total_values = len(candidates)

#get the unique candidates from the above list
unique_can = np.unique(candidates)

#create new df to store unique candidates in one column, their count of votes in second, and percent of total in third
can_df = pd.DataFrame(unique_can, columns=['Candidate'])

#create second and third column filled with 0's to change to calculated values later
can_df['Vote Count'] = 0 
can_df['Percent Vote'] = 0

#loop through unique candidates
#get count of times that unique candidate name is in "Candidate" column of total voting data set
#fill that count value into above created data frame in "Vote Count" column
for i in unique_can:
    can_df.loc[can_df['Candidate']==i,'Vote Count'] = voter_data.loc[voter_data['Candidate']==i,'Candidate'].count()


#get count of total votes for percent vote calc
total_votes = np.sum(can_df.loc[:,'Vote Count'].values)

#print statement to make sure the count of votes in main dataframe 
# is equal to the count votes in the can_df dataframe
#print(total_votes == total_values)


#loop through unique candidates and get their percent_count
#fill into smaller dataframe for tracking percent and count of votes per candidate

for i in unique_can:
    person_count = can_df.loc[can_df['Candidate']==i, 'Vote Count']
    can_df.loc[can_df['Candidate']==i, 'Percent Vote'] = person_count / total_votes


#make sure can_df is looking the way we expected it to 
#print(can_df)

#get index of larget value within array returned from df[''].values 
winner_index = np.argmax(can_df['Vote Count'].values)

#print to terminal 
print('\n\nElection Results')
print('-'*35)
print('Total Votes: {}'.format(total_votes))
print('-'*35)
for i in unique_can:
    percent_vote = np.round((can_df.loc[can_df['Candidate']==i, 'Percent Vote'].values)*100,2)
    vote_count = can_df.loc[can_df['Candidate']==i, 'Vote Count'].values
    print('{}: {}% ({})'.format(i, *percent_vote, *vote_count))# '*' unpacks the value, would display with [] around number without
print('-'*35)
print('Winner: {}'.format(unique_can[winner_index]))
print('-'*35+'\n\n')


#print same terminal output to .txt file
with open(r"C:\Users\graha\Desktop\python_homework\PyPoll\pypoll_output.txt",'w') as file:
    lines = ['Election Results\n','-'*35+'\n','Total Votes: {}\n'.format(total_votes),
             '-'*35+'\n']
    file.writelines(lines)
    for i in unique_can:
        percent_vote = np.round((can_df.loc[can_df['Candidate']==i, 'Percent Vote'].values)*100,2)
        vote_count = can_df.loc[can_df['Candidate']==i, 'Vote Count'].values
        file.writelines('{}: {}% ({})\n'.format(i, *percent_vote, *vote_count))
    lines2 = ['-'*35+'\n', 'Winner: {}\n'.format(unique_can[winner_index]),'-'*35+'\n']
    file.writelines(lines2)
