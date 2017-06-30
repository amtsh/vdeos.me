from flask import Flask
from flask import jsonify

import app.controllers.feed_controller as feedCtrl

flask_app = Flask(__name__)


@flask_app.route('/')
def root():
    return flask_app.send_static_file('index.html')


@flask_app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return flask_app.send_static_file(path)


@flask_app.route('/api/feed/<twitter_username>', methods=['GET'])
def get_videos(twitter_username):
    return jsonify(feedCtrl.get_video_feed(twitter_username))

if __name__ == "__main__":
    flask_app.run(debug=True, use_reloader=True)
