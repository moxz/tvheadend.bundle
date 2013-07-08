tvheadend.bundle
================

HTS-TVHeadend channel for Plex Media Server

WIP and Proof of concept.
This Channel takes the http streams from TVheadend and displays them in your PHT/PMC client.
A better way would probably to directly communicate with TVheaend with it's own hts protocol.

What does it do for now?

It supports direct stream from TVheadend from a directly taken stream : example http://user:password@server:port/stream/channelid/number
It has some support for using TVheadend as encoder/transcoder (this need's some tweaking and an git version of tvheadend with transcoding enabled).
Preferences for username, password, port, enable/disable transcoding. (For some reason after editing the Preferences PMS has to be restarted, this needs to be fixed)
It only works in PHT och PLEX Media Client on OSX Win Linux for now.

Thanks to Furs on Plex Forums the plugin now gets all channels directly from TVheadend


Things to do in no order: 
Auto import and list channels from tvheadend

Options for using TVHeadend as a transcoder so iOS/mobile devices can use the plugin.
(Some code for this has been added)

Things that have superlow prio.
EPG
Recording options

Icon is a  mockup of TVheadend logo (https://tvheadend.org) and Plex logo (http://plexapp.com) all rights to their respective owners. 
