# Wallapop-bumper
This script automatically edits all your posted wallapop products so that they don't expire. It works better when instantiated via `cronjob`.
The credentials of the user have to be replaced in `constants.py`. They can be obtained by inspecting HTTP requests sent while using the Wallapop website.

For obtaining your `USER_ID`, visit your profile and inspect the response of the `me` HTTP request:
![](https://i.imgur.com/C0GBaiX.png)

For obtaining the `Authorization` and `User-agent` information, perform an operation in Wallapop while logged into your account (e.g. edit an article):
![](https://i.imgur.com/p3ePXYt.png)
