####################################################################################################
#               Thanks to Mikedm139 for helping me getting this to work. 			   #
####################################################################################################
NAME = 'TVHeadend'
#ART = 'art-default.jpg'
ICON = 'icon-default.png'
PLUGIN_PREFIX = '/video/tvheadend'

#import
import urllib2, base64, json

#Prefs
username = '%s' % (Prefs['tvheadend_user']) 
password = '%s' % (Prefs['tvheadend_pass'])
hostname = '%s' % (Prefs['tvheadend_host'])
web_port = '%s' % (Prefs['tvheadend_web_port'])
htsp_port = '%s' % (Prefs['tvheadend_htsp_port'])
options_transcode = '%s' % (Prefs['tvheadend_transcode'])

#Links Structures
structure = 'stream/channelid'
transcode = '?mux=matroska&acodec=vorbis&vcodec=H264&scodec=NONE&transcode=1&resolution=384' ## Proof Of Concept
htsurl = 'http://%s:%s@%s:%s/%s/' % (username, password, hostname, web_port, structure)

#Resource Files
xml_file = Resource.Load('channels.xml')

#Texts
TEXT_TITLE = u'HTS-TVheadend'
TEXT_CHANNELS = u'Channels'

####################################################################################################

def Start():
	Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, NAME, ICON)

#	ObjectContainer.art = R(ART)	
	TrackObject.thumb = R(ICON)

####################################################################################################

@handler('/video/tvheadend', TEXT_TITLE, thumb=ICON)
def MainMenu():

	menu = ObjectContainer(title1=TEXT_TITLE)
	menu.add(DirectoryObject(key=Callback(GetChannels, prevTitle=TEXT_TITLE), title=TEXT_CHANNELS,))
	menu.add(PrefsObject(title='Preferences'))

	return menu

def getChannelsjson(username,password,host,port):
        base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        request = urllib2.Request("http://%s:%s/channels" % (host,port),"op=list" )
        request.add_header("Authorization", "Basic %s" % base64string)
        response = urllib2.urlopen(request)
        json_tmp = response.read()
        json_data = json.loads(json_tmp)
        return json_data

if "on" in options_transcode:
	def GetChannels(prevTitle):
 		json_data = getChannelsjson(username,password,hostname,web_port)
		channelList = ObjectContainer(title1=prevTitle, title2=TEXT_CHANNELS)
		
		for channel in json_data['entries']:
			name = channel['name']
			id = channel['chid']
			if 'ch_icon' in channel:
				icons = channel['ch_icon']
			else:
				icons = ''
                	mo = MediaObject(parts=[PartObject(key=HTTPLiveStreamURL("%s%s%s" % (htsurl, id, transcode)))])
                	vco = VideoClipObject(title=name, thumb=icons, url='%s%s%s' % (htsurl, id, transcode))
                	vco.add(mo)
                	channelList.add(vco)
        	return channelList

else:
	def GetChannels(prevTitle):
		json_data = getChannelsjson(username,password,hostname,web_port)
		channelList = ObjectContainer(title1=prevTitle, title2=TEXT_CHANNELS)
		
		for channel in json_data['entries']:
			name = channel['name']
			id = channel['chid']
			if 'ch_icon' in channel:
				icons = channel['ch_icon']
			else:
				icons = ''
			mo = MediaObject(parts=[PartObject(key=HTTPLiveStreamURL("%s%s" % (htsurl, id)))])
			vco = VideoClipObject(title=name, thumb=icons, url='%s%s' % (htsurl, id))
			vco.add(mo)
			channelList.add(vco)
        	return channelList

#################################################
#Examples

#Original Demo code below
#def ChannelsMenu(title):
#	oc = ObjectContainer(view_group='InfoList')
#
#	oc = ObjectContainer(title1="Channels")
#	mo = MediaObject(parts=[PartObject(key=HTTPLiveStreamURL("%s25" % (htsurl)))])
#	vco = VideoClipObject(title="C More Sport", url='%s25' % (htsurl))
#	vco.add(mo)
#	oc.add(vco)
#
#	return oc

##		Transcoding options from TVHeadend											     ##
# http://user:password@tvheadendserver:9981/stream/channelid/66?mux=matroska&acodec=vorbis&vcodec=H264&scodec=NONE&transcode=1&resolution=384 #
##																       	     ##
