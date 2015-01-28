'''If run as a script this will output the stats of the last profile.'''

import os.path
import time
import cProfile
import pstats

SRC_FOLDER = os.path.dirname(os.path.dirname(__file__))
MAIN_FOLDER = os.path.dirname(SRC_FOLDER)
DATA_PATH = os.path.join(MAIN_FOLDER, "data")
#TODO: Put profile file into temporary files location
PROFILE_FILE_PATH = os.path.join(MAIN_FOLDER, "profile", "profile.txt")

def time_functions(*functions, print_out=True, profile=False):
    """Return a list [(function1, output, time taken), ...]
    
    The time taken normally has 16ms of precision.
    Profiling only saves the results of the last function. You can use the
    see_profile function to get the results, or run this file as a script."""
    
    def time_them():
        for function in functions:
            start = time.time()
            output = function()
            time_taken = time.time() - start
            
            time_list.append((function, output, time_taken))
            
            if print_out:
                s = "----------\n"
                s += "{}: {}\n"
                s += "Time: {}ms\n"
                s += "----------\n"
                s = s.format(function.__name__, output, time_taken*1000)
                print(s)
    
    time_list = []
    
    if profile:
        cProfile.runctx('time_them()', globals(), locals(), PROFILE_FILE_PATH)
    else:
        time_them()
    
    return time_list

def see_profile():
    """Output last profile"""
    stats = pstats.Stats(PROFILE_FILE_PATH)
    stats.strip_dirs()
    stats.sort_stats('time')
    stats.print_stats()


if __name__ == "__main__":
    see_profile()
