from datetime import timedelta

from babelfish import Language
from subliminal import download_best_subtitles, region, save_subtitles, scan_videos

import os
# configure the cache
region.configure('dogpile.cache.dbm', arguments={'filename': 'cachefile.dbm'})


rootdir="D:/Downloads"
for folder in os.listdir(rootdir):
    path = str(os.path.join(rootdir,folder))
    videos = scan_videos(path, age=timedelta(days=3))
    scan_videos()
    #print(videos)
    print("scan success:"+str(path))
    try:
        subtitles = download_best_subtitles(videos, {Language('eng')})
    except:
        print("skip")
        continue
    for v in videos:
        save_subtitles(v,subtitles[v])

    
