import os

import twint


def search_followers(users, config):
    '''
    Search the followers of the users from the list
    :param users: list of Twitter username (without any spaces)
    :param config: dictionary of the configuration
    '''
    print("Searching followers")
    i = 0
    for name in users:
        print(str(round(i / len(users) * 100, 2)) + "%. " + str(i) + " done, " + str(len(users) - i) + " remaining.")
        write_csv(name, config)
        i += 1

    if config["output"] == "singleFile":
        os.rename("tmp/users.csv", "users.csv")
        remove_first_line("users.csv")


def run_twint(username):
    '''
    Run Twint to recover the followers
    :param username: user to recover followers
    :return:
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


def write_csv(username, config):
    '''
    Search the followers of a single user, and put them into CSV
    :param username: Twitter username (without any spaces)
    :param config: dictionary of the configuration
    '''
    run_twint(username)
    out = ""

    print("Scraping for " + username + " done.\nCurrently saving followers.")

    if config["output"] != "singleFile":
        remove_first_line("tmp/users.csv")

    if config["output"] == "folderByUser":
        out = username + "/"
        create_folder(out)

    if config["output"] in ["folderByUser", "severalFiles"]:
        final = open(name_final_file(config, out), "a")
        for line in open("tmp/users.csv"):
            final.write(line)
            if os.stat(final.name).st_size >= config["sizeFile"]:
                # Changing of file if the size of the current one is too big
                final.close()
                final = open(name_final_file(config, out), "a")
        os.remove("tmp/users.csv")
        final.close()
    elif config["output"] == "fileByUser":
        os.rename("tmp/users.csv", username + ".csv")

    if config["removeUser"]:
        remove_first_line('users.txt')

    print("Work done for " + username + ".")


def name_final_file(config, output):
    '''
    Generate the name of one of the final file
    :param config: dictionary of the configuration
    :param output: path to expect output
    :return name of the file to open
    '''
    i = -1
    condition = True
    while condition:
        i += 1
        if os.path.isfile(output + "final" + str(i) + ".csv"):
            if os.stat(output + "final" + str(i) + ".csv").st_size < config["sizeFile"]:
                condition = False
        else:
            condition = False
    return output + "final" + str(i) + ".csv"


def remove_first_line(filename):
    '''
    Remove the first line of a file
    '''
    with open(filename, 'r+') as f:
        f.readline()
        data = f.read()
        f.seek(0)
        f.write(data)
        f.truncate()


def create_folder(path):
    '''
    Create a folder
    :param path: path and name of the new folder
    '''
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))


# Config
configuration = {
    # Approximate size of output files
    "sizeFile": 48000,
    # Remove users that have been checked from list
    "removeUser": True,
    # Way of creating the output
    "output": "severalFiles"
}

with open("users.txt") as f:
    users_list = f.read().splitlines()
search_followers(users_list, configuration)
os.rmdir("tmp")
