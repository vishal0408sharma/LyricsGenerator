import urllib2
from bs4 import BeautifulSoup

while(1):
    print "\nInput song song_name whose lyrics you want to generate (Simply hit enter to exit)\n>>> ",
    song_name=raw_input()
    song_name2=song_name

    if(song_name==""):
        print "\nNo song song_name entered \nExiting..."
        break;

    try:
        unicoded_song_name = song_name
        unicoded_song_name = unicode(unicoded_song_name, errors='replace')
        song_name = unicoded_song_name.encode('utf8')

        print('Searching lyrics for the song : '+song_name)
        song_name = song_name +' lyrics'
        song_name  = song_name.replace(' ','+')

        url = 'http://www.google.com/search?q='+song_name
        
        req = urllib2.Request(url, headers={'User-Agent' : "foobar"})

        response = urllib2.urlopen(req)
        str = response.read()
        str = unicode(str, errors='replace')

        search_results = str.encode('utf8')

        link_start=search_results.find('http://www.metrolyrics.com')
        link_end=search_results.find('html',link_start+1)

        link = search_results[link_start:link_end+4]
        print "Lyrics found"
        print "Generating lyrics ..."
        
        lyrics_html = urllib2.urlopen(link).read()
        soup = BeautifulSoup(lyrics_html)
        raw_lyrics= (soup.findAll('p', attrs={'class' : 'verse'}))
        lyrics=unicode.join(u'\n',map(unicode,raw_lyrics))

        lyrics= (lyrics.replace('<p class="verse">','\n'))
        lyrics= (lyrics.replace('<br/>',' '))
        lyrics = lyrics.replace('</p>',' ')

        print "The lyrics for the song is \n"
        print (lyrics)

        with open (song_name.replace('+',' ')+'.txt','a') as f:
                f.write(lyrics)
       
        print('\nlyrics file Generated! \n\n')

    except :
        print ('\nCould not find lyrics for '+song_name2+'\n\n')		

