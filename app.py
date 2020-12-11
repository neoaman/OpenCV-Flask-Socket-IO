from flask import Flask, render_template, Response, request, jsonify
from flask_socketio import SocketIO
import logging
from sys import stdout
from camera import VideoCamera

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(stdout))
app.config['DEBUG'] = True
socketio = SocketIO(app)
Cam = VideoCamera()

@socketio.on('input image', namespace='/test')
def test_message(input):
    input = input.split(",")[1]
    Cam.enqueue_input(input)
    #camera.enqueue_input(base64_to_pil_image(input))


@socketio.on('connect', namespace='/test')
def test_connect():
    app.logger.info("client connected")



@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(Camera,no):
    while True:
        frame = Camera.get_frame()[no]

        yield (b"--frame\r\n"
            b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    frame = gen(Cam,0) 

    return Response(frame, mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed2')
def video_feed2():
    """Video streaming route. Put this in the src attribute of an img tag."""
    frame = gen(Cam,1) 

    return Response(frame, mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == '__main__':
    socketio.run(app)