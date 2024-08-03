import base64


def image_to_base64(image_field):
    with image_field.open("rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
