from flask import request,jsonify
import face_recognition
from app.main import bp

@bp.route('/validate-faces',methods=["POST"])
def index():
    """
    get to images an compare if the have identical faces

    @param k_image , unk_image
    @return bool
    """
    if request.method == 'POST':

        file_list = list(request.files.keys())

        print(file_list)

        if ('k_image' not in file_list )and ('unk_image' not in file_list):
            return jsonify({'error':'require both unknown_image and known_image check entry and try again'}),406
        
        try:
            k_image = request.files['k_image']
            unk_image = request.files['unk_image']
            
            known_image = face_recognition.load_image_file(k_image)
            known_encoding = face_recognition.face_encodings(known_image)[0]

            unknown_image = face_recognition.load_image_file(unk_image)
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

            result = face_recognition.compare_faces([known_encoding],unknown_encoding)
            
            return jsonify({'result':str(result[0])})
        except Exception:
            return jsonify({'error':'something went wrong try again'}), 400

    return jsonify({'error':"accept only post request"}), 406

@bp.route('/welcome')
def home():
    return jsonify({'message':"welcome to face recognition api"})

