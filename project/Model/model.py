import cv2
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

class ImageProcessor:
    def __init__(self, app):
        self.app = app
        

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def process_image(self, f):
        if f and self.allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(self.app.config['UPLOAD_FOLDER'], filename))
            
            # Đọc ảnh
            img = cv2.imread(os.path.join(self.app.config['UPLOAD_FOLDER'], filename), cv2.IMREAD_GRAYSCALE)

            # Lưu ảnh grayscale với tên mới
            grayscale_filename = "grayscale_" + filename
            cv2.imwrite(os.path.join(self.app.config['UPLOAD_FOLDER'], grayscale_filename), img)

            
            full_og_filename = os.path.join(self.app.static_folder, filename)
            full_gs_filename = os.path.join(self.app.static_folder, grayscale_filename)

            print(full_og_filename)
            print(full_gs_filename,"\n")
            return full_og_filename, full_gs_filename
        return None, None   