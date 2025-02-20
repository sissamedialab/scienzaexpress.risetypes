# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s scienzaexpress.risetypes -t test_contenuto_digitale.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src scienzaexpress.risetypes.testing.SCIENZAEXPRESS_RISETYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/scienzaexpress/risetypes/tests/robot/test_contenuto_digitale.robot
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

Scenario: As a site administrator I can add a Contenuto Digitale
  Given a logged-in site administrator
    and an add Contenuto Digitale form
   When I type 'My Contenuto Digitale' into the title field
    and I submit the form
   Then a Contenuto Digitale with the title 'My Contenuto Digitale' has been created

Scenario: As a site administrator I can view a Contenuto Digitale
  Given a logged-in site administrator
    and a Contenuto Digitale 'My Contenuto Digitale'
   When I go to the Contenuto Digitale view
   Then I can see the Contenuto Digitale title 'My Contenuto Digitale'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Contenuto Digitale form
  Go To  ${PLONE_URL}/++add++Contenuto Digitale

a Contenuto Digitale 'My Contenuto Digitale'
  Create content  type=Contenuto Digitale  id=my-contenuto_digitale  title=My Contenuto Digitale

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Contenuto Digitale view
  Go To  ${PLONE_URL}/my-contenuto_digitale
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Contenuto Digitale with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Contenuto Digitale title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
