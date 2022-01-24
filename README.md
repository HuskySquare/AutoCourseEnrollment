# AutoCourseEnrollment
A tool for UofT students to enroll in courses without having to wake up early or strange times 

## About this tool
This is a very "rough draft" version of the tool. I never planned on putting this in a public repo because of the potential breach on University guidelines. This repo will most likely be deleted or updated in some way very soon.


## How to use

Go into save_cookie.py and replace username and password with your own acorn username and password (Line 16-17). Before runnning, you should make sure that you have chrome installed and the chromedriver supports your current chrome version. After running this, your login cookie will be saved. 

Then, all you need to is to keep main.py running. Alternatively, you can estimate the amount of time until course enrollment starts and input the following in the terminal(if you're using linux):
 
 ```
 sleep 10s; python3 main.py
 ```
Replace 10s with the number of seconds until course enrollment time starts

Make sure you leave your pc running this program at night before going to sleep. Input the courses you want to enroll in courses.txt, note that this should be the full course code.  Make sure your power settings does not shutdown or sleep the pc before course enrollment time starts.

No support for the specific section yet, the recommendation is that you only use this tool for the courses that you know are going to be full before you wake up.
