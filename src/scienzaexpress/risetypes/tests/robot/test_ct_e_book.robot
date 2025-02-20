# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s scienzaexpress.risetypes -t test_e_book.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src scienzaexpress.risetypes.testing.SCIENZAEXPRESS_RISETYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/scienzaexpress/risetypes/tests/robot/test_e_book.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a E-Book
  Given a logged-in site administrator
    and an add E-Book form
   When I type 'My E-Book' into the title field
    and I submit the form
   Then a E-Book with the title 'My E-Book' has been created

Scenario: As a site administrator I can view a E-Book
  Given a logged-in site administrator
    and a E-Book 'My E-Book'
   When I go to the E-Book view
   Then I can see the E-Book title 'My E-Book'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add E-Book form
  Go To  ${PLONE_URL}/++add++E-Book

a E-Book 'My E-Book'
  Create content  type=E-Book  id=my-e_book  title=My E-Book

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the E-Book view
  Go To  ${PLONE_URL}/my-e_book
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a E-Book with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the E-Book title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
