from flask import Flask, request, render_template, send_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PAIRED_FOLDER = 'paired_files'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PAIRED_FOLDER'] = PAIRED_FOLDER

# Define the file pairs
file_pairs = {
    'Accidentrep.csv': 'masked_Accidentrep.csv',
    'Accused.csv': 'masked_Accused.csv',
    'ArrestPerdet.csv': 'masked_ArrestPerdet.csv',
    'ChargeSheet.csv': 'masked_ChargeSheet.csv',
    'Complainant.csv': 'masked_Complainant.csv',
    'FIR.csv': 'masked_FIR.csv',
    'MOB.csv': 'masked_MOB.csv',
    'RowdySheet.csv': 'masked_RowdySheet.csv',
    'Victim.csv': 'masked_Victim.csv'
    # Add all your file pairs here
}

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if filename in file_pairs:
            paired_filename = file_pairs[filename]
            paired_file_path = os.path.join(app.config['PAIRED_FOLDER'], paired_filename)
            return send_file(paired_file_path, as_attachment=True)
        else:
            return "No paired file found"
    return "File upload failed"

if __name__ == '__main__':
    app.run(debug=True)
