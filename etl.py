import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    
    """ 
        Processes song JSON file to insert data into song and artist tables

        Arguments:
            * cur : creates connection to the Database
            * filepath: path to json file to extract data to be inserting into song and artist tables
        Returns:
            * Song Data inserted into songs table
            * Artist Data inserted into artists table
        """
    # open song file
    df = pd.read_json(filepath, lines = True)

    # insert song record
    song_data = list((df.values[0][7], df.values[0][8], df.values[0][0], df.values[0][9], df.values[0][5]))
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = list((df.values[0][0], df.values[0][4], df.values[0][2], df.values[0][1], df.values[0][3]))
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    
    """ Processes log JSON file to insert data into users and time table

        Arguments:
            * cur : creates connection to the Database
            * filepath: path to json file to extract data to be inserting into users andtime tables
        Returns:
            * User Data inserted into users table
            * Time Data inserted into times table
            * Songplay data inserted into songplay table
        """
    # open log file
    df = pd.read_json(filepath, lines= True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit = 'ms')
    
    # insert time data records
    time_data = list(zip(t.dt.strftime('%Y-%m-%d %I:%M:%S'),t.dt.hour, t.dt.day, t.dt.week, t.dt.month, \
             t.dt.year, t.dt.weekday))
    column_labels = ['start_time', 'Hour', 'Day', 'Week', 'Month', 'Year', 'Weekday']
    time_df = pd.DataFrame(time_data, columns = column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']].drop_duplicates()

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        start_time = pd.to_datetime(row.ts, unit = 'ms')
        songplay_data = [start_time, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent]
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    
    """ Connects to database and calls functions to insert all data from JSON files into Database

        Arguments:
            * cur : creates connection to the Database
            * conn:
            * filepath: Paths to log and song data data/song_data and data/log_data
            * func : calls functions process_song_file and process_log_file to extract, transform and load data into appropiate tables
        Returns:
            * Sparkify tables with all data inserted into respected tables
        """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    
    """ Connects to database and calls process_data

        Arguments:
            
        Returns:
            * Sparkify tables with all data inserted into respected tables and then closes connection
        """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
