import flask_cors
import flask
from PIL import Image
import src.ImagenBase64 as ImagenBase64

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route('/color_image', methods=['GET'])
def get_color():
    '''
    AQUI CODIGO DE OBTENER IMAGEN COLOR
    '''
    image_path = 'photo/lena.jpg'
    depth = Image.open(image_path)
    
    return ImagenBase64.get_image(depth)


@app.route('/depth_image', methods=['GET'])
def get_depth():
    '''
    AQUI CODIGO DE OBTENER IMAGEN DEPTH
    '''
    image_path = 'photo/lena.jpg'
    depth = Image.open(image_path)
    
    return ImagenBase64.get_image(depth)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)