from bs4 import BeautifulSoup
import requests
import os

def download_file(url):
    content = requests.get(url).text
    filename = url.split('/')[-1]
    if os.path.isfile(filename):
        return
    with open(filename, 'w') as fileobj:
        fileobj.write(content)

def download_log_files_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    for a_tag in soup.find_all('a'):
        link = str(a_tag.get('href'))
        if link.endswith('.txt'):
            download_file(url + link)


def get_stats():
    # A dictionary to contain nicks and the number of lines and words spoken by them
    nicks = {}

    filenames = os.listdir()
    for filename in filenames:
        if filename.endswith('.txt'):
            with open(filename, 'r') as fileobj:
                log = fileobj.read()
                for line in log.split('\n'):
                    parts = line.split()
                    if len(parts) < 3:
                        continue
                    
                    current_nick = parts[1].strip('<>')
                    words_spoken = parts[2:]

                    if current_nick in nicks:
                        # Update the number of lines spoken by the nick
                        nicks[current_nick][0] = nicks[current_nick][0] + 1
                        # Update the number of words spoken by the nick
                        nicks[current_nick][1] = nicks[current_nick][1] + len(words_spoken)
                    else:
                        # Create a new nick entry
                        nicks[current_nick] = []
                        nicks[current_nick].append(1)
                        nicks[current_nick].append(len(words_spoken))

    print('There were {} different nicks present till now'.format(len(nicks)))
    print('\nDetailed overview:')
    print('------------------')
    for current_nick in nicks:
        print('{} spoke {} lines and {} words.'.format(current_nick, nicks[current_nick][0], nicks[current_nick][1]))


if __name__ == '__main__':
    download_log_files_from_url('https://dgplug.org/irclogs/2017/')
    get_stats()
