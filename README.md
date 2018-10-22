# DeLight
#### Host your blog on your machine with ZERO coding

## Dependency
For now, the code is entirely written using Django python framework (version 2.1).
May switch to a production server in the future.

Notice: For now, due to file path problem, may not work on windows laptop. This can be overcome later in the development. Windows users can also try using Ubuntu subsystem for windows in the windows store as a temporary solution.

## Usage
To create, make changes to your blog, simply log in as a superuser. No need to code!

#### You are 3 STEPS away from running your own web server
1. Clone the repository
```
git clone https://github.com/liangw6/DeLight.git
```
2. Go the directory that has manage.py
```
cd ./DeLight/DeLight/
```
3. Launch the server!
```
python3 manage.py runserver
```
4. Your website will be at
```
http://127.0.0.1:8000/
```

##### To show off your website with the rest of the world
1. Launch your server to everyone
```
python3 manage.py runserver 0:8080
```
Feel free to change 8000 to any other numbers

2. Find your IP address (use another terminal)
```
hostname -I
```
3. Your website will be at
```
http://[IP Address]:8000
```

##### Make it YOUR website
1. Log into admin site
```
http//[website address]/admin
```
with
```
username: admin
password: admin
```
2. CHANGE YOUR ADMIN PASSWORD!!!!

  You can see "change password" on the upper right corner of the admin page

3. Add/Modify/Delete new blogs by making changes to IndexCard


## Current Status and Limitations
Unfortunately, this repository is still under construction. Only the follwing features are available:

  1. blogs

We expect more features to be developed

## Copyright
Arthur Liang @2018
