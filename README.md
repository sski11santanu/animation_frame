# animation_frame
A simple Python module to run a function repeatedly with a specified time delay before each successive recursion.

# How to use it?
1.) Put the *animation_frame.py* in your project folder, or inside the folder where your other python modules (site-packages) are (you can find it by following the *How to get the location of site-packages* section just below this).

2.) Do either (i)**import animation_frame** or (ii)**from animation_frame import animationFrame**.
3.) Then do any one of the following, according to the option you chose in step 2 (here func is the name of the function on which you want to apply thi feature, and delay is the number of milliseconds after which each succesive recursion of func will be done):
    (i)
        def func(arguments):
            Your code here...
            
            animation_frame.animationFrame(func, delay, arguments)
            
    (ii)
        def func(arguments):
             Your code here...
             
             animationFrame(func, delay, arguments)
             
# How to get the location of site-packages?
1.) Run the Python IDLE, or create a new Python file.
2.) *import sys* **[ENTER]**
3.) *print(sys.path)*
4.) If you created a new file, save it now.
5.) **[ENTER]** if you're using IDLE, or run the saved file.
6.) In the long string of output of comma-separated values you get, check the value (within inverted commas) including *site-packages*.
7.) Copy this path (excluding the inverted commas), replace the double backslashes with single ones, copy this new path and paste in the address bar of the file explorer.
8.) Paste this module in this folder.
