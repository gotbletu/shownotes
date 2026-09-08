#!/usr/bin/env bash
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)
#         https://www.youtube.com/user/gotbletu
# DESC:   my unfinish example shellnium script for craigslist
# DEMO:   https://youtu.be/Q10dcPjmRTI
# DEPEND: jq chromium (or chrome)
#         shellnium (https://github.com/Rasukarusan/shellnium)

# start chromedriver
chromedriver &
sleep 1

source ./lib/selenium.sh

ITEM_TITLE="Leaf Village"
ITEM_PRICE="10"
ITEM_CITY="North Hollywood"
ITEM_POSTAL="91601"
ITEM_DESCRIPTION="Village Hidden in the Leaf"
ITEM_CONTACTEMAIL="tobi@akatsuki.com"
ITEM_CONTACTNUM="818-333-4444"
ITEM_CONTACTNAME="Tobi"

ITEM_STREET="hatteras"
ITEM_CROSSSTREET="tujunga"

main() {

    # 1. Open the apage.
    navigate_to 'https://post.craigslist.org/c/lax'

    # Click on radio "san fernado valley"
    # <input type="radio" name="n" value="2">
    local radioclick_location=($(find_elements 'name' 'n'))
    click ${radioclick_location[1]}


    # 2. Click on radio "for sale by owner"
    local radioclick_sale=($(find_elements 'name' 'id'))
    click ${radioclick_sale[5]}

    # 3. Click on radio "video gaming by owner"
    local radioclick_videogame=($(find_elements 'name' 'id'))
    click ${radioclick_videogame[43]}

    # 4. Fill in Ad listing

    # Post Title
    # <input class="json-form-input" name="PostingTitle" value="" tabindex="1" type="text" autofocus="autofocus" id="PostingTitle" maxlength="70">
    local AD_TITLE=$(find_element 'name' 'PostingTitle')
    send_keys $AD_TITLE "$ITEM_TITLE"

    # Price
    # <input type="number" class="json-form-input" name="price" value="" title="Please enter a number" tabindex="1" maxlength="11">
    local AD_PRICE=$(find_element 'name' 'price')
    send_keys $AD_PRICE "$ITEM_PRICE"

    # City or neighborhood
    # <input class="json-form-input" name="geographic_area" value="" tabindex="1" type="text" id="geographic_area" maxlength="60">
    local AD_CITY=$(find_element 'name' 'geographic_area')
    send_keys $AD_CITY "$ITEM_CITY"

    # Postal Code/Zip code
    # <input class="json-form-input" name="postal" value="" tabindex="1" type="text" id="postal_code" maxlength="15">
    local AD_POSTAL=$(find_element 'name' 'postal')
    send_keys $AD_POSTAL "$ITEM_POSTAL"

    # Description
    # <textarea class="json-form-input PostingBody " name="PostingBody" placeholder="" tabindex="1" id="PostingBody" rows="10"></textarea>
    local AD_DESCRIPTION=$(find_element 'name' 'PostingBody')
    send_keys $AD_DESCRIPTION "$ITEM_DESCRIPTION"

    # [checkbox] include "more ads by this user" link
    # <input type="checkbox" name="see_my_other" value="1" class="see_my_other">
    local checkbox_moreads=($(find_element 'name' 'see_my_other'))
    click ${checkbox_moreads}

    # [checkbox] contact info: phone/text options enable
    # <input type="checkbox" name="show_phone_ok" value="1" class="show_phone_ok">
    local checkbox_phone=($(find_element 'name' 'show_phone_ok'))
    click ${checkbox_phone}

    # [checkbox] text/SMS OK
    # <input type="checkbox" name="contact_text_ok" value="1" class="contact_text_ok">
    local checkbox_texting=($(find_element 'name' 'contact_text_ok'))
    click ${checkbox_texting}

    # Contact Email
    # <input class="json-form-input" name="FromEMail" value="" tabindex="1" type="text" placeholder="Your email address" autocapitalize="off" maxlength="60">
    local AD_CONTACTEMAIL=$(find_element 'name' 'FromEMail')
    send_keys $AD_CONTACTEMAIL "$ITEM_CONTACTEMAIL"

    # Contact Number: Phone Number/Texting Number
    # <input class="json-form-input" name="contact_phone" value="" tabindex="1" type="tel">
    local AD_CONTACTNUM=$(find_element 'name' 'contact_phone')
    send_keys $AD_CONTACTNUM "$ITEM_CONTACTNUM"

    # Contact Name
    # <input class="json-form-input" name="contact_name" value="" tabindex="1" type="text">
    local AD_CONTACTNAME=$(find_element 'name' 'contact_name')
    send_keys $AD_CONTACTNAME "$ITEM_CONTACTNAME"

    # Click Continue Button
    # <button type="submit" name="go" value="continue" class="go big-button submit-button" tabindex="1">continue</button>
    local button_continue=($(find_element 'name' 'go'))
    click ${button_continue}

    # 5. Map Page
    # Street
    # <input tabindex="1" id="xstreet0" name="xstreet0" size="16" maxlength="80" value="">
    local AD_STREET=$(find_element 'name' 'xstreet0')
    send_keys $AD_STREET "$ITEM_STREET"

    # Cross Street
    # <input tabindex="1" id="xstreet1" name="xstreet1" size="16" maxlength="80" value="">
    local AD_CROSSSTREET=$(find_element 'name' 'xstreet1')
    send_keys $AD_CROSSSTREET "$ITEM_CROSSSTREET"

    # City (use same variables as last page)
    # <input tabindex="1" id="city" name="city" size="16" maxlength="80" value="">
    local AD_CITY=$(find_element 'name' 'city')
    send_keys $AD_CITY "$ITEM_CITY"

    # Postal (use same variables as last page)
    # <input tabindex="1" id="postal_code" name="postal" size="7" maxlength="7" value="91601">
    local AD_POSTAL=$(find_element 'name' 'POSTAL')
    send_keys $AD_POSTAL "$ITEM_POSTAL"

    # Click Find Button
    # <button id="search_button" type="submit">find</button>
    local button_find=$(find_element 'id' 'search_button')
    click ${button_find}

    # Click Continue Button (class name with space just ignore the anything after the 1st word)
    # <button class="continue bigbutton" type="submit">continue</button>
    local button_continue=($(find_element 'class name' 'continue'))
    click ${button_continue}

    # 6. Add Images: Max 24 images
    # Add Images Button
    # <input id="html5_1ev3jmtn2s6v1d34598198uckb3" type="file" style="font-size:
    # local inputElement=$(find_element 'xpath' "//input[@type='file' and @id='file-input']")
    local inputElement=$(find_element 'xpath' "//input[@type='file']")
    send_keys $inputElement "/media/Suiton/Downloads/tobi.png\n/media/Suiton/Downloads/tobiren.jpg"

    sleep 10

    # Click done with images Button
    # <button class="done bigbutton" tabindex="1" type="submit" name="go" value="Done with Images">done with images</button>
    local button_donewithimages=($(find_element 'class name' 'done'))
    click ${button_donewithimages}

}
main

# stop chromedriver
killall chromedriver
