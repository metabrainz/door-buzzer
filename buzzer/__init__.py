from flask import Flask, Blueprint, request, send_from_directory
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
import config
from buzzer import door

bp = Blueprint("door", __name__)

@bp.route("/open", methods=["POST"])
def open_door():

    if not request.remote_addr in config.ALLOWED_IPS:
        raise NotFound

    duration = request.form.get("duration")
    if not duration:
        raise BadRequest("Duration needs to be specified.")
    try:
        duration = int(duration)
    except ValueError:
        raise BadRequest("Incorrect duration format.")

    try:
        door.open_door(duration)
        print("BZZZZZZZZZZ!")
    except door.DoorException as e:
        raise InternalServerError("Failed to open the door: %s" % e)

    return "OK"

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)

    return app
