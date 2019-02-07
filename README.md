# Typhon, a followers scraper

A common problem when you are on Twitter is that you can very easily be targeted by malicious people. If an important user retweets, shares a screenshot of one of your Tweet, or just replies to you, you can be a target for harassment. It is very complicated to get ride of that.

Also, there are some communities that you may not want to see, for various reasons (prevent bullying for exemple).

A simple way to solve those problem is to block followers of some users, but this process is time consuming.

## Installation

Firstly, install [Python 3](https://python.org). After that, just download or clone this repositoy, and install the only direct dependency, [Twint](https://github.com/twintproject/twint). To do so, run

```
pip3 install twint
```

or, inside a shell or bash inside the Typhon folder's

```
pip install -r requirements.txt
```

On Windows, shift and right-click on nothing, an select Powershell to directly open a shell inside the folder.

## Usage

Write the list of users inside the file users.txt, one by line and without any space, like that:

> Twitter
> 
> TwitterLive
> 
> verified

Run the following command inside a shell

```
py typhon.py
```

According to the users that you have choosen, it may take a while. Indeed, the program does not use the Official Twitter API. However, you can do whatever you want during that time. Even if the connection is lost, you computer crash or I don't know, the progress will be saved. Just **don't forget to remove the users that already have been processed**.



Once it is done, you can import the list of users on Twitter, right [here](https://twitter.com/settings/blocked), to block them all. Unfortunately, you have to select each file one by one. It will take a while to update your database.



## Configuration

The only configuration available is the ability to choose the approximate size of the files at the end. I personnaly recommend 48000 octets. Note that the maximum for Twitter is 50000 octets.
