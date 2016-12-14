*** Settings ***

Documentation  Test load related items button from the automatic related items behavior
Resource  plone/app/robotframework/keywords.robot
Variables  plone/app/testing/interfaces.py

Library  Remote  ${PLONE_URL}/RobotRemote

Suite Setup  Open Test Browser
Suite Teardown  Close all browsers

*** Variables ***

${title_selector}  input#form-widgets-IDublinCore-title
${tags_selector}  textarea#form-widgets-IDublinCore-subjects

*** Test Cases ***

Test Automatic Related Items
    Enable Autologin as  Owner
    Go to Homepage

    Create  Related Item 1  Tag1
    Page Should Contain  Item created
    Page Should Not Contain Element  css=#relatedItemBox
    Go to Homepage

    Create  Related Item 2  Tag1\nTag2
    Page Should Contain  Item created
    Page Should Contain Element  css=#relatedItemBox
    Page Should Contain  Related Item 1
    Go to Homepage

    Create  Related Item 3  Tag1\nTag2\nTag3
    Page Should Contain  Item created
    Page Should Contain Element  css=#relatedItemBox
    Page Should Contain  Related Item 1
    Page Should Contain  Related Item 2
    Go to Homepage

    Create  Related Item 4  Tag1\nTag2\nTag3\nTag4
    Page Should Contain  Item created
    Page Should Contain Element  css=#relatedItemBox
    Page Should Contain  Related Item 1
    Page Should Contain  Related Item 2
    Page Should Contain  Related Item 3

*** Keywords ***

Click Add News Item
    Open Add New Menu
    Click Link  css=a#news-item
    Page Should Contain  News Item

Create
    [arguments]  ${title}  ${tags}

    Click Add News Item
    Input Text  css=${title_selector}  ${title}
    Click Link  Categorization
    Input Text  css=${tags_selector}  ${tags}
    Click Button  Suggest related items
    Click Button  Save
