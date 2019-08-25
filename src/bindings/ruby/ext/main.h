/*
 * $Id$
 */

#ifndef __RB_DESPOTIFY_H
#define __RB_DESPOTIFY_H

VALUE cAlbum;
VALUE cAlbumBrowse;
VALUE cArtist;
VALUE cArtistBrowse;
VALUE cPlaylist;
VALUE cSearch;
VALUE cSession;
VALUE cTrack;

VALUE eDespotifyError;

typedef struct ds_album ds_album_t;
typedef struct ds_album_browse ds_album_browse_t;
typedef struct ds_artist ds_artist_t;
typedef struct ds_artist_browse ds_artist_browse_t;
typedef struct ds_playlist ds_playlist_t;
typedef struct ds_link ds_link_t;
typedef struct ds_search_result ds_search_t;
typedef struct despotify_session ds_session_t;
typedef struct ds_track ds_track_t;
typedef struct ds_user_info ds_user_info_t;

#define BOOL2VALUE(exp) exp ? Qtrue : Qfalse
#define RB_DESPOTIFYERR(session) \
	rb_raise(eDespotifyError, (session)->real->last_error)

#define HASH_VALUE_ADD(hash, key, val) \
	rb_hash_aset(hash, rb_str_new2((key)), (val))

#endif
