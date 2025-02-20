# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s scienzaexpress.risetypes -t test_libro.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src scienzaexpress.risetypes.testing.SCIENZAEXPRESS_RISETYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/scienzaexpress/risetypes/tests/robot/test_libro.robot
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

Scenario: As a site administrator I can add a Libro
  Given a logged-in site administrator
    and an add Libro form
   When I type 'My Libro' into the title field
    and I submit the form
   Then a Libro with the title 'My Libro' has been created

Scenario: As a site administrator I can view a Libro
  Given a logged-in site administrator
    and a Libro 'My Libro'
   When I go to the Libro view
   Then I can see the Libro title 'My Libro'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Libro form
  Go To  ${PLONE_URL}/++add++Libro

a Libro 'My Libro'
  Create content  type=Libro  id=my-libro  title=My Libro

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Libro view
  Go To  ${PLONE_URL}/my-libro
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Libro with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Libro title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
