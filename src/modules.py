"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print("\n".join(sys.argv)) # 03modules.py

# Print out the OS platform you're using:
# YOUR CODE HERE
print(os.name) # nt
print(sys.platform) #win32 

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version_info) #sys.version_info(major=3, minor=8, micro=2, releaselevel='final', serial=0)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid()) #63128

# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd()) #C:\Users\jtrom\OneDrive\Desktop\Projects\Python\Intro-Python-I\src
 
# Print out your machine's login name
# YOUR CODE HERE
print(os.getlogin()) #jtrom
