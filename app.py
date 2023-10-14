import os, json                   # for file handling
from github import Github         # for accessing github data
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
import subprocess
from operator import itemgetter   # for sorting nested list
from flask import Flask, render_template, send_from_directory

# run tailwind build command in background:
if not os.path.isdir("node_modules"):
    print("Installing node_modules...")
    subprocess.run("npm install", shell=True)
    print("node_modules installed successfully!")
tailwind = subprocess.Popen("npm run dev", shell=True)

load_dotenv()
github_token = os.getenv("github_token")


# Initializing the flask app:
app = Flask(__name__)

# Info to edit for 2023:
label_for_hacktober_2023 = "hacktoberfest"
label_accepted_pull = "hacktoberfest-accepted"
# timezone aware datetime object:

event_starting_date = datetime(2022, 10, 1)


levels = {"level-1" : 5, "level-2": 10, "level-3" : 20, "Level-1" : 5, "Level-2": 10, "Level-3" : 20}


# g = Github("github_token")
g = Github(github_token)
org = g.get_organization("GDSC-IIIT-Kalyani")
org.login


hack_repos = []   # This list will contain all the hackable 2022 repos name
# for repo in org.get_repos():
#     labels = repo.get_labels()
#
#     if label_for_hacktober_2022 in [label.name for label in labels]:
#         hack_repos.append(repo)
# hack_repos.append(g.get_repo("GDSC-IIIT-Kalyani/hacktobot"))
# hack_repos.append(g.get_repo("GDSC-IIIT-Kalyani/Doggo-run"))
# hack_repos.append(g.get_repo("GDSC-IIIT-Kalyani/Typing-Speed-Test"))
# hack_repos.append(g.get_repo("GDSC-IIIT-Kalyani/react-star-match"))
# hack_repos.append(g.get_repo("GDSC-IIIT-Kalyani/Plot"))
# hack_repos.append(g.get_repo("GDSC-IIIT-Kalyani/Face-Recognition"))
# hack_repos.append(g.get_repo("GDSC-IIIT-Kalyani/hacktober-leaderboard"))
hack_repos.append(g.get_repo("GDSC-IIIT-Kalyani/Hacktober-Fest-2023"))

def get_leaderboard():
    ranks = []
    done_users = []
    repo = g.get_repo("GDSC-IIIT-Kalyani/Hacktober-Fest-2023")
    pulls = repo.get_pulls(state='closed', sort="created", direction='desc')   # getting all the closed pull requests
    for pr in pulls:
        pr_labels = [label.name for label in pr.labels]
        if pr.created_at > event_starting_date:
            if label_accepted_pull in pr_labels:
                score = 0
                for k, v in levels.items():   # calculating score from the level dictionary
                    if k in pr_labels:
                        score = v
                if score == 0:
                    continue

                # print(pr.user.name, pr.user.login, pr.created_at, pr_labels, score)
                if pr.user.name in done_users:
                    for i in range(len(ranks)):
                        if ranks[i][0] == pr.user.name:
                            ranks[i][1] += (-score)
                            break
                else:
                    # Making a nested list (ranks):
                    # ranks = [['uname', '-score', 'img_url', 'first_pull_req_date&time'], ...] (-score would be taken care of later)
                    ranks.append([pr.user.name, -score, "https://github.com/"+pr.user.login+".png", pr.user.login, pr.created_at])
                    done_users.append(pr.user.name)
        else:
            break

    # Sorting rank according to the score then the date & time of first pull req. per user:
    ranks = sorted(ranks, key=itemgetter(1, 4), reverse=True)
    ranks = ranks[::-1]
    # print(ranks)

    # Populating the final export data with rank detail based on the ranks list:
    rank = 1
    user = {}
    data = {}
    data['records'] = []

    for i in ranks:
        user["rank"] = rank
        user["username"] = i[0]
        user["points"] = -i[1]
        user["profileLink"] = i[2]
        user["full_name"] = i[3]
        user["profilepage"]=i[2][:-4]
        data['records'].append(user)
        user = {}
        rank+=1


    print(data)

    return data

data = get_leaderboard()

# URL routings:
@app.route("/")
def start():
    return render_template("index.html", data=data)


# Main:
if __name__ == '__main__':
    app.run(debug=True, threaded=True)
