import twint
import os


def search_followers(users):
	'''
	Search the followers of the users from the list
	:param users: list of Twitter username (without any spaces)
	'''
	print("Searching followers")
	i = 0
	for name in users:
		print(str(i / len(users) * 100) + "%. " + str(i) + " done, " + str(len(users)) + " remaining.")
		write_csv(name)
		i += 1


def write_csv(username):
	'''
	Search the followers of a single user, and put them into CSV
	:param username: Twitter username (without any spaces)
	'''
	# Configuring Twint
	c = twint.Config()
	c.Username = username
	c.Store_csv = True
	c.Custom["user"] = ["id"]
	c.User_full = True
	c.Hide_output = True
	c.Output = "tmp"

	twint.run.Followers(c)

	print("Scraping for " + username + " done.\nCurrently saving followers.") 
	final = open(name_final_file(), "a")
	for line in open("tmp/users.csv"):
			if line != 'id\n':
				final.write(line)
			if os.stat(final.name).st_size >= sizeFile:
				# Changing of file if the size of the current one is too big
				final.close()
				final = open(name_final_file(), "a")
	os.remove("tmp/users.csv")
	final.close()
	print("Work done for " + username + ".")
	

def name_final_file():
	'''
	Generate the name of one of the final file
	'''
	i = -1
	condition = True
	while condition:
		i += 1
		if os.path.isfile("final" + str(i) + ".csv"):
			if os.stat("final" + str(i) + ".csv").st_size < sizeFile:
				condition = False
		else:
			condition = False
	return "final" + str(i) + ".csv"


# Config
sizeFile = 48000

with open("users.txt") as f:
	users_list = f.read().splitlines()
search_followers(users_list)
os.rmdir("tmp")
