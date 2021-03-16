import time
import pandas as pd
import numpy as np
import datetime
CITY_DATA = { 'chicago': 'chicago.csv',
                  'new york city': 'new_york_city.csv',
                  'washington': 'washington.csv' }
DAYS_WEEK = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
def get_filters():
        """
        Asks user to specify a city, month, and day to analyze.

        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
        print('Hello! Let\'s explore some US bikeshare data!')
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        while(True):
            city = input('Please Enter The City\'s name: (chicago, new york city, washington)\n').lower()
            if(city not in ('chicago', 'new york city', 'washington')):
               print('wrong city please enter one of the items mentioned')
               continue
            else:
               break

        # TO DO: get user input for month (all, january, february, ... , june)
        while(True):
            month = input('Please Enter The Month\'s name: (All,January,February,March,April,May,June)\n').title()
            if(month not in ('All','January','February','March','April','May','June')):
               print('wrong month please enter one of the items mentioned')
               continue
            else:
               break


        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while(True):
            day = input('Please Enter The Day\'s name: (All,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday)\n').title()
            if(day not in ('All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')):
               print('wrong Day please enter one of the items mentioned')
               continue
            else:
               break



        print('-'*60)
        return city, month, day

def load_data(city, month, day):
        """
        Loads data for the specified city and filters by month and day if applicable.

        Args:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        Returns:
            df - Pandas DataFrame containing city data filtered by month and day
        """
      
        df = pd.read_csv(CITY_DATA[city])

        
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        
        df['month'] = df['Start Time'].dt.month
        
        """
        using weekday property of module dt instead of weekday_name as some versions of pandas does not have weekday_name
        so instead  using indexing in list DAYS_WEEK defined above to retrun the name of the day
        """
        df['day_of_week'] = df['Start Time'].dt.weekday

        if month != 'All':
            
            months = ['January','February','March','April','May','June']
            
            month = months.index(month) + 1

            
            df = df[df['month'] == month]
            

        
        if day != 'All':
            
            day = DAYS_WEEK.index(day)  
            
            
            
            df = df[df['day_of_week'] == day]
            
            
            
            
        
        return df

def time_stats(df):
        """Displays statistics on the most frequent times of travel.
           (Pandas.DatFrame) df - The Data Frame to be analyzed
        """

        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # TO DO: display the most common month
        print('Most Common Month: {}'.format(df['month'].mode()[0]))

        # TO DO: display the most common day of week
        print('Most Common day of week: {}'.format( DAYS_WEEK[ df['day_of_week'].mode()[0] ] ) )
        del df['day_of_week']
        # TO DO: display the most common start hour
        """
        after finishing I deleted the Column hour and day_of_week as it is not used any more to reduce the amount of data in memory
        
        """        
        df['hour'] = df['Start Time'].dt.hour
        print('Most Common start hour: {}'.format(df['hour'].mode()[0]))
        del df['hour']
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*60)


def station_stats(df):
        """Displays statistics on the most popular stations and trip.
           (Pandas.DatFrame) df - The Data Frame to be analyzed
        """

        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # TO DO: display most commonly used start station
        print('Most Common Start Station: {}'.format(df['Start Station'].mode()[0]))
        print('-'*40)

        # TO DO: display most commonly used end station
        print('Most Common End Station: {}'.format(df['End Station'].mode()[0]))
        print('-'*100)

        # TO DO: display most frequent combination of start station and end station trip
        """
        adding Combine Column to data consisting of the elements in Starting Stating concatenated with elments in End Station with a format of display
        then displaying this format with the most frequent combination using mode() method and using index 0 to get the specified value 
        after finishing I deleted the Column Combine as it is not used any more
        """
        df['Combine'] = '\nStart Station: '+df['Start Station'] + '\t\tEnd Station: ' +df['End Station']
        print('\t\tmost frequent combination of start station and end station trip\n {}'.format(df['Combine'].mode()[0]))
        del df['Combine']

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*60)


def trip_duration_stats(df):
        """Displays statistics on the total and average trip duration.
           (Pandas.DatFrame) df - The Data Frame to be analyzed
        """

        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # TO DO: display total travel time
        """ 
        using converted datetime object with method timedelta ,assigned to the sum or the mean of Trip Duration column in the data frame, to string                   will return time in dd days , hh:mm:ss hours format
        """
        print( 'Total Travel Time Spent: {} hours'.format( str( datetime.timedelta( seconds=sum(df['Trip Duration']) ) ) ) )
        print('-'*40)
        # TO DO: display mean travel time
        print( 'Average Travel Time Spent: {} hours'.format( str( datetime.timedelta( seconds=df['Trip Duration'].mean() ) ) ) )
        

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*60)


def user_stats(df,city):
        """Displays statistics on bikeshare users.
            (str) city - name of the city to analyze
            (Pandas.DatFrame) df - The Data Frame to be analyzed
        """

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        """
        using counts (list object) of tuples that contains the the total numbers of user type in value_counts() method
        UserType (numpy ndarray) contains the unique elements in column User Type
        UserType (dictionary) contains unique User Type elments as keys and thier counts as tuples of length of 1 as its value
        
        """        
        counts=list(zip(df['User Type'].value_counts()))
        UserType = df['User Type'].unique()
        UserType = dict(zip(UserType,counts))
        del counts
        
        for key,value in UserType.items():
            print('Total Number of {} : {}'.format(key,value[0]))
        
        # TO DO: Display counts of gender
        if(city !='washington'):
            """
            using counts (list object) of tuples that contains the the total numbers of user type in value_counts() method
            Gender (numpy ndarray) contains the unique elements in column Gender
            Gender (dictionary) contains unique Gender elments as keys and thier counts as tuples of length of 1 as its value

            """
            print('-'*40)
            
            counts=list(zip(df['Gender'].value_counts()))
            Gender = df['Gender'].unique()
            Gender = dict(zip(Gender,counts))
            del counts
            for key,value in Gender.items():
                print('Total Number of {} : {}'.format(key,value[0]))
            print('-'*40)
            # TO DO: Display earliest, most recent, and most common year of birth
            print('Earliest Year Of Birth: {}'.format(int(df['Birth Year'].min())))
            print('Most Recent Year Of Birth: {}'.format(int(df['Birth Year'].max())))
            print('Most Common Year Of Birth: {}'.format(int(df['Birth Year'].mode()[0])))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*60)


def main():
        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df,city)
            print('-'*100)
            
            #Display Raw Data
            while(True):
                choice = input('do you want to display 5 rows of the raw data? (yes-no) \n').lower()
                
                if (choice == 'yes'):

                    for i in range(0,len(df),5):
                        for x in range(i,i+5):
                            display = dict(df.iloc[x]) #dictionary contains the column names of the Data Frame as keys and its values as value
                            print()
                            for key,value in display.items():
                                print('{} : {}'.format(key,value))

                            print()
                            print('-'*60)

                        while(True):   
                            choice = input('do you want to display 5 more rows? (yes-no) \n').lower()
                            print('-'*60)

                            if(choice == 'yes'):
                               break
                            elif(choice == 'no'):
                                choice = 'out'
                                break
                            else:
                               print('please enter a correct choice \'yes\' or \'no\'\n\n')
                               continue
                        if(choice == 'out'):
                               break
                           
                    if(choice == 'out'):
                        break
                
                elif(choice == 'no'):
                    break
                else:
                    print('please enter a correct choice \'yes\' or \'no\'\n\n')
                    continue
            
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
        main()
