# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s scienzaexpress.risetypes -t test_nuova_lettera_matematica.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src scienzaexpress.risetypes.testing.SCIENZAEXPRESS_RISETYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/scienzaexpress/risetypes/tests/robot/test_nuova_lettera_matematica.robot
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

Scenario: As a site administrator I can add a Nuova Lettera Matematica
  Given a logged-in site administrator
    and an add Nuova Lettera Matematica form
   When I type 'My Nuova Lettera Matematica' into the title field
    and I submit the form
   Then a Nuova Lettera Matematica with the title 'My Nuova Lettera Matematica' has been created

Scenario: As a site administrator I can view a Nuova Lettera Matematica
  Given a logged-in site administrator
    and a Nuova Lettera Matematica 'My Nuova Lettera Matematica'
   When I go to the Nuova Lettera Matematica view
   Then I can see the Nuova Lettera Matematica title 'My Nuova Lettera Matematica'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Nuova Lettera Matematica form
  Go To  ${PLONE_URL}/++add++Nuova Lettera Matematica

a Nuova Lettera Matematica 'My Nuova Lettera Matematica'
  Create content  type=Nuova Lettera Matematica  id=my-nuova_lettera_matematica  title=My Nuova Lettera Matematica

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Nuova Lettera Matematica view
  Go To  ${PLONE_URL}/my-nuova_lettera_matematica
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Nuova Lettera Matematica with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Nuova Lettera Matematica title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
