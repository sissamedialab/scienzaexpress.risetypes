# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s scienzaexpress.risebook -t test_corpo.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src scienzaexpress.risebook.testing.SCIENZAEXPRESS_RISEBOOK_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/scienzaexpress/risebook/tests/robot/test_corpo.robot
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

Scenario: As a site administrator I can add a Corpo
  Given a logged-in site administrator
    and an add Book form
   When I type 'My Corpo' into the title field
    and I submit the form
   Then a Corpo with the title 'My Corpo' has been created

Scenario: As a site administrator I can view a Corpo
  Given a logged-in site administrator
    and a Corpo 'My Corpo'
   When I go to the Corpo view
   Then I can see the Corpo title 'My Corpo'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Book form
  Go To  ${PLONE_URL}/++add++Book

a Corpo 'My Corpo'
  Create content  type=Book  id=my-corpo  title=My Corpo

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Corpo view
  Go To  ${PLONE_URL}/my-corpo
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Corpo with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Corpo title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
