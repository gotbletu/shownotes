# this is notes for video: http://www.youtube.com/watch?v=UhVKuAozSMc

say() { 
        # limit to 100 character or less
        # language code: http://developers.google.com/translate/v2/using_rest#language-params
        # useage: say <language code> <phase>
        # example: say es come with me
	mplayer -user-agent Mozilla \
        "http://translate.google.com/translate_tts?ie=UTF-8&tl="$1"&q=$(echo "$@" \
        | cut -d ' ' -f2- | sed 's/ /\+/g')" > /dev/null 2>&1 ;}

say-translation() { 
        # by: gotbletu
        # requires: http://www.soimort.org/google-translate-cli/
        # limit to 100 character or less
        # language code: http://developers.google.com/translate/v2/using_rest#language-params
        # useage: say-translation <language code> <phase>
        # example: say-translation es come with me
        lang=$1
        trans=$(translate {=$lang} "$(echo "$@" | cut -d ' ' -f2- | sed 's/ /\+/g')" )
        echo $trans
        mplayer -user-agent Mozilla \
        "http://translate.google.com/translate_tts?ie=UTF-8&tl=$lang&q=$trans" > /dev/null 2>&1 ;}
