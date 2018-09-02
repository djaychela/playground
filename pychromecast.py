import pychromecast


print(dir(pychromecast))
casts = pychromecast.get_chromecasts()
for cast in casts:
    print(cast)