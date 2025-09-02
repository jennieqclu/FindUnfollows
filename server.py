from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("unfollowers.html")

@app.route("/upload", methods=["POST"])
def upload():

    followers_file = request.files["followers"]
    followings_file = request.files["followings"]
        
    raw1 = followers_file.read()
    raw2 = followings_file.read()

    text1 = BeautifulSoup(raw1.decode("utf-8", errors="ignore"), features="lxml")
    text2= BeautifulSoup(raw2.decode("utf-8", errors="ignore"), features="lxml")
    
    usernamesFollowers = [a.text.strip() for a in text1.find_all("a")]
    usernamesFollowing = [a.text.strip() for a in text2.find_all("a")]

    unfollowers = sorted(list(set(usernamesFollowing) - set(usernamesFollowers)))

    return jsonify({
        "followers":{
            "preview": '\n'.join(usernamesFollowers)
        },
        "followings": {
            "preview": '\n'.join(usernamesFollowing)
        },
        "unfollowers": {
            "preview": '\n'.join(unfollowers)
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
