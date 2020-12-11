# OpenCV-Flask-Socket-IO
Rendering webcam Image through python OPEN-CV (Deployed in heroku)
[Example site](https://neovision.herokuapp.com/)

1 : Raw_image from JS using main.js pushed to socket /test and geathered by app.py file to class `VideoCamera`.   
2 : The raw image (bytes64) in stored in list with name `to_process`.
3 : If `to_process` list is not empty, `process_one` method grab the last raw image string from the list.   
4 : `process_one` method store the output image in `output_image_rgb` list, in this method we perform our preprocessing with the image by converting bytes64 to cv readable array format.   
5 : `get_frame` method get the latest **output_image** from the list. Here we are getting the base64 type image output   
6 : Route '/video_feed' get the image through the generator and response with the bytes64 image.   
7 : In `index.html` ```<img id="imageElement" src="{{ url_for('video_feed') }}" style=" height: 300px;">``` get the image to display.
