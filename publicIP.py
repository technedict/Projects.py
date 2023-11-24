import requests as req

def getIP():
    try:
        url: str = 'https://checkip.amazonaws.com'
        request = req.get(url)
        ip: str = request.text
        print(f'\nYour IP Address is: {ip}')

    except Exception as err:
        if 'NameResolutionError' in str(err):
            print("\n\nYou aren't connected to the internet")
        elif "Read timed out." in str(err):
            print("\nYou do not have data connection")
        else:
            print(f'There was an error: {err}')

  
getIP()
input("\nPress Enter to exit ")
