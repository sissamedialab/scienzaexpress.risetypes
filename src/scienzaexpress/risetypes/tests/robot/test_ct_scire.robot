# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s scienzaexpress.risetypes -t test_scire.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src scienzaexpress.risetypes.testing.SCIENZAEXPRESS_RISETYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/scienzaexpress/risetypes/tests/robot/test_scire.robot
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

Scenario: As a site administrator I can add a SCIRE
  Given a logged-in site administrator
    and an add SCIRE form
   When I type 'My SCIRE' into the title field
    and I submit the form
   Then a SCIRE with the title 'My SCIRE' has been created

Scenario: As a site administrator I can view a SCIRE
  Given a logged-in site administrator
    and a SCIRE 'My SCIRE'
   When I go to the SCIRE view
   Then I can see the SCIRE title 'My SCIRE'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add SCIRE form
  Go To  ${PLONE_URL}/++add++SCIRE

a SCIRE 'My SCIRE'
  Create content  type=SCIRE  id=my-scire  title=My SCIRE

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the SCIRE view
  Go To  ${PLONE_URL}/my-scire
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a SCIRE with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the SCIRE title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
