from argparse import ArgumentParser
from requests import get, HTTPError, ConnectionError
from platform import system as getos
from os import system
from sys import exit
from re import findall
from urllib.parse import unquote
from tqdm import tqdm


def banner():
    if getos().lower()[0] is not "w":
        system("clear")
    else:
        system("cls")
    print("""
                                                              
,------.,-----.      ,------.   ,-----. ,--.   ,--.,--.  ,--. 
|  .---'|  |) /_     |  .-.  \ '  .-.  '|  |   |  ||  ,'.|  | 
|  `--, |  .-.  \    |  |  \  :|  | |  ||  |.'.|  ||  |' '  | 
|  |`   |  '--' /    |  '--'  /'  '-'  '|   ,'.   ||  | `   | 
`--'    `------'     `-------'  `-----' '--'   '--'`--'  `--' 
                   By : GURKIRAT SINGH
            https://tbhaxor.github.com/fbdown    
    """)
    pass


def main(url, path):
    banner()
    print("URL :", url)
    print("Save As :", path)
    link = getdownlink(url)
    download(link, path)
    pass


def download(url, path):
    chunk = 1024  # 1kB
    r = get(url, stream=True)
    total = int(r.headers.get("content-length"))
    print("Video Size : ", round(total / chunk, 2), "KB", end="\n\n")
    with open(path, "wb") as file:
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk), total=total / chunk, unit="KB"):
            file.write(data)
        file.close()

    print("Download Complete !!!")

    pass


def getdownlink(url):
    url = url.replace("www", "mbasic")
    try:
        r = get(url, timeout=5, allow_redirects=True)
        if r.status_code != 200:
            raise HTTPError
        a = findall("/video_redirect/", r.text)
        if len(a) == 0:
            print("[!] Video Not Found...")
            exit(0)
        else:
            return unquote(r.text.split("?src=")[1].split('"')[0])
    except (HTTPError, ConnectionError):
        print("[x] Invalid URL")
        exit(1)
    pass


def defaultOP(url):
    data = url.split("/")
    if data[-1] == "":
        return data[-2] + ".mp4"
    else:
        return data[-1]


def parse():
    global url
    global path
    parser = ArgumentParser(description="FB Down is an open source program to download videos uploaded to facebook")
    parser.add_argument("url", help="Facebook Video URL To Download")
    parser.add_argument("--output", metavar="Optional", nargs="?", type=str, default=None,
                        help="Facebook Video Name to Save As. This is an optional argument")
    args = parser.parse_args()
    url = args.url
    path = defaultOP(url)
    if args.output != None:
        path = args.output
    return url, path


def TheMain():
    args = parse()
    main(args[0], args[1])
    pass


if __name__ == '__main__':
    TheMain()
