Feature: User Guide Page Navigation

  Scenario: User can open User Guide page
    Given the user is on the main page "https://soft.reelly.io"
    When the user logs in with the username "binta.mballo29@gmail.com" and password "Bineta1994"
    And the user waits for the sidebar to be visible
    And the user clicks on the settings option
    And the user clicks on the User Guide option
    Then the User Guide page opens with the title "User guide"
    And all lesson videos on the User Guide page contain titles
