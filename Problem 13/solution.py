import requests

def download_image(url):
    """ str -> None
    Check if the URL points to an image and download it in the current directory.
    """
    if url.endswith('.png') or url.endswith('.jpg') or url.endswith('.svg'):
        print('Found image. Downloading...')
        response = requests.get(url)
        filename = url.split('/')[-1]
        with open(filename, 'wb') as file:
             file.write(response.content)
        print('Image successfully downloaded.')
    else:
        print('No image found.')


if __name__ == '__main__':
    download_image('https://dgplug.org/assets/img/header.png')