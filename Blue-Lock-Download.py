#! python3

import requests, os, bs4, threading

os.makedirs('./Blue Lock Manga', exist_ok=True) # store comics

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print(f"https://blue-lock-manga.com/manga/blue-lock-chapter-{urlNumber}")
        response = requests.get(f"https://blue-lock-manga.com/manga/blue-lock-chapter-{urlNumber}")
        response.raise_for_status()

        soup = bs4.BeautifulSoup(response.text, "lxml")

        # Find the URL of the comic image.
        Manga_Image_List = soup.select('p > img')
        if Manga_Image_List == []:
            print("Manga couldn't be found")
        else:
            for i in range(len(Manga_Image_List)):
                comicUrl = Manga_Image_List[i].get('src')
                # Download the image.
                print('Downloading image %s...' % (comicUrl))
                response = requests.get(comicUrl)
                response.raise_for_status()

                # Save the image to ./xkcd
                with open(f"./Blue Lock Manga/{Manga_Image_List[i].get('alt')}", 'wb') as imageFile:
                    for chunk in response.iter_content(100000):
                        imageFile.write(chunk)

# Create and start the Thread objects.
downloadThreads = [] # a list of all the Thread objects
for i in range(216, 217): # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
