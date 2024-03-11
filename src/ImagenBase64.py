import base64
from io import BytesIO
 
from PIL import Image


def get_image(img):
    output_buffer = BytesIO()
    img.save(output_buffer, format='PNG')
    binary_data = output_buffer.getvalue()
    base64_data = base64.b64encode(binary_data)
    return base64_data


def get_image_from_array(image_array):
    try:
        img = Image.fromarray(image_array)
        img = img.resize((640,480), Image.LANCZOS)
        output_buffer = BytesIO()
        img.save(output_buffer, format='PNG')
        binary_data = output_buffer.getvalue()
        base64_data = base64.b64encode(binary_data)
    
        return base64_data
    except Exception as ex:
        print(image_array)
        print(ex)