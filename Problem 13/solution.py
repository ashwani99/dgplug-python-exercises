import requests

def is_valid_image(magic_number):
    """byte literal-> bool
    Checks if a file is a valid image file. The byte literal represents the magic number.
    The magic number is checked only for first four bytes.
    """

    MAGIC_NUMBER_PNG = b'\x89\x50\x4E\x47'
    MAGIC_NUMBER_JPG = [b'\xFF\xD8\xFF\xDB', b'\xFF\xD8\xFF\xE0', b'\xFF\xD8\xFF\xE1']
    MAGIC_NUMBER_SVG = b'\x3C\x3F\x78\x6D'

    if magic_number in [MAGIC_NUMBER_PNG, MAGIC_NUMBER_SVG] or magic_number in MAGIC_NUMBER_JPG:
        return True
    else:
        return False


def download_image(url):
    """ str -> None
    Download and save image in the current directory if the image file exists.
    """

    if url.endswith(('.png', '.jpg', '.svg')):
        try:
            response = requests.get(url)
            if is_valid_image(response.content[:4]):
                print('Found image. Downloading...')
                filename = url.split('/')[-1]
                with open(filename, 'wb') as file:
                     file.write(response.content)
                print('{} has been successfully downloaded.'.format(filename))
            else:
                print('Invalid image file.')
        except requests.exceptions.RequestException as e:
            print(e)
    else:
        print('No image found.')


if __name__ == '__main__':
    download_image('https://dgplug.org/assets/img/header.png')
