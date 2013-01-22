####################################################################################################
NAME = 'TVHeadend'
ART = 'art-default.jpg'
ICON = 'icon-default.png'
PLUGIN_PREFIX = '/video/tvheadend'
structure = 'stream/channelid'
htsurl = 'http://%s:%s@%s:%s/%s/' % (Prefs['tvheadend_user'], Prefs['tvheadend_pass'], Prefs['tvheadend_host'], Prefs['tvheadend_port'], structure)

####################################################################################################

def Start():
	Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, NAME, ICON, ART)

	ObjectContainer.art = R(ART)	
	objectContainer.title1 = NAME

	TrackObject.thumb = R(ICON)

####################################################################################################

def MainMenu():

	oc = ObjectContainer(no_cache = True)
	oc.add(DirectoryObject(key = Callback(ChannelsMenu, title = L('Channels')), title = L('Channels')))

	oc.add(PrefsObject(title = L('Preferences')))

	return oc

def ChannelsMenu(title):
        oc = ObjectContainer(view_group='InfoList')

        oc = ObjectContainer(title1="Channels")
        mo = MediaObject(parts=[PartObject(key=HTTPLiveStreamURL("%s25" % (htsurl)))])
        vco = VideoClipObject(title="C More Sport", url='%s25' % (htsurl))
        vco.add(mo)
        oc.add(vco)

        return oc

