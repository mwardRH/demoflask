import requests
import sys
import time

def main():
    uri = sys.argv[1]
    #uri = input('Please input the url: ')
    i = 0
    while  i != 10:
        r = requests.get(uri)
        print(r.content)
        time.sleep(1)
        i = i+1

if __name__ == '__main__':
    main()
