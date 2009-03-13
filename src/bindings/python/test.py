#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Simple test to show how Spytify works.
# Copyright Jørgen P. Tjernø <jorgen@devsoft.no>

from getpass import getpass
import sys

import spytify

def print_track(track):
    has_metadata = "un"
    if track.has_meta_data():
        has_metadata = ""

    print "  > %03d %s - %s (%s), length: %d [%splayable]" % (track.id, track.artist,
                                                              track.title, track.album,
                                                              track.length, has_metadata)

def main():
    print "Enter your username: ",
    username = sys.stdin.readline().strip()

    if not username:
        print >>sys.stderr, "Empty username, exiting."
        sys.exit(1)

    password = getpass("Enter your password: ").strip()
    if not password:
        print >>sys.stderr, "Empty password, exiting."
        sys.exit(1)

    s = spytify.Spytify(username, password)

    print "Enter searchterm: (blank for foo) "
    searchterm = sys.stdin.readline().strip()
    if not searchterm:
        searchterm = "foo"

    print "\nStored playlists:"
    playlists = s.stored_playlists()
    for playlist in playlists:
        print " %s, by %s" % (playlist.name, playlist.author)
        for track in playlist.tracks:
            print_track(track)

    sr = s.search(searchterm)

    print "\nSearch:"
    print " %s, by %s" % (sr.name, sr.author)
    for track in sr.tracks:
        print_track(track)

    s.close()

if __name__ == '__main__':
    main()