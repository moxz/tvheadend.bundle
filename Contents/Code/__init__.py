####################################################################################################
#               Thanks to Mikedm139 for helping me getting this to work. 			   #
####################################################################################################
NAME = 'TVHeadend'
ART = 'art-default.jpg'
ICON = 'icon-default.png'
PLUGIN_PREFIX = '/video/tvheadend'

#Links Structures
structure = 'stream/channelid'
transcode = '?mux=matroska&acodec=vorbis&vcodec=H264&scodec=NONE&transcode=1&resolution=384' ## Prof Of Concept
htsurl = 'http://%s:%s@%s:%s/%s/' % (Prefs['tvheadend_user'], Prefs['tvheadend_pass'], Prefs['tvheadend_host'], Prefs['tvheadend_port'], structure)

#Options
options_transcode = '%s' % (Prefs['tvheadend_transcode'])

#Resource Files
xml_file = Resource.Load('channels.xml')

#Texts
TEXT_TITLE = u'HTS-TVheadend'
TEXT_CHANNELS = u'Channels'

####################################################################################################

def Start():
	Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, NAME, ICON, ART)

	ObjectContainer.art = R(ART)	
	TrackObject.thumb = R(ICON)

####################################################################################################

@handler('/video/tvheadend', TEXT_TITLE, thumb=ICON, art=ART)
def MainMenu():

	menu = ObjectContainer(title1=TEXT_TITLE)
	menu.add(DirectoryObject(key=Callback(GetChannels, prevTitle=TEXT_TITLE), title=TEXT_CHANNELS,))
	menu.add(PrefsObject(title='Preferences'))

	return menu

if "on" in options_transcode:
	def GetChannels(prevTitle):
        
		xml_content = XML.ElementFromString(xml_file)
        	channels = xml_content.xpath("//channel")
        	channelList = ObjectContainer(title1=prevTitle, title2=TEXT_CHANNELS)
        

		for channel in channels:
        	        name = channel.get('name')
        	        id = channel.get('id')
               		icons = channel.get('icon')
                	mo = MediaObject(parts=[PartObject(key=HTTPLiveStreamURL("%s%s%s" % (htsurl, id, transcode)))])
                	vco = VideoClipObject(title=name, thumb=icons, url='%s%s%s' % (htsurl, id, transcode))
                	vco.add(mo)
                	channelList.add(vco)
        	return channelList

else:
	def GetChannels(prevTitle):
        
		xml_content = XML.ElementFromString(xml_file)
        	channels = xml_content.xpath("//channel")
       		channelList = ObjectContainer(title1=prevTitle, title2=TEXT_CHANNELS)

        
		for channel in channels:
                	name = channel.get('name')
                	id = channel.get('id')
			icons = channel.get('icon')
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
