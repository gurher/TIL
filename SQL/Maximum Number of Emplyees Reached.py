import pandas as pd
import datetime as dt


# Start writing code
uber_employees = [1,2,3,3,5]
uber_employees.head()

uber_employees['name'] =  uber_employees['first_name'] + ' ' + uber_employees['last_name'] 
uber_employees.drop(['first_name','last_name'], axis = 1, inplace = True)



# List all hire_date dates and add a colum with a value 1
hired_dates = pd.DataFrame(uber_employees['hire_date'].rename('date'))
hired_dates['value'] = 1
hired_dates

# List all termination_dates and add a colum with a value 1
termination_dates = pd.DataFrame(uber_employees['termination_date'].rename('date'))
termination_dates['value'] = -1
termination_dates = termination_dates.dropna()

all_dates = pd.concat([hired_dates,termination_dates], ignore_index = True)

# Aggregate the list by date
all_dates = all_dates.groupby('date').sum().reset_index()
all_dates = all_dates.sort_values('date')
all_dates['emp_count'] = all_dates['value'].cumsum()
all_dates


for i in range(uber_employees.shape[0]):
    # For emplyees with no termination_date, add todays date
    if uber_employees.at[i, 'termination_date'] is pd.NaT:
        end_date = dt.datetime.today()
        
    else:
        end_date = uber_employees.at[i, 'termination_date']
        
    start_date = uber_employees.at[i, 'hire_date']
    
    
    # For each emplyee :
    #  -  find the maximum in the cumulative sum between their hire_date and termination_date
    max_emp_count = all_dates[all_dates['date'].between(start_date, end_date)]['emp_count'].max()
    uber_employees.at[i, 'max_emp'] = max_emp_count
    
    
    # - find the earliest date corresponding to this maximum number of emplyees
    earliest_date = all_dates[(all_dates['emp_count'] == max_emp_count) & all_dates['date'].between(start_date, end_date)]['date'].min()
    uber_employees.at[i, 'min_date'] = earliest_date


# Output the emplyees ID, the corresponding highest nunber of employees and the date

result = uber_employees[['id', 'max_emp', 'min_date']]
result

