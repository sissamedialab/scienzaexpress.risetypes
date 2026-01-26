# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s scienzaexpress.risetypes -t test_manoscritto.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src scienzaexpress.risetypes.testing.SCIENZAEXPRESS_RISETYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/scienzaexpress/risetypes/tests/robot/test_manoscritto.robot
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

Scenario: As a site administrator I can add a Manoscritto
  Given a logged-in site administrator
    and an add Manoscritto form
   When I type 'My Manoscritto' into the title field
    and I submit the form
   Then a Manoscritto with the title 'My Manoscritto' has been created

Scenario: As a site administrator I can view a Manoscritto
  Given a logged-in site administrator
    and a Manoscritto 'My Manoscritto'
   When I go to the Manoscritto view
   Then I can see the Manoscritto title 'My Manoscritto'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Manoscritto form
  Go To  ${PLONE_URL}/++add++Manoscritto

a Manoscritto 'My Manoscritto'
  Create content  type=Manoscritto  id=my-manoscritto  title=My Manoscritto

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Manoscritto view
  Go To  ${PLONE_URL}/my-manoscritto
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Manoscritto with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Manoscritto title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
