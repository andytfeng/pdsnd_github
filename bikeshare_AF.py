import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   
    # get user input for city (chicago, new york city, washington).
    while True:
          city = input('Please choose a city (Chicago, New York City, or Washington): ')
          city=city.lower()
          
          if city not in ('new york city', 'chicago', 'washington'):
            print('You entered an invalid value. Please re-enter.')
            continue
          else:
            break
        
    # get user input to filter by month.    
    while True:
          month = input('Which month (All, Jan, Feb, Mar, Apr, May, or Jun)? ')
          month = month.lower() 
           
          if month not in ('all', 'jan', 'feb', 'mar', 'apr', 'may', 'jun'):
            print('You entered an invalid value. Please re-enter.')
            continue
          else:
            break
     
    # get user input to filter by day.
    while True:
          day = input('Which day (All, Sun, Mon, Tue, Wed, Thu, Fri, Sat)? ')
          day=day.lower()
          if day not in ('all', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'):
            print('You entered an invalid value. Please re-enter.')
            continue
          else:
            break
    
    return city, month, day

print('Ok, got it. The data you are looking for are as follows: ')


        
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
    df['day_of_week'] = df['Start Time'].dt.day
    df['month'] = df['Start Time'].dt.month  
    
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_popular_month = df['month'].mode()
    print('The most popular month is: ', most_popular_month)

    # display the most common day of week
    most_popular_day_ofaweek = df['day_of_week'].mode()
    print('The most popular day of a week is: ', most_popular_day_ofaweek)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_popular_hour = df['hour'].mode()
    print('The most popular start hour is: ', most_popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mostcommon_startstation = df['Start Station'].mode()
    print('The most common start station is: ', mostcommon_startstation)

    # display most commonly used end station
    mostcommon_endstation = df['End Station'].mode()
    print('The most common end station is: ', mostcommon_endstation)

    # display most frequent combination of start station and end station trip
    combination = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station'])
    print('The most frequent combinbation of start station and end station is: ', combination)
                                                                
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
    total_travel_time = np.sum(df['Travel Time'])
    print('Total travel time: ', total_travel_time)

    # display mean travel time
    mean_travel_time = np.mean(df['Travel Time'])
    print(mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_usertypes = df['User Type'].value_counts()
    print('Counts of usertypes are: ')

    # Display counts of gender
    print('Gender information for these users: ')
    if 'Gender' not in df:
        print('No gender data.')
    else: 
        gender_count = df.groupby('Gender').count()
        print(gender_count)
    
    # Display earliest, most recent, and most common year of birth
    print('Year of Birth information. Earliest, most recent, and most common year: ')
    if 'Birth Year' in df.columns:
        earliest = np.min(df['Birth Year'])
        most_recent = np.max(df['Birth Year'])
        most_common = df['Birth Year'].mode()
    else:
        print('Birth Year does not exisit')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

    
def display_data(df):
    """
    Displays the data used to compute the stats
    Input:
        the dataframe with all the bikeshare data
    Returns: 
       none
    """
    
    df = df.drop(['month', 'day'], axis = 1)
    view_data = input('Would you like to view 5 rows of individual trip data? Please enter Yes or No.').lower()
    start_loc = 0
    
    while True:
        if view_data == 'No':
            return
        elif view_data == 'Yes':
            print(df[start_loc: start_loc + 5])
            start_loc += 0



def main(display_data):
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\n Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main(display_data)
