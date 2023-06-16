from flask import Flask, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configure upload directory
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set allowed file extensions
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx', 'xlsx'}

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file is included in the request
    if 'file' not in request.files:
        return 'No file provided', 400
    
    file = request.files['file']

    # Check if the file has an allowed extension
    if file and allowed_file(file.filename):
        # Secure the filename
        filename = secure_filename(file.filename)
        
        # Save the file to the upload directory
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Return a success message
        return 'File uploaded successfully'

    # If the file is not allowed, return an error message
    return 'File not allowed', 400

if __name__ == '__main__':
    app.run()
