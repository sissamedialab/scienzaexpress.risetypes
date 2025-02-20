# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s scienzaexpress.risetypes -t test_materiale_istruttorio.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src scienzaexpress.risetypes.testing.SCIENZAEXPRESS_RISETYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/scienzaexpress/risetypes/tests/robot/test_materiale_istruttorio.robot
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

Scenario: As a site administrator I can add a Materiale Istruttorio
  Given a logged-in site administrator
    and an add Materiale Istruttorio form
   When I type 'My Materiale Istruttorio' into the title field
    and I submit the form
   Then a Materiale Istruttorio with the title 'My Materiale Istruttorio' has been created

Scenario: As a site administrator I can view a Materiale Istruttorio
  Given a logged-in site administrator
    and a Materiale Istruttorio 'My Materiale Istruttorio'
   When I go to the Materiale Istruttorio view
   Then I can see the Materiale Istruttorio title 'My Materiale Istruttorio'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Materiale Istruttorio form
  Go To  ${PLONE_URL}/++add++Materiale Istruttorio

a Materiale Istruttorio 'My Materiale Istruttorio'
  Create content  type=Materiale Istruttorio  id=my-materiale_istruttorio  title=My Materiale Istruttorio

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Materiale Istruttorio view
  Go To  ${PLONE_URL}/my-materiale_istruttorio
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Materiale Istruttorio with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Materiale Istruttorio title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
