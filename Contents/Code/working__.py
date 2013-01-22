####################################################################################################
NAME = 'TVHeadend'
ART = 'art-default.jpg'
ICON = 'icon-default.png'
PLUGIN_PREFIX = '/video/tvheadend'
structure = 'stream/channelid'
htsurl = 'http://%s:%s@%s:%s/%s/' % (user, password, addr, port, structure)

####################################################################################################

def Start():
	Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, NAME, ICON, ART)

	ObjectContainer.art = R(ART)	
	objectContainer.title1 = NAME

	TrackObject.thumb = R(ICON)

####################################################################################################

def MainMenu():

        oc = ObjectContainer(view_group='InfoList')

        oc = ObjectContainer(title1="Channels")       
        mo = MediaObject(parts=[PartObject(key=HTTPLiveStreamURL("http://hemma.yakumo.se:9981/stream/channelid/18"))])
        vco = VideoClipObject(title="C More Hockey", url='http://hemma.yakumo.se:9981/stream/channelid/18')
        vco.add(mo)
        oc.add(vco)

        mo = MediaObject(parts=[PartObject(key=HTTPLiveStreamURL("http://%s:%s/stream/channelid/20" % (addr, port)))])
        vco = VideoClipObject(title="C More Live", url='http://%s:%s/stream/channelid/20' % (addr, port))
        vco.add(mo)
        oc.add(vco)

        mo = MediaObject(parts=[PartObject(key=HTTPLiveStreamURL("%s25" % (htsurl)))])
        vco = VideoClipObject(title="C More Sport", url='%s25' % (htsurl))
        vco.add(mo)
        oc.add(vco)

        return oc
