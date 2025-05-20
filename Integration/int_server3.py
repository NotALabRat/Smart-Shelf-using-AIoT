from flask import Flask, request
import os

app = Flask(__name__)

#-------------------------------------------------------------------------
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/uploads', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        image_data = request.data
        if image_data:
            filename = "image.jpg" #or create a unique filename.
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            with open(filepath, 'wb') as f:
                f.write(image_data)
            
            return 'Image uploaded successfully!', 200
        else:
            return 'No image data received.', 400

#------------------------------------------------------------------------



if __name__ == '__main__':
    print(os.getcwd())
    app.run(host='0.0.0.0', port=5000, debug=True)




#--------------------------------------------------------------------------
