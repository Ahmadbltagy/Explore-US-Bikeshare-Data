import time
import pandas as pd
import numpy as np

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n').title()
        if city not in ('Chicago', 'New York City', 'Washington'):
            print('Wrong input, Try again. ')
            continue
        else:
            break
        print('Looks like you want to hear about {}! If this not true, restart the program now!\n'.format(city))
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month - January, February, March, April, May, or June? Please Type out the full month name.\n').title()
        if month not in ('January', 'February', 'March', 'April', 'May', 'June'):
            print('Wrong input, Try again. ')
            continue
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()
        if day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
            print('Wrong input, Try again. ')
            continue
        else:
            break
    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour
     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month",popular_month)
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most common day of week",popular_day)
    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("Most common start hour: ", popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most start station",popular_start_station)
    # display most commonly used end station
    print("Most end station",df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print("frequent combination of start station and end station trip",np.max(df.groupby(['Start Station', 'End Station']).count()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total time: ",df['Trip Duration'].sum())

    # display mean travel time
    print("Average of travel time: ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types: ",df['User Type'].value_counts())


    # Display counts of gender
    print("Counts of gender: ",df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    print("Earliest year of birth",np.min(df['Birth Year']))
    print("Most recent year of birth",np.max(df['Birth Year']))
    print("Earliest year of birth",df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        #Display raw data
        x = 0
        while True:
            raw = input("Would you like to see raw data?Type 'yes' or 'No'. ")
            if raw.lower() == 'yes':
                print(df[x:x+5])
                x = x+5
            elif raw.lower() == 'no':
                break
            else:
                print("Worng input, Try Again")
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
	main()
