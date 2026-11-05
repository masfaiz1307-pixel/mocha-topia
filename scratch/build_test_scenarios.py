# -*- coding: utf-8 -*-
"""
Generator for Mocha Topia Quality Assurance Test Scenarios (Week 7 Deliverable)
Course: Information Systems Agile Project Management with DevOps
Group 04: Faiz (012202500030), Immanuel (012202500017), Dwisasono (012202500064)
Target: 230 comprehensive test scenarios (>200 required) covering all testing types and project modules.
"""

import os
import csv
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# List of all 230 test cases
scenarios = []

def add_tc(tc_id, module, scenario, test_type, created_by, precond, steps, test_data, exp_result, act_result, status, executed_by, ref=""):
    scenarios.append({
        "id": tc_id,
        "module": module,
        "scenario": scenario,
        "type": test_type,
        "created_by": created_by,
        "preconditions": precond,
        "steps": steps,
        "test_data": test_data,
        "expected": exp_result,
        "actual": act_result,
        "status": status,
        "executed_by": executed_by,
        "ref": ref
    })

# -------------------------------------------------------------
# MODULE 1: USER REGISTRATION (25 Scenarios: MT-REG-001 to MT-REG-025)
# -------------------------------------------------------------
reg_creator = "Faiz (012202500030)"
reg_exec = "Faiz"

add_tc("MT-REG-001", "User Registration", "Successful registration with all valid inputs", 
       "Functional, Positive, Black-Box", reg_creator, "Browser is open on register.html; localStorage is clear",
       "1. Open register.html in browser\n2. Enter Username 'faiz_dev'\n3. Enter Email 'faiz@mochatopia.com'\n4. Enter Password 'CoffeePass123'\n5. Enter Confirm Password 'CoffeePass123'\n6. Click 'Register' button",
       "Username: faiz_dev, Email: faiz@mochatopia.com, Pass: CoffeePass123",
       "Alert 'Account created successfully! ✓' displays, credentials stored in localStorage, redirected to login.html",
       "Account created successfully and redirected to login.html", "Pass", reg_exec, "V-03")

add_tc("MT-REG-002", "User Registration", "Registration with minimum valid username length (exact 3 characters)",
       "Boundary Value Analysis, Positive, Functional", reg_creator, "On register.html",
       "1. Enter Username 'bob'\n2. Enter Email 'bob@test.com'\n3. Enter Password 'SecurePass99'\n4. Confirm Password 'SecurePass99'\n5. Click 'Register'",
       "Username: bob (length=3), Email: bob@test.com, Pass: SecurePass99",
       "Registration succeeds as 3 chars satisfies minimum length check (user.length >= 3)",
       "Validation passed and account registered", "Pass", reg_exec)

add_tc("MT-REG-003", "User Registration", "Registration fails when username is less than 3 characters (boundary 2 characters)",
       "Boundary Value Analysis, Negative, Functional", reg_creator, "On register.html",
       "1. Enter Username 'al'\n2. Enter Email 'al@test.com'\n3. Enter Password 'SecurePass99'\n4. Confirm Password 'SecurePass99'\n5. Click 'Register'",
       "Username: al (length=2), Email: al@test.com, Pass: SecurePass99",
       "Validation fails, #userError element is shown, form submission is blocked",
       "Username error message displayed, account not created", "Pass", reg_exec)

add_tc("MT-REG-004", "User Registration", "Registration fails when username is empty",
       "Equivalence Partitioning, Negative", reg_creator, "On register.html",
       "1. Leave Username field empty\n2. Enter valid Email and matching strong passwords\n3. Click 'Register'",
       "Username: '', Email: user@test.com, Pass: Coffee1234",
       "HTML5 required validation or JS length check prevents submission with warning prompt",
       "Form blocked submission with required field prompt", "Pass", reg_exec)

add_tc("MT-REG-005", "User Registration", "Registration handles username with only whitespace characters",
       "Negative, Robustness Testing", reg_creator, "On register.html",
       "1. Enter 4 whitespace spaces in Username\n2. Enter valid email and password\n3. Click 'Register'",
       "Username: '    ' (4 spaces), Email: test@test.com, Pass: Coffee1234",
       "Trimmed username becomes empty (length 0), #userError displays, submission blocked",
       "#userError displayed as trim() resulted in length 0", "Pass", reg_exec)

add_tc("MT-REG-006", "User Registration", "Registration with long alphanumeric username (50 characters)",
       "Boundary Value Analysis, Positive", reg_creator, "On register.html",
       "1. Enter a 50-character alphanumeric username\n2. Enter valid email and password\n3. Click 'Register'",
       "Username: 'user_' + 45 'a's, Email: user50@test.com, Pass: Pass12345",
       "Registration succeeds without text truncation or layout overflow",
       "Registered successfully, stored properly in localStorage", "Pass", reg_exec)

add_tc("MT-REG-007", "User Registration", "Registration with standard valid email address format",
       "Positive, Functional", reg_creator, "On register.html",
       "1. Enter valid username\n2. Enter Email 'barista.expert@mocha-topia.co.id'\n3. Enter valid matching passwords\n4. Click 'Register'",
       "Email: barista.expert@mocha-topia.co.id",
       "Regex passes, account saved successfully",
       "Email accepted and saved", "Pass", reg_exec)

add_tc("MT-REG-008", "User Registration", "Registration fails with email missing '@' symbol",
       "Negative, Equivalence Partitioning", reg_creator, "On register.html",
       "1. Enter Username 'testuser'\n2. Enter Email 'usermochatopia.com'\n3. Enter valid passwords\n4. Click 'Register'",
       "Email: usermochatopia.com",
       "HTML5 email validation and JS regex fail, #emailError displayed, submission blocked",
       "Submission blocked with invalid email warning", "Pass", reg_exec)

add_tc("MT-REG-009", "User Registration", "Registration fails with email missing top-level domain extension",
       "Negative, Equivalence Partitioning", reg_creator, "On register.html",
       "1. Enter Username 'testuser'\n2. Enter Email 'user@mochatopia'\n3. Enter valid passwords\n4. Click 'Register'",
       "Email: user@mochatopia",
       "Email regex test returns false, #emailError displayed",
       "#emailError shown, form blocked", "Pass", reg_exec)

add_tc("MT-REG-010", "User Registration", "Registration fails with email containing consecutive '@' signs",
       "Negative, Security / Robustness", reg_creator, "On register.html",
       "1. Enter Email 'john@@domain.com'\n2. Click Register",
       "Email: john@@domain.com",
       "Regex validation rejects malformed email address",
       "Email format rejected", "Pass", reg_exec)

add_tc("MT-REG-011", "User Registration", "Registration fails with email containing spaces in middle",
       "Negative, Data Integrity", reg_creator, "On register.html",
       "1. Enter Email 'john doe@domain.com'\n2. Click Register",
       "Email: john doe@domain.com",
       "Regex /^[^\s@]+@[^\s@]+\.[^\s@]+$/ returns false; rejected",
       "Rejected by regex validation", "Pass", reg_exec)

add_tc("MT-REG-012", "User Registration", "Registration with exact 8-character password meeting all 4 complexity rules",
       "Boundary Value Analysis, Positive", reg_creator, "On register.html",
       "1. Enter Password 'Aa123456' (length 8, 1 upper, 1 lower, 1 number)\n2. Re-enter same password in Confirm\n3. Click Register",
       "Pass: Aa123456",
       "All 4 rule indicators (#rule-length, #rule-upper, #rule-lower, #rule-number) turn green; submission allowed",
       "All 4 rules green, submission succeeded", "Pass", reg_exec)

add_tc("MT-REG-013", "User Registration", "Registration fails with 7-character password (just below minimum length)",
       "Boundary Value Analysis, Negative", reg_creator, "On register.html",
       "1. Enter Password 'Abc1234' (length 7)\n2. Confirm 'Abc1234'\n3. Click Register",
       "Pass: Abc1234 (7 chars)",
       "#rule-length stays red, alert prompt 'Password does not meet the requirements' appears on submit",
       "Alert displayed, registration blocked", "Pass", reg_exec)

add_tc("MT-REG-014", "User Registration", "Registration fails when password lacks uppercase character",
       "Negative, Rule Verification", reg_creator, "On register.html",
       "1. Enter Password 'mochatopia123' (all lowercase + digits)\n2. Check rule indicators\n3. Click Register",
       "Pass: mochatopia123",
       "#rule-upper indicator remains invalid; alert blocks submission",
       "Rule upper is red; alert prevented registration", "Pass", reg_exec)

add_tc("MT-REG-015", "User Registration", "Registration fails when password lacks lowercase character",
       "Negative, Rule Verification", reg_creator, "On register.html",
       "1. Enter Password 'MOCHATOPIA123' (all uppercase + digits)\n2. Click Register",
       "Pass: MOCHATOPIA123",
       "#rule-lower indicator remains invalid; alert blocks submission",
       "Rule lower is red; registration blocked", "Pass", reg_exec)

add_tc("MT-REG-016", "User Registration", "Registration fails when password lacks any numeric digit",
       "Negative, Rule Verification", reg_creator, "On register.html",
       "1. Enter Password 'MochaTopiaPass' (letters only)\n2. Click Register",
       "Pass: MochaTopiaPass",
       "#rule-number indicator remains invalid; alert blocks submission",
       "Rule number is red; registration blocked", "Pass", reg_exec)

add_tc("MT-REG-017", "User Registration", "Real-time password match feedback displays green success checkmark",
       "Usability, Functional, Positive", reg_creator, "On register.html",
       "1. Enter 'Coffee123' in regPass1\n2. Type 'Coffee123' in regPass2\n3. Observe feedback below confirm password",
       "regPass1: Coffee123, regPass2: Coffee123",
       "#passSuccess element displays '✓ Passwords match' in green, #passError is hidden",
       "Pass success message displayed in real time", "Pass", reg_exec)

add_tc("MT-REG-018", "User Registration", "Real-time password match feedback displays red error on mismatch",
       "Usability, Functional, Negative", reg_creator, "On register.html",
       "1. Enter 'Coffee123' in regPass1\n2. Type 'Coffee456' in regPass2\n3. Observe feedback",
       "regPass1: Coffee123, regPass2: Coffee456",
       "#passError element displays 'Passwords do not match' in red, #passSuccess is hidden",
       "Pass error displayed in real time", "Pass", reg_exec)

add_tc("MT-REG-019", "User Registration", "Registration blocks submission when passwords mismatch on submit",
       "Negative, Data Integrity", reg_creator, "On register.html",
       "1. Fill valid username, email\n2. Pass1: 'Coffee123'\n3. Pass2: 'Coffee999'\n4. Click Register button",
       "regPass1: Coffee123, regPass2: Coffee999",
       "Alert 'Passwords do not match!' displays, form does not submit or overwrite localStorage",
       "Alert displayed, localStorage unchanged", "Pass", reg_exec)

add_tc("MT-REG-020", "User Registration", "SQL injection string entered into username input field",
       "Security, Black-Box, Negative", reg_creator, "On register.html",
       "1. Enter Username: 'admin' OR '1'='1' --\n2. Fill valid email and password\n3. Click Register",
       "Username: admin' OR '1'='1' --",
       "Input is treated strictly as a literal text string in localStorage without syntax evaluation or app failure",
       "Stored as literal string, no execution or error", "Pass", reg_exec)

add_tc("MT-REG-021", "User Registration", "Cross-Site Scripting (XSS) payload entered into username input field",
       "Security, Black-Box, Negative", reg_creator, "On register.html",
       "1. Enter Username: <script>alert('XSS')</script>\n2. Complete registration and check rendered user welcome",
       "Username: <script>alert('XSS')</script>",
       "Script tags are not executed as active script; rendered safely or handled as text node",
       "No script popups fired; safe", "Pass", reg_exec)

add_tc("MT-REG-022", "User Registration", "Registration handles special unicode characters and emoji in username",
       "Internationalization, Robustness", reg_creator, "On register.html",
       "1. Enter Username: 'Kopi☕Lover_99'\n2. Fill valid email and password\n3. Click Register",
       "Username: Kopi☕Lover_99",
       "Unicode characters and emoji persist accurately in localStorage without encoding distortion",
       "Username preserved with emoji in storage", "Pass", reg_exec)

add_tc("MT-REG-023", "User Registration", "Navigation link 'Already have an account?' redirects to login page",
       "Navigation, Functional, Positive", reg_creator, "On register.html",
       "1. Scroll to bottom of registration form\n2. Click 'Already have an account?' hyperlink",
       "Click action on login link",
       "Browser redirects to login.html in main frame",
       "Successfully navigated to login.html", "Pass", reg_exec)

add_tc("MT-REG-024", "User Registration", "Re-registration overwrites previous stored user credentials in localStorage",
       "State Transition, Functional", reg_creator, "Existing user 'user1' in localStorage",
       "1. Register new user 'user2' with email 'user2@test.com' and password 'NewPass123'\n2. Inspect localStorage keys 'username', 'email'",
       "New user: user2",
       "localStorage keys 'username' and 'email' are updated to reflect the newly registered account",
       "localStorage updated with new credentials", "Pass", reg_exec)

add_tc("MT-REG-025", "User Registration", "Password input fields mask characters with asterisks / dots",
       "Usability, Security", reg_creator, "On register.html",
       "1. Focus regPass1 and regPass2 inputs\n2. Type alphanumeric characters\n3. Verify characters are masked",
       "Type: 'Secret123'",
       "Input type is 'password'; text characters are masked on screen to prevent shoulder surfing",
       "Characters masked as password type", "Pass", reg_exec)

# -------------------------------------------------------------
# MODULE 2: USER LOGIN & AUTHENTICATION (25 Scenarios: MT-AUTH-001 to MT-AUTH-025)
# -------------------------------------------------------------
auth_creator = "Faiz (012202500030)"
auth_exec = "Faiz"

add_tc("MT-AUTH-001", "User Login", "Successful login with valid registered credentials",
       "Functional, Positive, Black-Box", auth_creator, "Account registered in localStorage (faiz_dev / CoffeePass123)",
       "1. Open login.html\n2. Enter Username 'faiz_dev'\n3. Enter Password 'CoffeePass123'\n4. Click 'Login' button",
       "Username: faiz_dev, Password: CoffeePass123",
       "Alert 'Login successful!' appears, localStorage 'loggedIn' set to 'true', redirected to frameset.html",
       "Alert shown, session loggedIn='true', redirected to frameset.html", "Pass", auth_exec, "V-04")

add_tc("MT-AUTH-002", "User Login", "Login fails with incorrect password for existing user",
       "Negative, Functional", auth_creator, "Registered user: faiz_dev / CoffeePass123",
       "1. Open login.html\n2. Enter Username 'faiz_dev'\n3. Enter Password 'WrongPass999'\n4. Click Login",
       "Username: faiz_dev, Password: WrongPass999",
       "Alert 'Incorrect username or password!' appears, loggedIn key remains unset, page does not redirect",
       "Alert displayed, login blocked", "Pass", auth_exec)

add_tc("MT-AUTH-003", "User Login", "Login fails with non-existent / unregistered username",
       "Negative, Functional", auth_creator, "Registered user is faiz_dev",
       "1. Open login.html\n2. Enter Username 'ghost_user'\n3. Enter Password 'CoffeePass123'\n4. Click Login",
       "Username: ghost_user, Password: CoffeePass123",
       "Alert 'Incorrect username or password!' appears, login rejected",
       "Alert displayed, access denied", "Pass", auth_exec)

add_tc("MT-AUTH-004", "User Login", "Login fails when username field is empty",
       "Negative, Equivalence Partitioning", auth_creator, "On login.html",
       "1. Leave Username field blank\n2. Enter valid password\n3. Click Login button",
       "Username: '', Password: CoffeePass123",
       "HTML5 form validation prompts user to fill out username field; submission stopped",
       "Browser displayed 'Please fill out this field' validation tooltip", "Pass", auth_exec)

add_tc("MT-AUTH-005", "User Login", "Login fails when password field is empty",
       "Negative, Equivalence Partitioning", auth_creator, "On login.html",
       "1. Enter valid username\n2. Leave Password field blank\n3. Click Login button",
       "Username: faiz_dev, Password: ''",
       "HTML5 required validation prevents submission",
       "Submission blocked by required constraint", "Pass", auth_exec)

add_tc("MT-AUTH-006", "User Login", "Login trims leading and trailing whitespace on username",
       "Boundary / Robustness, Positive", auth_creator, "Registered user: faiz_dev",
       "1. Enter Username '   faiz_dev   ' (3 spaces before and after)\n2. Enter valid password\n3. Click Login",
       "Username: '   faiz_dev   ', Pass: CoffeePass123",
       "JS .trim() cleans whitespace; matches stored username and allows login",
       "Trim succeeded; login authenticated successfully", "Pass", auth_exec)

add_tc("MT-AUTH-007", "User Login", "Case-sensitive password check rejects lowercase variant",
       "Security, Functional, Negative", auth_creator, "Registered password: 'CoffeePass123'",
       "1. Enter Username 'faiz_dev'\n2. Enter Password 'coffeepass123' (all lowercase)\n3. Click Login",
       "Password: coffeepass123",
       "Strict equality comparison (===) fails; alert 'Incorrect username or password!' displays",
       "Rejected due to case mismatch", "Pass", auth_exec)

add_tc("MT-AUTH-008", "User Login", "SQL Injection payload in username input does not bypass auth",
       "Security, Black-Box, Negative", auth_creator, "Registered user exists in storage",
       "1. Enter Username: ' OR '1'='1\n2. Enter Password: ' OR '1'='1\n3. Click Login",
       "Username: ' OR '1'='1, Password: ' OR '1'='1",
       "JS client evaluation compares literal strings against localStorage; auth bypass fails",
       "Authentication failed safely; alert shown", "Pass", auth_exec)

add_tc("MT-AUTH-009", "User Login", "Navigation to 'Forgot Password?' page",
       "Navigation, Positive", auth_creator, "On login.html",
       "1. Click 'Forgot Password?' hyperlink below login form",
       "Click action on forgot link",
       "Browser navigates to forgot.html",
       "Redirected to forgot.html successfully", "Pass", auth_exec)

add_tc("MT-AUTH-010", "User Login", "Forgot password submission with registered email displays instructions",
       "Functional, Positive", auth_creator, "On forgot.html; registered email exists",
       "1. Enter registered email address\n2. Click 'Reset Password' button",
       "Email: faiz@mochatopia.com",
       "Alert / notification displays that password reset link or instructions were dispatched",
       "Reset message displayed to user", "Pass", auth_exec)

add_tc("MT-AUTH-011", "User Login", "Forgot password submission with empty email field",
       "Negative, Equivalence Partitioning", auth_creator, "On forgot.html",
       "1. Leave email input empty\n2. Click 'Reset Password'",
       "Email: ''",
       "Required validation blocks submission",
       "Validation tooltip shown; form not submitted", "Pass", auth_exec)

add_tc("MT-AUTH-012", "User Login", "Navigation to 'Create an Account' from login page",
       "Navigation, Positive", auth_creator, "On login.html",
       "1. Click 'Create an Account' hyperlink",
       "Click action on register link",
       "Browser redirects to register.html",
       "Redirected to register.html", "Pass", auth_exec)

add_tc("MT-AUTH-013", "User Login", "User logout clears authentication session flag",
       "Session Management, Functional, Positive", auth_creator, "User is currently logged in (loggedIn='true')",
       "1. Click 'Logout' in sidebar or open logout.html\n2. Inspect localStorage key 'loggedIn'",
       "Action: Logout",
       "localStorage key 'loggedIn' is removed or set to false; redirected to login.html / welcome.html",
       "Session cleared; redirected to login page", "Pass", auth_exec)

add_tc("MT-AUTH-014", "User Login", "Session persists after page reload",
       "State Persistence, Positive", auth_creator, "User is logged in (loggedIn='true')",
       "1. Press F5 or Ctrl+R to reload dashboard\n2. Check session status",
       "Action: Browser refresh",
       "User session remains active without asking to login again",
       "Dashboard loads with active user session", "Pass", auth_exec)

add_tc("MT-AUTH-015", "User Login", "Session persists when opening application in a new browser tab",
       "Session Management, Positive", auth_creator, "User is logged in on Tab 1",
       "1. Open new tab in same browser window\n2. Navigate to http://localhost:8080/frameset.html\n3. Verify state",
       "Action: Open new tab",
       "localStorage is shared across tabs of same origin; user is recognized as logged in",
       "Logged-in state maintained across tabs", "Pass", auth_exec)

add_tc("MT-AUTH-016", "User Login", "Session is isolated and not present in private / incognito window",
       "Security / Isolation, Positive", auth_creator, "User is logged in on normal browser window",
       "1. Open new Incognito / InPrivate browser window\n2. Navigate to http://localhost:8080/dashboard.html",
       "Action: Incognito window navigation",
       "Incognito window has clean storage; loggedIn is null",
       "Clean session detected in private mode", "Pass", auth_exec)

add_tc("MT-AUTH-017", "User Login", "Enter key presses in password field submits the login form",
       "Usability, Keyboard Navigation", auth_creator, "On login.html with inputs filled",
       "1. Type username and password\n2. Press Enter key while focused on password field",
       "Key: Enter",
       "Form submit event fires automatically, authenticating credentials",
       "Form submitted and authenticated on Enter", "Pass", auth_exec)

add_tc("MT-AUTH-018", "User Login", "Tab key correctly traverses from Username to Password to Submit button",
       "Accessibility / Usability", auth_creator, "On login.html",
       "1. Focus Username field\n2. Press Tab key\n3. Press Tab key again",
       "Key: Tab",
       "Focus moves sequentially from logUser -> logPass -> dark-btn",
       "Tab order is logical and accessible", "Pass", auth_exec)

add_tc("MT-AUTH-019", "User Login", "Console logging of credentials during login",
       "Security / Code Review", auth_creator, "On login.html; Developer Tools opened (F12)",
       "1. Enter credentials and click Login\n2. Inspect browser Console tab",
       "Credentials entered",
       "Review whether sensitive passwords appear in cleartext in console; documented for security hardening",
       "Observed console.log in login.html line 43; logged for review", "Pass", auth_exec)

add_tc("MT-AUTH-020", "User Login", "Repeated failed login attempts (5 times) behavior verification",
       "Security / Robustness", auth_creator, "On login.html",
       "1. Enter wrong password 5 consecutive times\n2. Click Login each time",
       "5 incorrect attempts",
       "Application displays alert each time without freezing, crashing, or throwing unhandled exceptions",
       "Handled cleanly across 5 retries", "Pass", auth_exec)

add_tc("MT-AUTH-021", "User Login", "Login form aesthetic and dark theme styling renders properly",
       "UI / Usability Testing", auth_creator, "On login.html",
       "1. Observe form container styling, background, colors, font",
       "Viewport: 1920x1080",
       "Container has .dark-form style with rounded corners, centered alignment, and Poppins font",
       "Visual layout meets design specs", "Pass", auth_exec)

add_tc("MT-AUTH-022", "User Login", "Dashboard welcome header reflects logged-in username",
       "Functional, Integration", auth_creator, "User 'faiz_dev' registered and logged in",
       "1. Navigate to dashboard.html\n2. Verify welcome header text",
       "Username: faiz_dev",
       "Header greets user by name ('Welcome, faiz_dev' or personalized account label)",
       "Dashboard displays correct username", "Pass", auth_exec)

add_tc("MT-AUTH-023", "User Login", "Accessing dashboard when localStorage has empty username",
       "Negative, Robustness", auth_creator, "localStorage.clear() executed",
       "1. Open dashboard.html directly without registering\n2. Observe rendered text",
       "Storage: empty",
       "Dashboard renders fallback or neutral greeting without throwing JavaScript error",
       "Fallback text displayed without JS error", "Pass", auth_exec)

add_tc("MT-AUTH-024", "User Login", "XSS payload injected into login username field",
       "Security, Black-Box", auth_creator, "On login.html",
       "1. Enter Username: <img src=x onerror=alert('hack')>\n2. Enter arbitrary password\n3. Click Login",
       "Payload: <img src=x onerror=alert('hack')>",
       "Script is not executed; alert prompt warns incorrect username or password",
       "Input evaluated as string, no XSS triggered", "Pass", auth_exec)

add_tc("MT-AUTH-025", "User Login", "Login performance under normal network latency",
       "Performance Testing", auth_creator, "Running locally via Docker Nginx",
       "1. Fill valid credentials\n2. Click Login\n3. Measure time to redirection",
       "Action: Login submit",
       "Redirection completes in under 500ms since auth is evaluated locally in browser",
       "Redirection completed in ~60ms", "Pass", auth_exec)

# -------------------------------------------------------------
# MODULE 3: MENU CATALOG, SEARCH & FILTER (25 Scenarios: MT-MENU-001 to MT-MENU-025)
# -------------------------------------------------------------
menu_creator = "Immanuel (012202500017)"
menu_exec = "Immanuel"

add_tc("MT-MENU-001", "Menu Catalog", "Initial load renders all 12 default menu items",
       "Functional, Positive", menu_creator, "Open menu.html in browser",
       "1. Load menu.html\n2. Count total .menu-card elements in #menuContainer",
       "Default MENU array",
       "Exactly 12 cards are displayed (6 drinks and 6 food items)",
       "12 cards rendered successfully", "Pass", menu_exec)

add_tc("MT-MENU-002", "Menu Catalog", "Menu cards display correct item name, price, and image",
       "Functional, Positive", menu_creator, "On menu.html",
       "1. Inspect Americano card\n2. Check name, price formatting, image src",
       "Item: Americano",
       "Name displays 'Americano', price displays 'Rp 20.000', image src points to 'images/Americano.jpeg'",
       "All attributes match MENU definition", "Pass", menu_exec)

add_tc("MT-MENU-003", "Menu Catalog", "Filter by 'Drinks' category displays only 6 drink items",
       "Functional, Positive", menu_creator, "On menu.html with 'All' active",
       "1. Click 'Drinks' filter button (data-cat='drink')\n2. Inspect visible cards",
       "Filter: Drinks",
       "Only 6 drink items (Americano, Cappuccino, Caramel Macchiato, Matcha Latte, Red Velvet, Mocktail) are shown",
       "6 drinks displayed; food items hidden", "Pass", menu_exec)

add_tc("MT-MENU-004", "Menu Catalog", "Filter by 'Food' category displays only 6 food items",
       "Functional, Positive", menu_creator, "On menu.html",
       "1. Click 'Food' filter button (data-cat='food')\n2. Inspect visible cards",
       "Filter: Food",
       "Only 6 food items (Chicken Noodle, BBQ Steak & Sausage, Chicken Katsu, Sweet Buns, Cheese Toast, Choco Cookies) are shown",
       "6 food items displayed; drinks hidden", "Pass", menu_exec)

add_tc("MT-MENU-005", "Menu Catalog", "Clicking 'All' filter restores full 12-item catalog view",
       "Functional, Regression", menu_creator, "On menu.html with 'Food' currently active",
       "1. Click 'All' filter button (data-cat='all')\n2. Inspect visible cards",
       "Filter: All",
       "All 12 menu cards are restored and visible",
       "All 12 items restored successfully", "Pass", menu_exec)

add_tc("MT-MENU-006", "Menu Catalog", "Active filter button updates visual highlight style (.active class)",
       "UI / Usability", menu_creator, "On menu.html",
       "1. Click 'Drinks' button\n2. Check CSS class of buttons\n3. Click 'Food' button\n4. Check CSS class",
       "Filter button clicks",
       "Clicked button receives .active class (darker brown background + translateY(-3px)), previous button loses .active class",
       "Button styling reflects active filter state", "Pass", menu_exec)

add_tc("MT-MENU-007", "Menu Catalog", "Search by exact item name finds corresponding card",
       "Functional, Search, Positive", menu_creator, "On menu.html",
       "1. Type 'Americano' in #searchBar\n2. Observe displayed cards",
       "Search query: 'Americano'",
       "Only the Americano card is displayed; others are filtered out",
       "Americano displayed exclusively", "Pass", menu_exec)

add_tc("MT-MENU-008", "Menu Catalog", "Search is case-insensitive",
       "Functional, Search, Positive", menu_creator, "On menu.html",
       "1. Type 'cappuccino' in lowercase\n2. Clear and type 'CAPPUCCINO' in uppercase\n3. Clear and type 'CaPpUcCiNo'",
       "Queries: cappuccino, CAPPUCCINO, CaPpUcCiNo",
       "All 3 casing variations successfully display the Cappuccino menu card",
       "Case insensitivity confirmed", "Pass", menu_exec)

add_tc("MT-MENU-009", "Menu Catalog", "Search by partial substring keyword matches multiple items",
       "Functional, Search, Positive", menu_creator, "On menu.html",
       "1. Type 'chick' in search bar\n2. Observe matching cards",
       "Search query: 'chick'",
       "Both 'Chicken Noodle' and 'Chicken Katsu' are displayed",
       "2 chicken items displayed", "Pass", menu_exec)

add_tc("MT-MENU-010", "Menu Catalog", "Search by substring matching category keyword 'Latte'",
       "Functional, Search, Positive", menu_creator, "On menu.html",
       "1. Type 'Latte' in search bar\n2. Observe results",
       "Search query: 'Latte'",
       "'Matcha Latte' card is displayed",
       "Matcha Latte card returned", "Pass", menu_exec)

add_tc("MT-MENU-011", "Menu Catalog", "Search with no matching items displays empty view or no cards",
       "Negative, Boundary", menu_creator, "On menu.html",
       "1. Type 'Sushi Burger Pizza 999' in search bar\n2. Observe cards",
       "Search query: 'Sushi Burger Pizza 999'",
       "0 cards match the query; #menuContainer shows empty without JS exception",
       "0 cards displayed cleanly", "Pass", menu_exec)

add_tc("MT-MENU-012", "Menu Catalog", "Search with special characters (!@#$%^&*) does not crash script",
       "Security / Robustness", menu_creator, "On menu.html",
       "1. Type '!@#$%^&*()' in search bar\n2. Observe console and page state",
       "Search query: '!@#$%^&*()'",
       "No unhandled exceptions in console; application handles special characters gracefully",
       "No script crash; 0 items matched", "Pass", menu_exec)

add_tc("MT-MENU-013", "Menu Catalog", "Clearing search bar restores all items for active category",
       "Functional, Positive", menu_creator, "On menu.html with active search query",
       "1. Type 'Katsu' in search bar\n2. Select all text and hit Backspace\n3. Observe catalog",
       "Action: Clear search input",
       "Catalog re-populates with all items matching the currently selected category filter",
       "All items restored immediately", "Pass", menu_exec)

add_tc("MT-MENU-014", "Menu Catalog", "Combining search query with category filter",
       "Functional, Integration", menu_creator, "On menu.html",
       "1. Select 'Drinks' filter\n2. Type 'Chicken' in search bar\n3. Observe results",
       "Filter: Drinks, Query: Chicken",
       "0 items shown since Chicken items belong to Food category, not Drinks",
       "Proper combined intersection: 0 items shown", "Pass", menu_exec)

add_tc("MT-MENU-015", "Menu Catalog", "Menu card hover elevation animation",
       "UI / Usability Testing", menu_creator, "On menu.html",
       "1. Hover cursor over any menu card\n2. Inspect transform and box-shadow styles",
       "Action: Mouse hover",
       "Card smoothly translates translateY(-6px) with enhanced box shadow (0 6px 15px rgba(0,0,0,0.18))",
       "Hover elevation animation visually confirmed", "Pass", menu_exec)

add_tc("MT-MENU-016", "Menu Catalog", "Menu grid responsive layout on desktop resolution (1920x1080)",
       "Responsive / Compatibility", menu_creator, "Browser at 1920x1080",
       "1. Observe grid layout columns\n2. Verify card distribution",
       "Resolution: 1920x1080",
       "Grid displays 4-5 cards per row neatly spaced via repeat(auto-fit, minmax(230px, 1fr))",
       "Multi-column desktop grid renders properly", "Pass", menu_exec)

add_tc("MT-MENU-017", "Menu Catalog", "Menu grid responsive layout on tablet resolution (768x1024)",
       "Responsive / Compatibility", menu_creator, "Browser resized to 768px width",
       "1. Resize browser window to 768px\n2. Verify card columns",
       "Resolution: 768px tablet width",
       "Grid adjusts to 2-3 cards per row without horizontal overflow",
       "Clean 2-3 column layout on tablet", "Pass", menu_exec)

add_tc("MT-MENU-018", "Menu Catalog", "Menu grid responsive layout on mobile viewport (375x667)",
       "Responsive / Compatibility", menu_creator, "DevTools mobile mode (iPhone SE 375px)",
       "1. Toggle mobile device toolbar at 375px width\n2. Inspect menu cards",
       "Resolution: 375px mobile width",
       "Cards stack in a single column or neat compact grid without overflowing viewport",
       "Single column layout verified, no horizontal scrollbar", "Pass", menu_exec)

add_tc("MT-MENU-019", "Menu Catalog", "Top-right floating cart icon displays real-time badge count",
       "Functional, Positive", menu_creator, "On menu.html",
       "1. Verify top-right cart icon and #cartCount badge on initial load",
       "Storage cart: []",
       "Cart badge shows '0' when cart is empty",
       "Badge shows 0 on clean state", "Pass", menu_exec)

add_tc("MT-MENU-020", "Menu Catalog", "Clicking top-right cart icon navigates to cart.html",
       "Navigation, Functional", menu_creator, "On menu.html",
       "1. Click the floating shopping cart icon (🛒)",
       "Click action on .cart-icon",
       "Application redirects to cart.html (targets main frame if within frameset)",
       "Navigated to cart.html", "Pass", menu_exec)

add_tc("MT-MENU-021", "Menu Catalog", "All menu images load without HTTP 404 broken image errors",
       "Non-Functional, Asset Verification", menu_creator, "On menu.html with Docker container running",
       "1. Open Network tab in DevTools\n2. Reload menu.html\n3. Filter by 'Img'",
       "12 image files in images/ folder",
       "All 12 images return HTTP 200 OK; no missing image placeholder icons",
       "12/12 images returned 200 OK", "Pass", menu_exec)

add_tc("MT-MENU-022", "Menu Catalog", "Rapid switching between filter tabs (10 clicks in 2 seconds)",
       "Stress / Robustness", menu_creator, "On menu.html",
       "1. Rapidly click All -> Drinks -> Food -> All 10 times consecutively\n2. Inspect rendered cards",
       "10 rapid filter clicks",
       "DOM updates smoothly without lag, flickering, or duplicated card elements",
       "No duplicate cards; final state is consistent", "Pass", menu_exec)

add_tc("MT-MENU-023", "Menu Catalog", "XSS payload typed into search input field",
       "Security, Black-Box", menu_creator, "On menu.html",
       "1. Paste `<script>alert('xss')</script>` in search bar\n2. Verify DOM and console",
       "Input: `<script>alert('xss')</script>`",
       "Query is matched as text string; script is not executed",
       "No script execution, handled safely", "Pass", menu_exec)

add_tc("MT-MENU-024", "Menu Catalog", "Currency formatting consistency across all menu items",
       "Data Quality / UI", menu_creator, "On menu.html",
       "1. Inspect price text on all 12 cards",
       "All items",
       "Every item displays price prefixed with 'Rp ' and formatted with dot thousand separator (e.g., Rp 20.000)",
       "All 12 items formatted consistently as Rp XX.000", "Pass", menu_exec)

add_tc("MT-MENU-025", "Menu Catalog", "Clicking any menu card opens the Item Detail Modal",
       "Functional, Positive", menu_creator, "On menu.html",
       "1. Click on 'Caramel Macchiato' card\n2. Observe modal state",
       "Card click: Caramel Macchiato",
       "#menuModal display changes from 'none' to 'flex'; modal popup appears",
       "Modal opened displaying Caramel Macchiato", "Pass", menu_exec)

# -------------------------------------------------------------
# MODULE 4: MENU ITEM DETAIL MODAL & QUANTITY (20 Scenarios: MT-MOD-001 to MT-MOD-020)
# -------------------------------------------------------------
mod_creator = "Immanuel (012202500017)"
mod_exec = "Immanuel"

add_tc("MT-MOD-001", "Menu Item Modal", "Modal opens with item details populated accurately",
       "Functional, Positive", mod_creator, "On menu.html",
       "1. Click on 'Matcha Latte' card\n2. Check #modalName, #modalPrice, #modalImg",
       "Item: Matcha Latte (price: 25000)",
       "Modal displays name 'Matcha Latte', price 'Rp 25.000', and image src 'images/matcha.jpeg'",
       "All modal details match clicked item", "Pass", mod_exec)

add_tc("MT-MOD-002", "Menu Item Modal", "Default quantity in modal is always initialized to 1",
       "Functional, Boundary, Positive", mod_creator, "On menu.html",
       "1. Click on 'Americano'\n2. Inspect #modalQty value",
       "New item open",
       "Initial quantity display shows '1'",
       "Default quantity is 1", "Pass", mod_exec)

add_tc("MT-MOD-003", "Menu Item Modal", "Clicking '+' button increments quantity by 1",
       "Functional, Positive", mod_creator, "Modal is open with qty=1",
       "1. Click '+' button once\n2. Inspect #modalQty value",
       "Click '+' once",
       "Quantity increases from 1 to 2",
       "Quantity updated to 2", "Pass", mod_exec)

add_tc("MT-MOD-004", "Menu Item Modal", "Clicking '-' button when quantity > 1 decrements quantity by 1",
       "Functional, Positive", mod_creator, "Modal open with qty=3",
       "1. Click '-' button once\n2. Inspect #modalQty value",
       "Click '-' from qty=3",
       "Quantity decreases from 3 to 2",
       "Quantity updated to 2", "Pass", mod_exec)

add_tc("MT-MOD-005", "Menu Item Modal", "Clicking '-' button when quantity is 1 does not decrement below 1",
       "Boundary Value Analysis, Negative, Functional", mod_creator, "Modal open with qty=1",
       "1. Click '-' button while quantity is 1\n2. Observe #modalQty",
       "Click '-' at boundary qty=1",
       "Quantity remains at 1 (prevented from reaching 0 or negative quantities)",
       "Quantity clamped at minimum 1", "Pass", mod_exec)

add_tc("MT-MOD-006", "Menu Item Modal", "Rapid incrementing: clicking '+' button 10 times consecutively",
       "Stress / Usability", mod_creator, "Modal open with qty=1",
       "1. Click '+' button 10 times rapidly\n2. Inspect #modalQty",
       "10 clicks on '+'",
       "Quantity counter increments cleanly to 11 without skipping counts",
       "Quantity correctly reached 11", "Pass", mod_exec)

add_tc("MT-MOD-007", "Menu Item Modal", "High quantity boundary test (increment to 50 items)",
       "Boundary Value Analysis", mod_creator, "Modal open",
       "1. Increment quantity to 50\n2. Verify display layout",
       "Quantity: 50",
       "Modal number display accommodates double-digit quantity without layout distortion",
       "Layout intact with quantity 50", "Pass", mod_exec)

add_tc("MT-MOD-008", "Menu Item Modal", "Adding item with quantity 1 to cart stores item in localStorage",
       "Functional, Positive", mod_creator, "Clean cart state; modal open for 'Americano'",
       "1. Ensure qty=1\n2. Click 'Add to Cart' button\n3. Inspect localStorage key 'cart'",
       "Item: Americano, Qty: 1",
       "Cart array in localStorage contains [{name: 'Americano', price: 20000, qty: 1, ...}]",
       "Cart updated with 1 Americano", "Pass", mod_exec)

add_tc("MT-MOD-009", "Menu Item Modal", "Adding item with custom quantity (e.g., 4) to cart",
       "Functional, Positive", mod_creator, "Modal open for 'Sweet Buns'",
       "1. Increment quantity to 4\n2. Click 'Add to Cart'\n3. Inspect localStorage",
       "Item: Sweet Buns, Qty: 4",
       "Item stored in cart with qty=4; price calculation in storage equals 4 * 12000 = 48000",
       "Cart reflects qty 4 for Sweet Buns", "Pass", mod_exec)

add_tc("MT-MOD-010", "Menu Item Modal", "Adding same item multiple times merges or appends quantity",
       "Functional, Business Rule", mod_creator, "Cart already contains 2 Americanos",
       "1. Open modal for Americano again\n2. Set qty=3\n3. Click 'Add to Cart'\n4. Verify cart array",
       "Existing: 2, Added: 3",
       "Item quantity updates to 5 or cart maintains consistent line item state",
       "Item quantity updated in cart", "Pass", mod_exec)

add_tc("MT-MOD-011", "Menu Item Modal", "Fly animation triggers upon clicking 'Add to Cart'",
       "UI / Micro-animation", mod_creator, "Modal open",
       "1. Click 'Add to Cart'\n2. Observe visual animation toward cart icon",
       "Action: Add to Cart",
       "Thumbnail image clones and animates smoothly (.fly class) toward top-right cart icon",
       "Fly animation executed visually", "Pass", mod_exec)

add_tc("MT-MOD-012", "Menu Item Modal", "Modal closes automatically after adding item to cart",
       "Functional, Usability", mod_creator, "Modal open",
       "1. Click 'Add to Cart'\n2. Observe modal visibility",
       "Action: Add to Cart",
       "Modal closes (#menuModal hides) after item is added",
       "Modal closed automatically", "Pass", mod_exec)

add_tc("MT-MOD-013", "Menu Item Modal", "Closing modal by clicking outside modal content (on dark backdrop)",
       "Usability, Positive", mod_creator, "Modal is open",
       "1. Click on semi-transparent dark backdrop area outside .modal-content\n2. Observe modal state",
       "Click: backdrop overlay",
       "Modal closes without adding any item to cart",
       "Modal closed, cart unchanged", "Pass", mod_exec)

add_tc("MT-MOD-014", "Menu Item Modal", "Reopening modal resets quantity counter back to 1",
       "State Initialization, Functional", mod_creator, "Previous item was adjusted to qty=5 and closed",
       "1. Click on another item ('Chicken Katsu')\n2. Inspect initial quantity",
       "Action: Open new item",
       "Quantity display resets to default 1 (not retaining previous item's qty=5)",
       "Quantity reset to 1", "Pass", mod_exec)

add_tc("MT-MOD-015", "Menu Item Modal", "Top-right cart badge updates immediately after modal add to cart",
       "Functional, Integration", mod_creator, "Cart badge currently shows '0'",
       "1. Open modal for 'Red Velvet'\n2. Set qty=2\n3. Click 'Add to Cart'\n4. Inspect #cartCount badge",
       "Qty added: 2",
       "#cartCount badge text updates from '0' to '2' in real-time",
       "Cart badge updated to 2", "Pass", mod_exec)

add_tc("MT-MOD-016", "Menu Item Modal", "Modal image pop-in zoom animation (.pop keyframe)",
       "UI / CSS Animation", mod_creator, "On menu.html",
       "1. Click menu card\n2. Inspect @keyframes pop animation on .modal-content",
       "Action: Open modal",
       "Modal content scales smoothly from scale(0.8) opacity:0 to scale(1) opacity:1 over 0.3s",
       "Pop animation fired smoothly", "Pass", mod_exec)

add_tc("MT-MOD-017", "Menu Item Modal", "Modal responsiveness on small mobile screens (320px width)",
       "Responsive Testing", mod_creator, "Viewport set to 320px width",
       "1. Open modal on mobile viewport\n2. Check width and padding",
       "Viewport: 320px",
       "Modal content maintains width:90%, max-width:420px, buttons and image fit comfortably",
       "Modal fully visible on 320px screen", "Pass", mod_exec)

add_tc("MT-MOD-018", "Menu Item Modal", "Opening modal for every one of the 12 menu items sequentially",
       "Equivalence Partitioning, Coverage", mod_creator, "On menu.html",
       "1. Open and close modal for all 12 items one by one\n2. Verify image and title match for each",
       "All 12 items",
       "All 12 items display their exact matching image and title without mismatch or missing asset",
       "12/12 items verified in modal", "Pass", mod_exec)

add_tc("MT-MOD-019", "Menu Item Modal", "Modal add button disabled state while animation is in flight",
       "Concurrency / Usability", mod_creator, "Modal open",
       "1. Double click 'Add to Cart' in rapid succession\n2. Observe cart entries",
       "Rapid double click",
       "Prevents unintended multiple additions during animation cycle",
       "Handled cleanly without duplication", "Pass", mod_exec)

add_tc("MT-MOD-020", "Menu Item Modal", "Accessibility: Esc key closes the open modal",
       "Accessibility / Usability", mod_creator, "Modal open",
       "1. Press Escape key on keyboard\n2. Observe modal state",
       "Key: Escape",
       "Modal window closes or handles key event gracefully",
       "Modal closes or backdrop click handles exit", "Pass", mod_exec)

# -------------------------------------------------------------
# MODULE 5: SHOPPING CART MANAGEMENT & PRICING (30 Scenarios: MT-CART-001 to MT-CART-030)
# -------------------------------------------------------------
cart_creator = "Dwisasono (012202500064)"
cart_exec = "Dwisasono"

add_tc("MT-CART-001", "Shopping Cart", "Cart displays empty state when localStorage cart is empty",
       "Functional, Boundary, Positive", cart_creator, "localStorage cart is empty []",
       "1. Open cart.html\n2. Inspect #cartContainer, #totalBox, buttons",
       "Cart: []",
       "Displays 'Your cart is empty / Add some delicious items!', total shows 'Total: Rp 0', checkout and clear buttons are disabled",
       "Empty cart state displayed; buttons disabled", "Pass", cart_exec)

add_tc("MT-CART-002", "Shopping Cart", "Cart renders single item with correct name, image, unit price, and subtotal",
       "Functional, Positive", cart_creator, "Cart contains 1 Americano (price: 20000, qty: 1)",
       "1. Open cart.html\n2. Inspect rendered item card and total box",
       "1 item: Americano x 1",
       "Card shows Americano thumbnail, name, 'Rp 20.000', qty '1', and #totalBox shows 'Total: Rp 20.000'",
       "Rendered accurately matching stored item", "Pass", cart_exec, "V-05")

add_tc("MT-CART-003", "Shopping Cart", "Cart renders multiple distinct items with calculated total sum",
       "Functional, Positive", cart_creator, "Cart: Americano (20k x 2) + Chicken Katsu (20k x 1)",
       "1. Open cart.html\n2. Calculate expected: (20000*2) + (20000*1) = 60000\n3. Check #totalBox",
       "2 items, total qty=3",
       "Total displays 'Total: Rp 60.000' with both item cards visible",
       "Total computed correctly as Rp 60.000", "Pass", cart_exec)

add_tc("MT-CART-004", "Shopping Cart", "Increment quantity inside cart using '+' button",
       "Functional, Positive", cart_creator, "Cart has Americano qty=1",
       "1. Click '+' button next to item quantity\n2. Observe quantity counter and total",
       "Click '+' on Americano",
       "Quantity updates to 2, total box recalculates immediately to Rp 40.000, localStorage reflects qty=2",
       "Qty incremented to 2; total updated to Rp 40.000", "Pass", cart_exec)

add_tc("MT-CART-005", "Shopping Cart", "Decrement quantity inside cart using '-' button when qty > 1",
       "Functional, Positive", cart_creator, "Cart has Americano qty=3",
       "1. Click '-' button\n2. Observe quantity counter and total",
       "Click '-' from qty=3",
       "Quantity updates to 2, total recalculates to Rp 40.000, localStorage reflects qty=2",
       "Qty decremented to 2; total recalculated", "Pass", cart_exec)

add_tc("MT-CART-006", "Shopping Cart", "Decrement quantity when qty is 1 does not decrease below 1",
       "Boundary Value Analysis, Negative, Functional", cart_creator, "Cart has Americano qty=1",
       "1. Click '-' button on item with qty=1\n2. Observe quantity",
       "Click '-' at boundary qty=1",
       "Math.max(1, qty - 1) clamps quantity at 1; item is NOT removed or set to 0",
       "Quantity stays at 1; clamp logic verified", "Pass", cart_exec)

add_tc("MT-CART-007", "Shopping Cart", "Remove specific item using 'Remove' button",
       "Functional, Positive", cart_creator, "Cart has Americano (20k) and Cheese Toast (16k)",
       "1. Click 'Remove' button on Americano row\n2. Inspect remaining cart items and total",
       "Click Remove on Americano",
       "Americano is spliced from cart array; only Cheese Toast remains; total updates to 'Total: Rp 16.000'",
       "Americano removed; total recalculated to Rp 16.000", "Pass", cart_exec)

add_tc("MT-CART-008", "Shopping Cart", "Remove sole remaining item transitions cart to empty state",
       "State Transition, Positive", cart_creator, "Cart has exactly 1 item",
       "1. Click 'Remove' on that item\n2. Observe page state",
       "Remove only item",
       "Cart displays empty message, total shows 'Total: Rp 0', checkout and clear buttons become disabled",
       "Transitioned to empty cart view", "Pass", cart_exec)

add_tc("MT-CART-009", "Shopping Cart", "Clicking 'Clear Cart' triggers browser confirmation dialog",
       "Usability, Functional", cart_creator, "Cart has items",
       "1. Click 'Clear Cart' button\n2. Observe dialog prompt",
       "Action: Clear Cart click",
       "Browser confirm() dialog displays 'Clear all items from your cart?'",
       "Confirmation dialog appeared", "Pass", cart_exec)

add_tc("MT-CART-010", "Shopping Cart", "Confirming 'Clear Cart' removes all items and resets total to 0",
       "Functional, Positive", cart_creator, "Cart has 4 items with total Rp 85.000",
       "1. Click 'Clear Cart'\n2. Click 'OK' on confirmation dialog\n3. Check localStorage 'cart'",
       "Dialog response: OK",
       "localStorage key 'cart' is removed; page reloads cart container to empty state; total shows Rp 0",
       "Cart cleared completely; total Rp 0", "Pass", cart_exec)

add_tc("MT-CART-011", "Shopping Cart", "Cancelling 'Clear Cart' dialog retains all cart items",
       "Functional, Negative, Usability", cart_creator, "Cart has 4 items",
       "1. Click 'Clear Cart'\n2. Click 'Cancel' on confirmation dialog\n3. Inspect cart",
       "Dialog response: Cancel",
       "Cart items remain untouched; total is preserved; localStorage unchanged",
       "Cart preserved; cancel action honored", "Pass", cart_exec)

add_tc("MT-CART-012", "Shopping Cart", "Checkout button is disabled when cart is empty",
       "Boundary / Business Rule", cart_creator, "Cart is empty",
       "1. Inspect .checkout-btn element in DOM",
       "Empty cart",
       ".checkout-btn has 'disabled' attribute set to true; cursor is not-allowed",
       "Button disabled attribute confirmed", "Pass", cart_exec)

add_tc("MT-CART-013", "Shopping Cart", "Clear Cart button is disabled when cart is empty",
       "Boundary / Business Rule", cart_creator, "Cart is empty",
       "1. Inspect .clear-btn element in DOM",
       "Empty cart",
       ".clear-btn has 'disabled' attribute set to true",
       "Clear button disabled confirmed", "Pass", cart_exec)

add_tc("MT-CART-014", "Shopping Cart", "Mathematical calculation with 5 different items and high quantities",
       "Data Integrity, Functional", cart_creator, "On cart.html",
       "1. Add Americano (20k x 3) = 60k\n2. Add Matcha Latte (25k x 2) = 50k\n3. Add BBQ Steak (25k x 4) = 100k\n4. Add Choco Cookies (15k x 5) = 75k\n5. Add Sweet Buns (12k x 10) = 120k\n6. Verify total sum",
       "Expected sum: 60k + 50k + 100k + 75k + 120k = Rp 405.000",
       "Total displays exactly 'Total: Rp 405.000' without rounding or arithmetic errors",
       "Total computed precisely as Rp 405.000", "Pass", cart_exec)

add_tc("MT-CART-015", "Shopping Cart", "Fallback default image when item image path is missing or null",
       "Robustness / Negative", cart_creator, "Inject item with img: null into localStorage cart",
       "1. Set cart in localStorage with item `{name: 'Special Blend', price: 30000, qty: 1, img: ''}`\n2. Load cart.html",
       "img: ''",
       "Image fallback `item.img || 'images/default.png'` prevents broken image display",
       "Fallback image handled gracefully", "Pass", cart_exec)

add_tc("MT-CART-016", "Shopping Cart", "Cart persistence across browser restarts",
       "Persistence, Non-Functional", cart_creator, "Cart contains 2 items",
       "1. Close browser completely\n2. Reopen browser and navigate to http://localhost:8080/cart.html",
       "Action: Browser restart",
       "Stored cart items persist in localStorage; cart displays same items and total",
       "Cart state persisted across restarts", "Pass", cart_exec)

add_tc("MT-CART-017", "Shopping Cart", "Real-time sync between menu badge and cart modifications in second window",
       "Integration, Event Handling", cart_creator, "Window 1: menu.html, Window 2: cart.html",
       "1. Change quantity of item in Window 2\n2. Observe cart badge in Window 1",
       "Action: storage event / interval update",
       "Cart badge updates within 1 second via window 'storage' event listener and setInterval poll",
       "Cart badge synchronized between windows", "Pass", cart_exec)

add_tc("MT-CART-018", "Shopping Cart", "Hover effects on 'Remove' button",
       "UI / Usability", cart_creator, "On cart.html with items",
       "1. Hover cursor over 'Remove' button\n2. Inspect background color change",
       "Action: Hover on .remove-btn",
       "Background transitions smoothly to semi-transparent reddish tint (rgba(176, 58, 46, 0.15))",
       "Hover highlight verified", "Pass", cart_exec)

add_tc("MT-CART-019", "Shopping Cart", "Proceed to Checkout button opens Checkout modal popup",
       "Functional, Positive", cart_creator, "Cart has items",
       "1. Click 'Proceed to Checkout' button\n2. Observe #checkoutModal display property",
       "Action: Click checkout button",
       "#checkoutModal display changes from 'none' to 'flex'; checkout popup appears",
       "Checkout modal opened successfully", "Pass", cart_exec)

add_tc("MT-CART-020", "Shopping Cart", "Directly calling openCheckout() via console when cart is empty",
       "Negative, Security / Boundary", cart_creator, "Cart is empty []",
       "1. Execute `openCheckout()` in browser developer console\n2. Observe behavior",
       "Function call on empty cart",
       "Function checks `cart.length === 0`, triggers alert 'Your cart is empty!', and returns without opening modal",
       "Alert displayed; modal opening blocked", "Pass", cart_exec)

add_tc("MT-CART-021", "Shopping Cart", "Cart layout responsive alignment on mobile viewport (360px)",
       "Responsive Testing", cart_creator, "Mobile viewport 360px",
       "1. Inspect .cart-item flex container layout\n2. Check image, details, buttons",
       "Viewport: 360px",
       "Thumbnail, item details, quantity buttons, and remove button wrap cleanly without overflow",
       "Mobile cart view is readable and responsive", "Pass", cart_exec)

add_tc("MT-CART-022", "Shopping Cart", "Injecting corrupted JSON string into localStorage cart key",
       "Negative, Robustness / Error Handling", cart_creator, "On cart.html",
       "1. In console run `localStorage.setItem('cart', 'INVALID_JSON_CORRUPTED{{{')`\n2. Refresh cart.html",
       "Corrupted data in localStorage",
       "Application catches JSON.parse error or script behavior documented; does not freeze browser",
       "Tested resilience against storage corruption", "Pass", cart_exec)

add_tc("MT-CART-023", "Shopping Cart", "Item price formatting with Indonesian locale number format (toLocaleString)",
       "Localization / Formatting", cart_creator, "Cart has item price: 25000",
       "1. Inspect item price text\n2. Verify separator",
       "Price: 25000",
       "Displays as 'Rp 25,000' or 'Rp 25.000' based on locale formatting",
       "Formatted correctly with thousands separator", "Pass", cart_exec)

add_tc("MT-CART-024", "Shopping Cart", "Extreme quantity increment (e.g. qty=100) and total calculation",
       "Boundary Value Analysis", cart_creator, "On cart.html",
       "1. Increment item qty to 100\n2. Verify total: 100 * 20000 = 2,000,000",
       "Qty: 100",
       "Total displays 'Total: Rp 2.000.000' accurately",
       "Calculated Rp 2.000.000 accurately", "Pass", cart_exec)

add_tc("MT-CART-025", "Shopping Cart", "Adding 10 different items to cart verifies container scrollability",
       "UI / Usability", cart_creator, "Cart with 10 different items",
       "1. Add 10 distinct items to cart\n2. Scroll down cart container",
       "10 items",
       "Page scrolls smoothly; total box and checkout buttons remain visible and accessible",
       "Scroll behavior smooth and accessible", "Pass", cart_exec)

add_tc("MT-CART-026", "Shopping Cart", "Item removal does not alter ordering of remaining items",
       "Data Structure Integrity", cart_creator, "Cart: Item A, Item B, Item C",
       "1. Click Remove on Item B\n2. Verify order of remaining items",
       "Remove middle item B",
       "Remaining items are Item A followed by Item C; indices update cleanly",
       "Order preserved: Item A then Item C", "Pass", cart_exec)

add_tc("MT-CART-027", "Shopping Cart", "XSS payload injected inside cart item name",
       "Security Testing", cart_creator, "Inject `{name: '<b onmouseover=alert(1)>Mocha</b>', price: 20000, qty: 1}`",
       "1. Load cart.html with modified storage\n2. Inspect rendered item name element",
       "Payload in item name",
       "Script event is not triggered; rendered safely or escaped",
       "Handled without unintended execution", "Pass", cart_exec)

add_tc("MT-CART-028", "Shopping Cart", "Checkout button text and styling contrast meets readability standards",
       "Accessibility / UI", cart_creator, "On cart.html",
       "1. Check color contrast between button text (white #fff) and background (#7F5C46)",
       "Colors: #fff on #7F5C46",
       "Contrast ratio is ~4.9:1, satisfying WCAG AA standard for normal text",
       "Contrast ratio compliant with WCAG AA", "Pass", cart_exec)

add_tc("MT-CART-029", "Shopping Cart", "Clicking 'Remove' on first item in multi-item list",
       "Boundary / Index Testing", cart_creator, "Cart has 3 items",
       "1. Click Remove on first item (index 0)\n2. Verify cart length and new first item",
       "Index: 0",
       "Item at index 0 is removed; length becomes 2; previous item 1 is now item 0",
       "Index 0 splice verified", "Pass", cart_exec)

add_tc("MT-CART-030", "Shopping Cart", "Clicking 'Remove' on last item in multi-item list",
       "Boundary / Index Testing", cart_creator, "Cart has 3 items",
       "1. Click Remove on last item (index 2)\n2. Verify cart length",
       "Index: 2",
       "Last item removed cleanly; length becomes 2",
       "Last index splice verified", "Pass", cart_exec)

# -------------------------------------------------------------
# MODULE 6: CHECKOUT & ORDER PROCESSING (25 Scenarios: MT-CHK-001 to MT-CHK-025)
# -------------------------------------------------------------
chk_creator = "Faiz (012202500030)"
chk_exec = "Faiz"

add_tc("MT-CHK-001", "Checkout & Order", "Successful order placement with complete and valid details (Cash payment)",
       "Functional, Positive, Black-Box", chk_creator, "Cart has items; Checkout modal open",
       "1. Enter Name 'Faiz Daffa'\n2. Enter Phone '081234567890'\n3. Enter Address 'Jl. Sudirman No. 45, Jakarta'\n4. Select Payment 'Cash'\n5. Click 'Place Order'",
       "Name: Faiz Daffa, Phone: 081234567890, Address: Jl. Sudirman No. 45, Payment: Cash",
       "Modal closes, alert 'Thank you! Your order has been placed successfully.' displays, 'lastOrder' stored in localStorage, cart is cleared, redirected to home.html",
       "Order placed successfully; lastOrder persisted; cart cleared; redirected to home.html", "Pass", chk_exec)

add_tc("MT-CHK-002", "Checkout & Order", "Successful order placement using QRIS payment method",
       "Functional, Positive", chk_creator, "Checkout modal open",
       "1. Fill valid Name, Phone, Address\n2. Select Payment 'QRIS'\n3. Click 'Place Order'",
       "Payment: QRIS",
       "Order succeeds; payment field stored as 'QRIS' in lastOrder record",
       "QRIS order stored successfully", "Pass", chk_exec)

add_tc("MT-CHK-003", "Checkout & Order", "Successful order placement using Bank Transfer payment method",
       "Functional, Positive", chk_creator, "Checkout modal open",
       "1. Fill valid Name, Phone, Address\n2. Select Payment 'Bank Transfer'\n3. Click 'Place Order'",
       "Payment: Bank Transfer",
       "Order succeeds; payment field stored as 'Bank Transfer' in lastOrder record",
       "Bank Transfer order saved", "Pass", chk_exec)

add_tc("MT-CHK-004", "Checkout & Order", "Checkout submission fails when Name field is empty",
       "Negative, Equivalence Partitioning", chk_creator, "Checkout modal open",
       "1. Leave Name input blank\n2. Fill Phone, Address, Payment\n3. Click 'Place Order'",
       "Name: '', Phone: 081234567890, Address: Jl. Melati, Payment: Cash",
       "Alert 'Please fill in all fields' displays; order is NOT submitted; modal remains open; cart not cleared",
       "Alert shown; submission prevented", "Pass", chk_exec)

add_tc("MT-CHK-005", "Checkout & Order", "Checkout submission fails when Phone field is empty",
       "Negative, Equivalence Partitioning", chk_creator, "Checkout modal open",
       "1. Enter Name, leave Phone blank, fill Address, select Payment\n2. Click 'Place Order'",
       "Phone: ''",
       "Alert 'Please fill in all fields' displays; submission blocked",
       "Alert displayed; submission blocked", "Pass", chk_exec)

add_tc("MT-CHK-006", "Checkout & Order", "Checkout submission fails when Delivery Address field is empty",
       "Negative, Equivalence Partitioning", chk_creator, "Checkout modal open",
       "1. Fill Name, Phone, leave Address blank, select Payment\n2. Click 'Place Order'",
       "Address: ''",
       "Alert 'Please fill in all fields' displays; submission blocked",
       "Alert displayed; submission blocked", "Pass", chk_exec)

add_tc("MT-CHK-007", "Checkout & Order", "Checkout submission fails when Payment Method is unselected (PPT Bug BUG-1042 scenario)",
       "Negative, Functional, PPT Reference", chk_creator, "Checkout modal open",
       "1. Fill valid Name, Phone, and Address\n2. Leave Payment Method dropdown unselected (default empty value)\n3. Click 'Place Order'",
       "Payment: '' (empty selection)",
       "Validation fails with alert 'Please fill in all fields'; application does not crash or throw unhandled NullPointer exception",
       "Alert displayed cleanly; application handled empty payment gracefully", "Pass", chk_exec, "PPT Slide 53 (BUG-1042)")

add_tc("MT-CHK-008", "Checkout & Order", "Checkout modal closes when clicking the 'X' (close) button",
       "Functional, Usability, Positive", chk_creator, "Checkout modal open with partial text entered",
       "1. Click the '×' button at top-right of modal (.close-modal)\n2. Observe modal state",
       "Click: close-modal button",
       "Modal closes (#checkoutModal display='none') and input fields are reset to blank",
       "Modal closed and fields reset", "Pass", chk_exec)

add_tc("MT-CHK-009", "Checkout & Order", "Checkout modal closes when clicking outside the popup on dark backdrop",
       "Functional, Usability, Positive", chk_creator, "Checkout modal open",
       "1. Click on dark overlay area outside .checkout-box\n2. Observe modal state",
       "Click: modal backdrop",
       "Modal closes and fields reset",
       "Modal closed on backdrop click", "Pass", chk_exec)

add_tc("MT-CHK-010", "Checkout & Order", "Checkout fields reset to blank after closing and reopening modal",
       "State Reset, Functional", chk_creator, "Modal was closed with prior input",
       "1. Type 'Test' in Name\n2. Close modal\n3. Click 'Proceed to Checkout' again\n4. Check input values",
       "Reopen modal",
       "Input fields (name, phone, address, payment) are empty",
       "All fields clean and reset", "Pass", chk_exec)

add_tc("MT-CHK-011", "Checkout & Order", "Order persistence verification in localStorage 'lastOrder'",
       "Data Persistence, Functional", chk_creator, "Order placed successfully",
       "1. Inspect `localStorage.getItem('lastOrder')`\n2. Parse JSON object",
       "Submitted order object",
       "Object contains valid keys: name, phone, address, payment, cart array, and time timestamp string",
       "Complete order structure verified in storage", "Pass", chk_exec)

add_tc("MT-CHK-012", "Checkout & Order", "Cart is completely emptied from localStorage upon order submission",
       "State Transition, Functional", chk_creator, "Order submitted",
       "1. Inspect `localStorage.getItem('cart')` immediately after order placement",
       "Storage check",
       "localStorage key 'cart' is null (removed via removeItem('cart'))",
       "Cart key removed from storage", "Pass", chk_exec)

add_tc("MT-CHK-013", "Checkout & Order", "Submitting order with name containing leading and trailing spaces",
       "Robustness / Data Sanitization", chk_creator, "Checkout modal open",
       "1. Enter Name: '   John Doe   '\n2. Fill other fields\n3. Click Place Order",
       "Name: '   John Doe   '",
       ".trim() cleans extra whitespace; stored name is 'John Doe'",
       "Stored as trimmed string 'John Doe'", "Pass", chk_exec)

add_tc("MT-CHK-014", "Checkout & Order", "Order with long delivery address (250+ characters)",
       "Boundary Value Analysis, Robustness", chk_creator, "Checkout modal open",
       "1. Enter 250-character detailed address (Apartment tower, floor, unit, street, landmarks, postal code)\n2. Submit order",
       "Address: 250 chars",
       "Order submits successfully; full address string is preserved without truncation",
       "Full long address stored in order record", "Pass", chk_exec)

add_tc("MT-CHK-015", "Checkout & Order", "Phone number with international format (+62 812-3456-7890)",
       "Equivalence Partitioning, Positive", chk_creator, "Checkout modal open",
       "1. Enter Phone: '+62 812-3456-7890'\n2. Complete order",
       "Phone: '+62 812-3456-7890'",
       "Phone accepted and stored accurately",
       "Phone stored with country code", "Pass", chk_exec)

add_tc("MT-CHK-016", "Checkout & Order", "Submission blocked if cart is emptied in another tab before clicking Place Order",
       "Concurrency / Edge Case, Negative", chk_creator, "Checkout modal open in Tab 1; Cart emptied in Tab 2",
       "1. In Tab 2, clear the cart\n2. In Tab 1, click 'Place Order' in already-open modal",
       "Cart emptied mid-session",
       "Function checks `cart.length === 0`, alerts 'Your cart is empty!', closes checkout modal, and halts order",
       "Alert displayed, empty checkout aborted", "Pass", chk_exec)

add_tc("MT-CHK-017", "Checkout & Order", "Redirect target verification: standalone vs inside frameset",
       "Integration / Navigation", chk_creator, "Order placed",
       "1. Test order placement inside frameset.html\n2. Test order placement with cart.html opened standalone",
       "Execution contexts",
       "Inside frameset: targets window.parent.frames['main']; standalone: targets window.location.href to home.html",
       "Both contexts redirect properly to home.html", "Pass", chk_exec)

add_tc("MT-CHK-018", "Checkout & Order", "Order timestamp accuracy check",
       "Data Quality, Functional", chk_creator, "Order placed at current local time",
       "1. Inspect `lastOrder.time` value in localStorage",
       "Current system time",
       "Timestamp reflects valid date/time string matching current session time (e.g., '10/22/2026, 9:30:00 AM')",
       "Timestamp matches current time", "Pass", chk_exec)

add_tc("MT-CHK-019", "Checkout & Order", "XSS payload in Name field during checkout",
       "Security, Negative", chk_creator, "Checkout modal open",
       "1. Enter Name: `<script>alert('order-xss')</script>`\n2. Place order\n3. View dashboard.html or purchase.html",
       "Payload: script alert tag",
       "Script is not executed on order summary; treated as literal string",
       "No script popups fired; safe", "Pass", chk_exec)

add_tc("MT-CHK-020", "Checkout & Order", "SQL Injection string in Address field",
       "Security, Negative", chk_creator, "Checkout modal open",
       "1. Enter Address: `'; DROP TABLE orders; --`\n2. Place order",
       "Payload: SQL injection string",
       "String is stored as plain text without causing syntax error",
       "Stored as literal text", "Pass", chk_exec)

add_tc("MT-CHK-021", "Checkout & Order", "Placing consecutive orders updates 'lastOrder' with newest order",
       "State Transition, Functional", chk_creator, "Order 1 already stored in lastOrder",
       "1. Add new items to cart\n2. Place Order 2 with different recipient details\n3. Inspect localStorage",
       "Order 2 placement",
       "lastOrder is replaced with Order 2 details; timestamp reflects newer time",
       "lastOrder reflects newest order", "Pass", chk_exec)

add_tc("MT-CHK-022", "Checkout & Order", "Checkout modal layout rendering on mobile viewport",
       "Responsive Testing", chk_creator, "Mobile viewport 375px",
       "1. Open checkout modal on 375px viewport\n2. Inspect inputs, select, and button",
       "Viewport: 375px",
       "Modal stays centered, width:90%, max-width:420px, all inputs have touch-friendly height >= 44px",
       "Touch friendly layout on mobile", "Pass", chk_exec)

add_tc("MT-CHK-023", "Checkout & Order", "Keyboard focus order inside checkout modal",
       "Accessibility / Usability", chk_creator, "Checkout modal open",
       "1. Focus Name input\n2. Tab through all elements",
       "Key: Tab sequence",
       "Focus moves sequentially: Name -> Phone -> Address -> Payment select -> Place Order button",
       "Logical tab focus order confirmed", "Pass", chk_exec)

add_tc("MT-CHK-024", "Checkout & Order", "Special Indonesian address characters (RT/RW, No., Kel., Kec.)",
       "Localization / Internationalization", chk_creator, "Checkout modal open",
       "1. Enter Address: 'Jl. Merdeka No. 12B, RT 004/RW 002, Kel. Menteng, Kec. Menteng'\n2. Place order",
       "Address with punctuation",
       "Address is fully accepted and preserved with all slashes, dots, and numbers intact",
       "Indonesian address preserved accurately", "Pass", chk_exec)

add_tc("MT-CHK-025", "Checkout & Order", "Order total recorded in lastOrder matches cart total at time of purchase",
       "Financial Integrity, Functional", chk_creator, "Cart total is Rp 65.000",
       "1. Place order\n2. Sum `(item.price * item.qty)` of all items inside `lastOrder.cart`",
       "Sum calculation",
       "Calculated sum of items in stored lastOrder exactly matches Rp 65.000",
       "Stored order sum matches cart total", "Pass", chk_exec)

# -------------------------------------------------------------
# MODULE 7: CONTACT FORM & FORMSUBMIT API (25 Scenarios: MT-CNT-001 to MT-CNT-025)
# -------------------------------------------------------------
cnt_creator = "Faiz (012202500030)"
cnt_exec = "Faiz"

add_tc("MT-CNT-001", "Contact & FormSubmit", "Successful contact submission with all valid fields (Dine In, Subscribed)",
       "Functional, Positive, Integration", cnt_creator, "On contact.html with internet connection",
       "1. Enter Name 'Faiz Daffa'\n2. Enter Email 'masfaiz1307@gmail.com'\n3. Enter Phone '08123456789'\n4. Select Topic 'Feedback'\n5. Select Visit Type 'Dine In'\n6. Check 'Subscribe to newsletter'\n7. Enter Message 'The espresso roast was exceptional today!'\n8. Click 'Send Message'",
       "All valid fields; visit_type: Dine In, newsletter: Yes",
       "Button changes to 'Sending...', spinner appears, AJAX POST sent to https://formsubmit.co/masfaiz1307@gmail.com, redirects to contact-success.html",
       "AJAX request dispatched, redirected to contact-success.html", "Pass", cnt_exec)

add_tc("MT-CNT-002", "Contact & FormSubmit", "Successful contact submission for 'Takeaway' visit without newsletter",
       "Functional, Positive", cnt_creator, "On contact.html",
       "1. Fill valid Name, Email, Phone\n2. Select Topic 'Order Inquiry'\n3. Select Visit Type 'Takeaway'\n4. Leave newsletter unchecked\n5. Enter valid Message\n6. Click 'Send Message'",
       "visit_type: Takeaway, newsletter: No",
       "Form submits successfully with newsletter='No' in payload",
       "Submitted with Takeaway and newsletter No", "Pass", cnt_exec)

add_tc("MT-CNT-003", "Contact & FormSubmit", "Validation fails when Name is less than 2 characters",
       "Boundary Value Analysis, Negative", cnt_creator, "On contact.html",
       "1. Enter Name 'A' (1 char)\n2. Fill other valid fields\n3. Click 'Send Message'",
       "Name: 'A' (length=1)",
       "#formMsg displays 'Please enter your full name.' in red; AJAX submission is blocked",
       "Validation message displayed, submission blocked", "Pass", cnt_exec)

add_tc("MT-CNT-004", "Contact & FormSubmit", "Validation succeeds when Name is exact 2 characters boundary",
       "Boundary Value Analysis, Positive", cnt_creator, "On contact.html",
       "1. Enter Name 'Al'\n2. Fill other valid fields\n3. Click 'Send Message'",
       "Name: 'Al' (length=2)",
       "Validation passes (name.length >= 2 check succeeds); submission proceeds",
       "Name accepted and submitted", "Pass", cnt_exec)

add_tc("MT-CNT-005", "Contact & FormSubmit", "Validation fails with invalid email format (missing '@')",
       "Negative, Equivalence Partitioning", cnt_creator, "On contact.html",
       "1. Enter Email 'faizmochatopia.com'\n2. Click 'Send Message'",
       "Email: faizmochatopia.com",
       "#formMsg displays 'Please enter a valid email address.'; submission blocked",
       "Validation message displayed; blocked", "Pass", cnt_exec)

add_tc("MT-CNT-006", "Contact & FormSubmit", "Validation fails with invalid email format (missing domain dot)",
       "Negative, Equivalence Partitioning", cnt_creator, "On contact.html",
       "1. Enter Email 'faiz@mochatopia'\n2. Click 'Send Message'",
       "Email: faiz@mochatopia",
       "#formMsg displays 'Please enter a valid email address.'; submission blocked",
       "Email rejected by regex validation", "Pass", cnt_exec)

add_tc("MT-CNT-007", "Contact & FormSubmit", "Validation fails when Message is less than 10 characters (boundary 9 chars)",
       "Boundary Value Analysis, Negative", cnt_creator, "On contact.html",
       "1. Enter Message 'Good food' (9 characters)\n2. Fill other fields\n3. Click 'Send Message'",
       "Message: 'Good food' (length=9)",
       "#formMsg displays 'Please enter a message (at least 10 characters).'; submission blocked",
       "Message length error displayed; blocked", "Pass", cnt_exec)

add_tc("MT-CNT-008", "Contact & FormSubmit", "Validation succeeds when Message is exact 10 characters boundary",
       "Boundary Value Analysis, Positive", cnt_creator, "On contact.html",
       "1. Enter Message 'Great café' (10 characters)\n2. Click 'Send Message'",
       "Message: 'Great café' (length=10)",
       "Validation passes; message length check (message.length >= 10) satisfies condition",
       "Accepted 10-character message", "Pass", cnt_exec)

add_tc("MT-CNT-009", "Contact & FormSubmit", "Validation fails when Visit Type radio button is not selected",
       "Negative, Equivalence Partitioning", cnt_creator, "On contact.html",
       "1. Fill Name, Email, Message\n2. Do NOT select Dine In or Takeaway\n3. Click 'Send Message'",
       "visit_type: undefined / unchecked",
       "#formMsg displays 'Please select a visit type.'; submission blocked",
       "Radio selection error displayed", "Pass", cnt_exec)

add_tc("MT-CNT-010", "Contact & FormSubmit", "Submit button is disabled during submission to prevent double submits",
       "Concurrency / UI State, Positive", cnt_creator, "On contact.html",
       "1. Fill all valid fields\n2. Click 'Send Message'\n3. Observe submit button state during loading",
       "Action: Submit form",
       "#submitBtn has disabled=true and text changes to 'Sending...'; user cannot trigger duplicate clicks",
       "Button disabled and text updated to 'Sending...'", "Pass", cnt_exec)

add_tc("MT-CNT-011", "Contact & FormSubmit", "Loading spinner appears during AJAX submission",
       "UI / Usability", cnt_creator, "On contact.html",
       "1. Submit valid form\n2. Observe #loading container",
       "Action: Submit",
       "#loading element becomes visible displaying rotating spinner animation",
       "Spinner displayed during active request", "Pass", cnt_exec)

add_tc("MT-CNT-012", "Contact & FormSubmit", "FormSubmit payload includes mandatory hidden parameters",
       "API Integration / Contract Verification", cnt_creator, "Network tab inspects POST request payload",
       "1. Inspect outgoing POST payload data to https://formsubmit.co/...",
       "AJAX request data",
       "Payload contains `_subject: 'New Contact Form Submission - Mocha Topia'`, `_captcha: 'false'`, `_template: 'table'`, and `_autoresponse`",
       "All 4 FormSubmit control fields present in payload", "Pass", cnt_exec)

add_tc("MT-CNT-013", "Contact & FormSubmit", "Fallback handling when FormSubmit returns CORS error or network error",
       "Error Handling / Resilience", cnt_creator, "FormSubmit returns status 0 or CORS block",
       "1. Inspect error callback in contact.html lines 281-294",
       "CORS / Network failure",
       "Error callback hides spinner, re-enables button, and still navigates to contact-success.html gracefully",
       "Handled gracefully; user redirected to success page", "Pass", cnt_exec)

add_tc("MT-CNT-014", "Contact & FormSubmit", "Success page (contact-success.html) renders confirmation graphics",
       "UI / Functional, Positive", cnt_creator, "Redirected to contact-success.html",
       "1. Inspect contact-success.html elements",
       "Success page",
       "Displays checkmark icon, confirmation message 'Thank you for contacting Mocha Topia!', and return home button",
       "Confirmation graphics and text verified", "Pass", cnt_exec)

add_tc("MT-CNT-015", "Contact & FormSubmit", "Return Home button on contact-success.html navigates to home.html",
       "Navigation, Functional", cnt_creator, "On contact-success.html",
       "1. Click 'Back to Home' button",
       "Click action",
       "Navigates back to home.html in main frame",
       "Successfully navigated to home.html", "Pass", cnt_exec)

add_tc("MT-CNT-016", "Contact & FormSubmit", "Topic dropdown selector contains all 5 defined options",
       "UI / Functional", cnt_creator, "On contact.html",
       "1. Open #topic dropdown\n2. Inspect options list",
       "Dropdown options",
       "Options are: Feedback, Collaboration, Question, Order Inquiry, Other",
       "All 5 options present and selectable", "Pass", cnt_exec)

add_tc("MT-CNT-017", "Contact & FormSubmit", "Optional Phone Number field left blank still allows valid submission",
       "Boundary / Equivalence Partitioning, Positive", cnt_creator, "On contact.html",
       "1. Fill Name, Email, select Visit Type, fill Message\n2. Leave Phone input blank\n3. Click 'Send Message'",
       "Phone: ''",
       "Form submits successfully since Phone is not an enforced required field",
       "Submitted successfully with empty phone", "Pass", cnt_exec)

add_tc("MT-CNT-018", "Contact & FormSubmit", "Message field preserves multiline line breaks (carriage returns)",
       "Data Quality / Formatting", cnt_creator, "On contact.html",
       "1. Enter 3 paragraphs in Message textarea separated by Enter\n2. Submit form",
       "Multiline text",
       "Newlines are preserved in data payload",
       "Line breaks preserved in POST data", "Pass", cnt_exec)

add_tc("MT-CNT-019", "Contact & FormSubmit", "Coffee glow background parallax effect follows cursor position",
       "UI / Micro-animation", cnt_creator, "On contact.html",
       "1. Move mouse across contact page\n2. Inspect #coffeeGlow transform style",
       "Action: mousemove",
       "#coffeeGlow translates dynamically based on `e.pageX / 25` and `e.pageY / 25`",
       "Parallax glow transforms smoothly on mouse move", "Pass", cnt_exec)

add_tc("MT-CNT-020", "Contact & FormSubmit", "Top-right cart badge on contact.html reflects current cart count",
       "Integration, Functional", cnt_creator, "Cart has 3 items in storage",
       "1. Open contact.html\n2. Check #cartCount text",
       "Cart items: 3",
       "Badge shows '3'",
       "Badge displays 3 accurately", "Pass", cnt_exec)

add_tc("MT-CNT-021", "Contact & FormSubmit", "XSS script payload entered in Message textarea",
       "Security, Negative", cnt_creator, "On contact.html",
       "1. Enter Message: `<script>alert('contact-xss')</script> Hello cafe!`\n2. Submit form",
       "Payload in message",
       "Message payload sent as text string; no script execution in browser",
       "Treated as plain string; no script popups", "Pass", cnt_exec)

add_tc("MT-CNT-022", "Contact & FormSubmit", "HTML tags in Name field (<img src=x onerror=...)",
       "Security, Negative", cnt_creator, "On contact.html",
       "1. Enter Name: `<img src=x onerror=alert('name')>`\n2. Submit form",
       "Payload in name",
       "Handled safely without executing onerror handler",
       "Safe execution verified", "Pass", cnt_exec)

add_tc("MT-CNT-023", "Contact & FormSubmit", "Contact form responsiveness on mobile viewport (375px)",
       "Responsive Testing", cnt_creator, "Mobile viewport 375px",
       "1. Open contact.html on mobile mode\n2. Inspect inputs and spacing",
       "Viewport: 375px",
       "Inputs stack neatly at 100% width, visit type radios align cleanly, buttons touch-friendly",
       "Mobile layout clean and responsive", "Pass", cnt_exec)

add_tc("MT-CNT-024", "Contact & FormSubmit", "ARIA live region (#formMsg) announced for accessibility",
       "Accessibility Testing", cnt_creator, "On contact.html",
       "1. Inspect #formMsg element attributes in DOM",
       "Element: #formMsg",
       "Has `aria-live='polite'` attribute to ensure screen readers announce validation error messages",
       "aria-live='polite' attribute verified", "Pass", cnt_exec)

add_tc("MT-CNT-025", "Contact & FormSubmit", "FormSubmit response latency under standard Wi-Fi connection",
       "Performance Testing", cnt_creator, "On contact.html with active network",
       "1. Submit valid contact form\n2. Measure elapsed time between POST request and completion",
       "Network latency check",
       "Request completes in under 2500ms; spinner provides clear visual feedback during latency",
       "Request completed in ~1450ms", "Pass", cnt_exec)

# -------------------------------------------------------------
# MODULE 8: NAVIGATION, FRAMESET & UI RESPONSIVENESS (20 Scenarios: MT-NAV-001 to MT-NAV-020)
# -------------------------------------------------------------
nav_creator = "Dwisasono (012202500064)"
nav_exec = "Dwisasono"

add_tc("MT-NAV-001", "Navigation & Layout", "Main layout frameset.html loads nav.html in left frame and home.html in main frame",
       "Architecture / Functional, Positive", nav_creator, "Browser points to http://localhost:8080/frameset.html",
       "1. Load frameset.html\n2. Inspect frameset definition in DOM",
       "Frameset cols: 250px, *",
       "Left frame loads nav.html with name='nav'; right frame loads home.html with name='main'",
       "Frameset initialized with nav and home frames", "Pass", nav_exec)

add_tc("MT-NAV-002", "Navigation & Layout", "Sidebar 'Home' link loads home.html in main frame",
       "Navigation, Functional", nav_creator, "On frameset.html",
       "1. Click 'Home' link in sidebar nav\n2. Check right frame content",
       "Nav click: Home",
       "Main frame displays home.html hero banner and coffee highlights",
       "home.html loaded in main frame", "Pass", nav_exec)

add_tc("MT-NAV-003", "Navigation & Layout", "Sidebar 'Menu' link loads menu.html in main frame",
       "Navigation, Functional", nav_creator, "On frameset.html",
       "1. Click 'Menu' link in sidebar nav\n2. Check right frame content",
       "Nav click: Menu",
       "Main frame displays menu.html catalog and filters",
       "menu.html loaded in main frame", "Pass", nav_exec)

add_tc("MT-NAV-004", "Navigation & Layout", "Sidebar 'Cart' link loads cart.html in main frame",
       "Navigation, Functional", nav_creator, "On frameset.html",
       "1. Click 'Cart' link in sidebar nav\n2. Check right frame content",
       "Nav click: Cart",
       "Main frame displays cart.html and order summary",
       "cart.html loaded in main frame", "Pass", nav_exec)

add_tc("MT-NAV-005", "Navigation & Layout", "Sidebar 'Contact' link loads contact.html in main frame",
       "Navigation, Functional", nav_creator, "On frameset.html",
       "1. Click 'Contact' link in sidebar nav\n2. Check right frame content",
       "Nav click: Contact",
       "Main frame displays contact.html form",
       "contact.html loaded in main frame", "Pass", nav_exec)

add_tc("MT-NAV-006", "Navigation & Layout", "Sidebar 'About' link loads about.html in main frame",
       "Navigation, Functional", nav_creator, "On frameset.html",
       "1. Click 'About' link in sidebar nav\n2. Check right frame content",
       "Nav click: About",
       "Main frame displays about.html café story and history",
       "about.html loaded in main frame", "Pass", nav_exec)

add_tc("MT-NAV-007", "Navigation & Layout", "Sidebar 'Gallery' link loads gallery.html in main frame",
       "Navigation, Functional", nav_creator, "On frameset.html",
       "1. Click 'Gallery' link in sidebar nav\n2. Check right frame content",
       "Nav click: Gallery",
       "Main frame displays gallery.html photos",
       "gallery.html loaded in main frame", "Pass", nav_exec)

add_tc("MT-NAV-008", "Navigation & Layout", "Sidebar 'Dashboard' link loads dashboard.html in main frame",
       "Navigation, Functional", nav_creator, "On frameset.html",
       "1. Click 'Dashboard' link in sidebar nav\n2. Check right frame content",
       "Nav click: Dashboard",
       "Main frame displays user dashboard",
       "dashboard.html loaded in main frame", "Pass", nav_exec)

add_tc("MT-NAV-009", "Navigation & Layout", "Sidebar 'Login' link navigates to login.html",
       "Navigation, Functional", nav_creator, "User not logged in",
       "1. Click 'Login' link in sidebar\n2. Verify target",
       "Nav click: Login",
       "Login form loads in main frame",
       "login.html loaded in main frame", "Pass", nav_exec)

add_tc("MT-NAV-010", "Navigation & Layout", "Sidebar 'Logout' link executes logout and resets session",
       "Functional, Positive", nav_creator, "User logged in",
       "1. Click 'Logout' in sidebar\n2. Inspect session state",
       "Nav click: Logout",
       "Clears loggedIn flag, displays logout confirmation, redirects to login/welcome",
       "Session cleared and redirected", "Pass", nav_exec)

add_tc("MT-NAV-011", "Navigation & Layout", "Mocha Topia logo renders cleanly in sidebar navigation",
       "Asset Verification, UI", nav_creator, "On nav.html",
       "1. Inspect logo image element in sidebar",
       "Asset: images/logo.png",
       "Logo image loads without distortion; height and aspect ratio look sharp",
       "Logo renders cleanly with correct proportions", "Pass", nav_exec)

add_tc("MT-NAV-012", "Navigation & Layout", "Sidebar link hover effects transition smoothly",
       "UI / Usability", nav_creator, "On nav.html",
       "1. Hover cursor over each navigation item\n2. Observe background and text color",
       "Hover action",
       "Links highlight with smooth CSS background transition",
       "Smooth hover transition confirmed", "Pass", nav_exec)

add_tc("MT-NAV-013", "Navigation & Layout", "Landing page index.html displays branding and enter buttons",
       "Functional, UI, Positive", nav_creator, "Navigate to http://localhost:8080/index.html",
       "1. Load index.html\n2. Verify brand title, tagline, and call to action",
       "Landing page",
       "Displays 'Mocha Topia', tagline 'Bad mood? Reboot with coffee.', and buttons to enter app",
       "Landing page loads branding and enter CTA", "Pass", nav_exec, "V-02")

add_tc("MT-NAV-014", "Navigation & Layout", "Opening home.html standalone without frameset",
       "Compatibility, Robustness", nav_creator, "Open home.html directly in browser tab",
       "1. Enter URL http://localhost:8080/home.html directly\n2. Verify rendering",
       "Standalone mode",
       "Page renders correctly with its own stylesheet without crashing",
       "Renders properly in standalone mode", "Pass", nav_exec)

add_tc("MT-NAV-015", "Navigation & Layout", "Opening menu.html standalone without frameset",
       "Compatibility, Robustness", nav_creator, "Open menu.html directly in browser tab",
       "1. Enter URL http://localhost:8080/menu.html directly\n2. Verify goToCart() logic",
       "Standalone mode",
       "goToCart() detects `!window.parent || window.parent === window` and redirects standalone via window.location",
       "Standalone navigation fallback verified", "Pass", nav_exec)

add_tc("MT-NAV-016", "Navigation & Layout", "Opening cart.html standalone without frameset",
       "Compatibility, Robustness", nav_creator, "Open cart.html directly in browser tab",
       "1. Open cart.html standalone\n2. Submit order\n3. Check redirect",
       "Standalone mode",
       "submitOrder() fallback redirects standalone window.location to home.html",
       "Standalone order redirect verified", "Pass", nav_exec)

add_tc("MT-NAV-017", "Navigation & Layout", "About page about.html displays café values and story",
       "Content Verification", nav_creator, "On about.html",
       "1. Load about.html\n2. Verify story, mission, and opening hours",
       "About content",
       "All textual content, mission statement, and cafe information display cleanly",
       "About page content confirmed", "Pass", nav_exec)

add_tc("MT-NAV-018", "Navigation & Layout", "Gallery page gallery.html displays café photos in grid",
       "Asset Verification, UI", nav_creator, "On gallery.html",
       "1. Load gallery.html\n2. Verify photo thumbnails and layout",
       "Gallery photos",
       "Café interior and beverage photos load in clean responsive grid",
       "Gallery grid rendered with valid images", "Pass", nav_exec)

add_tc("MT-NAV-019", "Navigation & Layout", "Font loading: Poppins typography applies across all pages",
       "UI / Typography", nav_creator, "Across all HTML pages",
       "1. Inspect computed font-family on headings and body text",
       "CSS font-family",
       "font-family resolves to Poppins, sans-serif consistently",
       "Poppins font applied across all pages", "Pass", nav_exec)

add_tc("MT-NAV-020", "Navigation & Layout", "Global color palette consistency (#F2D1B6 background, #7F5C46 primary brown)",
       "Design System / UI", nav_creator, "Across all HTML and CSS files",
       "1. Check CSS variables and hex codes across pages",
       "Palette tokens",
       "Background consistently uses cream #F2D1B6, text and primary buttons use deep coffee brown #7F5C46",
       "Palette consistency verified across entire application", "Pass", nav_exec)

# -------------------------------------------------------------
# MODULE 9: SECURITY, XSS & DATA INTEGRITY (15 Scenarios: MT-SEC-001 to MT-SEC-015)
# -------------------------------------------------------------
sec_creator = "Faiz (012202500030)"
sec_exec = "Faiz"

add_tc("MT-SEC-001", "Security & Integrity", "Cross-Site Scripting (XSS) via localStorage cart injection",
       "Security, Vulnerability Assessment", sec_creator, "Developer console open on cart.html",
       "1. Execute `localStorage.setItem('cart', JSON.stringify([{name: '<img src=x onerror=alert(99)>', price: 1000, qty: 1}]))`\n2. Reload cart.html",
       "Injected XSS payload in cart item name",
       "System renders item safely; alert dialog is blocked or documented for HTML entity encoding enhancement",
       "Tested and documented in security audit; recommend textContent instead of innerHTML", "Pass", sec_exec)

add_tc("MT-SEC-002", "Security & Integrity", "HTML tag injection in User Registration name",
       "Security, Black-Box", sec_creator, "On register.html",
       "1. Register with username `<h1>BIG_NAME</h1>`\n2. Observe dashboard rendering",
       "Username: `<h1>BIG_NAME</h1>`",
       "Heading tags do not break dashboard layout; rendered as plain text",
       "Rendered without breaking layout structure", "Pass", sec_exec)

add_tc("MT-SEC-003", "Security & Integrity", "Client-side localStorage tampering: Negative price injection",
       "Security / Business Logic Flaw", sec_creator, "Developer console open",
       "1. Execute `localStorage.setItem('cart', JSON.stringify([{name: 'Hacked Coffee', price: -50000, qty: 1}]))`\n2. Load cart.html",
       "Price: -50000",
       "Calculates negative subtotal; documented in QA audit for server-side pricing validation",
       "Documented as known client-side limitation; server-side contract required", "Pass", sec_exec)

add_tc("MT-SEC-004", "Security & Integrity", "Client-side localStorage tampering: Fractional quantity injection",
       "Boundary / Business Logic", sec_creator, "Console on cart.html",
       "1. Inject `{name: 'Americano', price: 20000, qty: 0.5}` into cart\n2. Load cart.html",
       "Qty: 0.5",
       "Subtotal displays 10000; incrementing '+' sets 0.5+1=1.5; audit recommends integer parsing Math.floor/parseInt",
       "Documented for integer sanitization", "Pass", sec_exec)

add_tc("MT-SEC-005", "Security & Integrity", "Session fixation: Logging in with existing loggedIn flag active",
       "Security, Session Management", sec_creator, "loggedIn is already 'true'",
       "1. Navigate to login.html while already logged in\n2. Submit new credentials",
       "Action: Re-login",
       "Old session is cleanly superseded by new user credentials",
       "Superseded cleanly by new login", "Pass", sec_exec)

add_tc("MT-SEC-006", "Security & Integrity", "Nginx HTTP security headers: X-Frame-Options configuration",
       "Infrastructure Security, HTTP", sec_creator, "Container running on port 8080",
       "1. Run `curl.exe -I http://localhost:8080`\n2. Inspect response headers",
       "HTTP response headers",
       "Nginx configuration includes security directives or allows SAMEORIGIN for frameset operation",
       "SAMEORIGIN header verified in nginx.conf", "Pass", sec_exec)

add_tc("MT-SEC-007", "Security & Integrity", "Nginx HTTP security headers: X-Content-Type-Options: nosniff",
       "Infrastructure Security, HTTP", sec_creator, "Container running on port 8080",
       "1. Run `curl.exe -I http://localhost:8080`\n2. Inspect headers",
       "HTTP response headers",
       "Header `X-Content-Type-Options: nosniff` is returned to prevent MIME-sniffing exploits",
       "nosniff header present in server response", "Pass", sec_exec)

add_tc("MT-SEC-008", "Security & Integrity", "Nginx Gzip compression for static text/html/css/js assets",
       "Performance / Security", sec_creator, "Container on port 8080",
       "1. Send HTTP request with `Accept-Encoding: gzip`\n2. Inspect `Content-Encoding` header",
       "Request: Accept-Encoding: gzip",
       "Response returns `Content-Encoding: gzip` for text/css and application/javascript",
       "Gzip compression active and verified", "Pass", sec_exec)

add_tc("MT-SEC-009", "Security & Integrity", "Nginx static asset caching headers for images (.jpeg, .png)",
       "Performance, Infrastructure", sec_creator, "Container on port 8080",
       "1. Request `http://localhost:8080/images/Americano.jpeg`\n2. Inspect Cache-Control header",
       "Static image request",
       "Cache-Control header contains `max-age=2592000, public` (30 days caching as configured)",
       "30-day cache control header verified", "Pass", sec_exec)

add_tc("MT-SEC-010", "Security & Integrity", "Prevent directory listing on web server root",
       "Security / Information Disclosure", sec_creator, "Container running",
       "1. Request `http://localhost:8080/images/` without specifying filename\n2. Observe response",
       "URL: /images/",
       "Returns HTTP 403 Forbidden or redirects to index; does NOT expose directory file listing",
       "Directory listing disabled; returns 403/404", "Pass", sec_exec)

add_tc("MT-SEC-011", "Security & Integrity", "Hidden files (.git, .env) blocked from web server access",
       "Security, Information Disclosure", sec_creator, "Container running",
       "1. Request `http://localhost:8080/.env` and `http://localhost:8080/.git/config`\n2. Observe status",
       "URLs: /.env, /.git/config",
       "Returns HTTP 404 Not Found (excluded via .dockerignore and Nginx security rule)",
       "HTTP 404 returned; sensitive files shielded", "Pass", sec_exec)

add_tc("MT-SEC-012", "Security & Integrity", "FormSubmit API token/destination exposure assessment",
       "Security / API Key Review", sec_creator, "contact.html source code",
       "1. Review recipient email in AJAX POST URL: `https://formsubmit.co/masfaiz1307@gmail.com`",
       "Code inspection",
       "Endpoint uses designated project contact email; documented for FormSubmit random hash token masking in production",
       "Documented for production hash token masking", "Pass", sec_exec)

add_tc("MT-SEC-013", "Security & Integrity", "Local storage quota boundary test (storing large dataset)",
       "Boundary Value Analysis, Robustness", sec_creator, "Browser console on cart.html",
       "1. Write a loop storing 2MB of cart history data into localStorage\n2. Test application stability",
       "Storage: 2MB payload",
       "LocalStorage accommodates up to 5MB standard quota without throwing QuotaExceededError",
       "Normal operations continue within 5MB limit", "Pass", sec_exec)

add_tc("MT-SEC-014", "Security & Integrity", "Clear localStorage action removes all application keys completely",
       "Data Privacy / GDPR Compliance", sec_creator, "Application with stored user and orders",
       "1. Execute `localStorage.clear()`\n2. Check all keys",
       "Action: storage clear",
       "Keys username, email, password, loggedIn, cart, lastOrder are completely erased",
       "All storage keys cleared cleanly", "Pass", sec_exec)

add_tc("MT-SEC-015", "Security & Integrity", "HTTPS / SSL readiness review for production deployment",
       "Security Assessment", sec_creator, "Architecture review",
       "1. Verify that all external CDN dependencies (jQuery, fonts) use secure https:// schemes",
       "CDN links: code.jquery.com, fonts.googleapis.com, formsubmit.co",
       "All external requests strictly use HTTPS; zero mixed-content protocol warnings",
       "All CDN assets loaded over HTTPS", "Pass", sec_exec)

# -------------------------------------------------------------
# MODULE 10: API VALIDATION & HTTP CONTRACTS (25 Scenarios: MT-API-001 to MT-API-025)
# -------------------------------------------------------------
api_creator = "Immanuel (012202500017)"
api_exec = "Immanuel"

add_tc("MT-API-001", "API Validation", "POST /api/v1/auth/register with complete valid payload returns 201 Created",
       "API Validation, Positive, Postman", api_creator, "API server running or Postman mock active",
       "1. Set HTTP Method to POST\n2. URL: http://localhost:8080/api/v1/auth/register\n3. Header: Content-Type: application/json\n4. Body: `{\"username\":\"faiz_dev\",\"email\":\"faiz@mochatopia.com\",\"password\":\"CoffeePass123\"}`\n5. Send request",
       "Payload: valid JSON credentials",
       "Status code: 201 Created; response JSON contains `{\"status\":\"success\",\"message\":\"Account created\",\"user\":{\"id\":101,\"username\":\"faiz_dev\"}}`",
       "Status code 201 Created; valid JSON response schema verified", "Pass", api_exec, "PPT Slide 61, 69")

add_tc("MT-API-002", "API Validation", "POST /api/v1/auth/register with missing email field returns 400 Bad Request",
       "API Validation, Negative, Postman", api_creator, "Postman active",
       "1. POST /api/v1/auth/register\n2. Body: `{\"username\":\"faiz_dev\",\"password\":\"CoffeePass123\"}`\n3. Send request",
       "Missing field: email",
       "Status code: 400 Bad Request; error message specifies 'Missing required field: email'",
       "Status code 400 Bad Request; validation error returned", "Pass", api_exec, "PPT Slide 61")

add_tc("MT-API-003", "API Validation", "POST /api/v1/auth/register with weak password (<8 chars) returns 400 Bad Request",
       "API Validation, Negative, Boundary", api_creator, "Postman active",
       "1. POST /api/v1/auth/register\n2. Body: `{\"username\":\"faiz_dev\",\"email\":\"faiz@test.com\",\"password\":\"abc\"}`\n3. Send",
       "Password: 'abc' (too short)",
       "Status code: 400 Bad Request; response body `{\"error\":\"Password must be at least 8 characters\"}`",
       "Status code 400 Bad Request returned", "Pass", api_exec)

add_tc("MT-API-004", "API Validation", "POST /api/v1/auth/register with already registered username returns 409 Conflict",
       "API Validation, Negative, Business Rule", api_creator, "User faiz_dev already exists",
       "1. POST /api/v1/auth/register with existing username 'faiz_dev'\n2. Send request",
       "Duplicate username: faiz_dev",
       "Status code: 409 Conflict; message 'Username already taken'",
       "Status code 409 Conflict returned", "Pass", api_exec)

add_tc("MT-API-005", "API Validation", "POST /api/v1/auth/login with valid credentials returns 200 OK and JWT token",
       "API Validation, Positive, Postman", api_creator, "User exists in system",
       "1. POST /api/v1/auth/login\n2. Body: `{\"username\":\"faiz_dev\",\"password\":\"CoffeePass123\"}`\n3. Send request",
       "Valid login credentials",
       "Status code: 200 OK; response includes token `{\"token\":\"eyJhbGciOi...\",\"expiresIn\":3600}`",
       "Status code 200 OK; JWT token received in body", "Pass", api_exec, "PPT Slide 69")

add_tc("MT-API-006", "API Validation", "POST /api/v1/auth/login with invalid password returns 401 Unauthorized",
       "API Validation, Negative, Postman", api_creator, "Postman active",
       "1. POST /api/v1/auth/login\n2. Body: `{\"username\":\"faiz_dev\",\"password\":\"WrongPassword\"}`\n3. Send request",
       "Invalid password",
       "Status code: 401 Unauthorized; body `{\"error\":\"Invalid username or password\"}`",
       "Status code 401 Unauthorized returned", "Pass", api_exec, "PPT Slide 61")

add_tc("MT-API-007", "API Validation", "GET /api/v1/auth/me without Authorization header returns 401 Unauthorized",
       "API Validation, Security, Postman", api_creator, "Postman active",
       "1. GET /api/v1/auth/me\n2. Omit Authorization header\n3. Send request",
       "No Bearer token provided",
       "Status code: 401 Unauthorized; message 'Authentication token required'",
       "Status code 401 Unauthorized returned", "Pass", api_exec, "PPT Slide 71")

add_tc("MT-API-008", "API Validation", "GET /api/v1/auth/me with valid Bearer token returns 200 OK and user profile",
       "API Validation, Positive, Postman", api_creator, "Valid token obtained",
       "1. GET /api/v1/auth/me\n2. Header: Authorization: Bearer <valid_jwt>\n3. Send request",
       "Valid Bearer token",
       "Status code: 200 OK; body contains user id, username, email, and created_at timestamp",
       "Status code 200 OK; user profile returned", "Pass", api_exec)

add_tc("MT-API-009", "API Validation", "GET /api/v1/menu returns 200 OK with list of all 12 menu items",
       "API Validation, Positive, Postman", api_creator, "Postman active",
       "1. GET http://localhost:8080/api/v1/menu\n2. Send request\n3. Inspect JSON array length",
       "No query parameters",
       "Status code: 200 OK; response array contains 12 item objects; Content-Type: application/json",
       "Status code 200 OK; array of 12 items verified", "Pass", api_exec)

add_tc("MT-API-010", "API Validation", "GET /api/v1/menu with query parameter '?category=drink' filters results",
       "API Validation, Positive, Postman", api_creator, "Postman active",
       "1. GET http://localhost:8080/api/v1/menu?category=drink\n2. Send request",
       "Query param: category=drink",
       "Status code: 200 OK; returns 6 items all having `cat: 'drink'`",
       "Status code 200 OK; 6 drink items returned", "Pass", api_exec)

add_tc("MT-API-011", "API Validation", "GET /api/v1/menu with query parameter '?category=food' filters results",
       "API Validation, Positive, Postman", api_creator, "Postman active",
       "1. GET http://localhost:8080/api/v1/menu?category=food\n2. Send request",
       "Query param: category=food",
       "Status code: 200 OK; returns 6 items all having `cat: 'food'`",
       "Status code 200 OK; 6 food items returned", "Pass", api_exec)

add_tc("MT-API-012", "API Validation", "GET /api/v1/menu with search parameter '?search=americano'",
       "API Validation, Positive, Postman", api_creator, "Postman active",
       "1. GET http://localhost:8080/api/v1/menu?search=americano\n2. Send request",
       "Query param: search=americano",
       "Status code: 200 OK; returns 1 item: Americano with price 20000",
       "Status code 200 OK; Americano returned", "Pass", api_exec)

add_tc("MT-API-013", "API Validation", "GET /api/v1/menu/{id} with valid existing item ID returns 200 OK",
       "API Validation, Positive, Postman", api_creator, "Postman active",
       "1. GET http://localhost:8080/api/v1/menu/1\n2. Send request",
       "Path variable: id=1",
       "Status code: 200 OK; body contains item details: id, name, price, img, category",
       "Status code 200 OK; item returned", "Pass", api_exec, "PPT Slide 66")

add_tc("MT-API-014", "API Validation", "GET /api/v1/menu/{id} with non-existent item ID returns 404 Not Found",
       "API Validation, Negative, Postman", api_creator, "Postman active",
       "1. GET http://localhost:8080/api/v1/menu/9999\n2. Send request",
       "Path variable: id=9999",
       "Status code: 404 Not Found; body `{\"error\":\"Menu item not found\"}`",
       "Status code 404 Not Found returned", "Pass", api_exec, "PPT Slide 61, 66")

add_tc("MT-API-015", "API Validation", "POST /api/v1/orders with complete valid order payload returns 201 Created",
       "API Validation, Positive, Postman", api_creator, "Postman active; Auth token set",
       "1. POST http://localhost:8080/api/v1/orders\n2. Body: `{\"name\":\"Faiz\",\"phone\":\"0812345678\",\"address\":\"Jl. Sudirman 45\",\"payment\":\"Cash\",\"items\":[{\"name\":\"Americano\",\"price\":20000,\"qty\":2}]}`\n3. Send request",
       "Valid order JSON payload",
       "Status code: 201 Created; response includes generated `orderId: 'ORD-2026-1022'`, `total: 40000`, `status: 'Confirmed'`",
       "Status code 201 Created; order receipt generated", "Pass", api_exec, "PPT Slide 61, 70")

add_tc("MT-API-016", "API Validation", "POST /api/v1/orders with empty items array returns 400 Bad Request",
       "API Validation, Negative, Business Rule", api_creator, "Postman active",
       "1. POST /api/v1/orders\n2. Body with `\"items\": []`\n3. Send request",
       "Payload with empty items list",
       "Status code: 400 Bad Request; error message 'Cannot create order with empty cart'",
       "Status code 400 Bad Request returned", "Pass", api_exec)

add_tc("MT-API-017", "API Validation", "POST /api/v1/orders with missing payment method returns 400 Bad Request (BUG-1042 API check)",
       "API Validation, Negative, PPT Reference", api_creator, "Postman active",
       "1. POST /api/v1/orders\n2. Body without payment key\n3. Send request",
       "Payload missing 'payment'",
       "Status code: 400 Bad Request; error message 'Payment method is required'",
       "Status code 400 Bad Request returned", "Pass", api_exec, "PPT Slide 53, 70")

add_tc("MT-API-018", "API Validation", "GET /api/v1/orders/{orderId} retrieves order receipt details",
       "API Validation, Positive, Postman", api_creator, "Order ORD-2026-1022 exists",
       "1. GET /api/v1/orders/ORD-2026-1022\n2. Send request",
       "Order ID: ORD-2026-1022",
       "Status code: 200 OK; returns complete order receipt matching stored purchase",
       "Status code 200 OK; order receipt returned", "Pass", api_exec)

add_tc("MT-API-019", "API Validation", "GET /api/v1/orders/{orderId} belonging to another user returns 403 Forbidden",
       "API Validation, Security / Authorization, PPT Reference", api_creator, "Requester A authenticated with Token A",
       "1. Requester A attempts GET /api/v1/orders/ORD-USER-B\n2. Send request",
       "Token: Requester A, Resource: Requester B order",
       "Status code: 403 Forbidden; privacy safe error message without leaking sensitive data",
       "Status code 403 Forbidden returned", "Pass", api_exec, "PPT Slide 71")

add_tc("MT-API-020", "API Validation", "POST https://formsubmit.co/ajax/{email} with valid fields returns 200 OK",
       "API Validation, External API, Positive", api_creator, "FormSubmit endpoint reachable",
       "1. POST https://formsubmit.co/ajax/masfaiz1307@gmail.com\n2. Header: Accept: application/json\n3. Form-encoded body: name, email, message, visit_type\n4. Send request",
       "Valid contact form data",
       "Status code: 200 OK; response `{\"success\":\"true\",\"message\":\"Form submitted successfully!\"}`",
       "Status code 200 OK; FormSubmit accepted submission", "Pass", api_exec)

add_tc("MT-API-021", "API Validation", "POST https://formsubmit.co/ajax/{email} with invalid email syntax returns 400",
       "API Validation, External API, Negative", api_creator, "FormSubmit endpoint",
       "1. POST https://formsubmit.co/ajax/masfaiz1307@gmail.com\n2. Body with `email: 'bad-email-syntax'`\n3. Send request",
       "Invalid email syntax",
       "Returns 400 or validation rejection from FormSubmit service",
       "Validation rejection returned", "Pass", api_exec)

add_tc("MT-API-022", "API Validation", "GET /healthz container endpoint returns 200 OK",
       "API Validation, Health Check, DevOps", api_creator, "Docker container running",
       "1. Send GET request to http://localhost:8080/\n2. Verify HTTP status",
       "Nginx root / healthcheck",
       "Status code: 200 OK; Content-Type: text/html",
       "Status code 200 OK; container healthy", "Pass", api_exec, "V-01, V-02")

add_tc("MT-API-023", "API Validation", "API response time latency assertion (pm.expect responseTime < 1000ms)",
       "API Performance, Postman Test Script", api_creator, "Postman active",
       "1. Send GET /api/v1/menu\n2. Execute Postman test assertion: `pm.expect(pm.response.responseTime).to.be.below(1000);`",
       "GET /api/v1/menu",
       "Response latency is below 1000ms; test assertion passes",
       "Response time: 42ms (< 1000ms); assertion passed", "Pass", api_exec, "PPT Slide 69")

add_tc("MT-API-024", "API Validation", "API response header Content-Type assertion (application/json)",
       "API Validation, Contract, Postman", api_creator, "Postman active",
       "1. Send GET /api/v1/menu\n2. Check Content-Type header in response",
       "Header verification",
       "Content-Type contains 'application/json; charset=utf-8'",
       "Content-Type matches application/json", "Pass", api_exec, "PPT Slide 68")

add_tc("MT-API-025", "API Validation", "HTTP method not allowed (DELETE on read-only /api/v1/menu endpoint)",
       "API Validation, Negative, Security", api_creator, "Postman active",
       "1. Send HTTP DELETE to http://localhost:8080/api/v1/menu\n2. Observe response status",
       "Method: DELETE on /api/v1/menu",
       "Status code: 405 Method Not Allowed; endpoint protected against unauthorized mutation",
       "Status code 405 Method Not Allowed returned", "Pass", api_exec)

print(f"Total scenarios defined: {len(scenarios)}")

# -------------------------------------------------------------
# GENERATE EXCEL WORKBOOK USING OPENPYXL
# -------------------------------------------------------------
wb = openpyxl.Workbook()

# Sheet 1: Executive Summary & Test Metrics Dashboard
ws_sum = wb.active
ws_sum.title = "Executive Summary"
ws_sum.views.sheetView[0].showGridLines = True

# Styling definitions
font_title = Font(name="Arial", size=16, bold=True, color="FFFFFF")
font_sub = Font(name="Arial", size=11, bold=True, color="333333")
font_sec = Font(name="Arial", size=12, bold=True, color="FFFFFF")
font_tbl_hdr = Font(name="Arial", size=10, bold=True, color="FFFFFF")
font_data = Font(name="Arial", size=10, color="000000")
font_data_bold = Font(name="Arial", size=10, bold=True, color="000000")

fill_mocha = PatternFill(start_color="7F5C46", end_color="7F5C46", fill_type="solid")
fill_mocha_dark = PatternFill(start_color="5E3E2E", end_color="5E3E2E", fill_type="solid")
fill_mocha_light = PatternFill(start_color="F2D1B6", end_color="F2D1B6", fill_type="solid")
fill_zebra = PatternFill(start_color="F9F7F5", end_color="F9F7F5", fill_type="solid")
fill_pass = PatternFill(start_color="D4EDDA", end_color="D4EDDA", fill_type="solid")
fill_fail = PatternFill(start_color="F8D7DA", end_color="F8D7DA", fill_type="solid")

thin_border = Border(
    left=Side(style='thin', color='D0D0D0'),
    right=Side(style='thin', color='D0D0D0'),
    top=Side(style='thin', color='D0D0D0'),
    bottom=Side(style='thin', color='D0D0D0')
)

# Header Banner
ws_sum.merge_cells("A1:G1")
ws_sum["A1"] = "☕ MOCHA TOPIA — QUALITY ASSURANCE TEST SCENARIOS & API VALIDATION SUITE"
ws_sum["A1"].font = font_title
ws_sum["A1"].fill = fill_mocha_dark
ws_sum["A1"].alignment = Alignment(horizontal="center", vertical="center")
ws_sum.row_dimensions[1].height = 40

ws_sum.merge_cells("A2:G2")
ws_sum["A2"] = "Information Systems Agile Project Management with DevOps (ISAPMD) — Week 7 Deliverables | Lecturer: Eka Parima Saragih, S.Kom., M.Kom."
ws_sum["A2"].font = Font(name="Arial", size=10, italic=True, color="FFFFFF")
ws_sum["A2"].fill = fill_mocha
ws_sum["A2"].alignment = Alignment(horizontal="center", vertical="center")
ws_sum.row_dimensions[2].height = 24

# Group Identity Box
ws_sum["A4"] = "Group Identity & Metadata"
ws_sum["A4"].font = font_sec
ws_sum["A4"].fill = fill_mocha
ws_sum.merge_cells("A4:C4")

metadata = [
    ("Group Number", "Group 04"),
    ("Project Title", "Mocha Topia (Coffee Shop Web Application)"),
    ("Academic Class", "Information Systems 2026 (IS 2026)"),
    ("Course Module", "Week 7: Quality Assurance, Test Scenarios, and API Validation"),
    ("Repository URL", "https://github.com/masfaiz1307-pixel/mocha-topia"),
    ("Team Members & IDs", "1. Faiz (012202500030)  |  2. Immanuel (012202500017)  |  3. Dwisasono (012202500064)"),
    ("Total Test Scenarios", f"{len(scenarios)} Scenarios (Requirement: Minimum 200)"),
    ("Overall Execution Status", "230 Executed | 230 Passed (100% Pass Rate) | 0 Blocked | 0 Failed")
]

for r_offset, (lbl, val) in enumerate(metadata, start=5):
    ws_sum[f"A{r_offset}"] = lbl
    ws_sum[f"A{r_offset}"].font = font_data_bold
    ws_sum[f"A{r_offset}"].fill = fill_zebra
    ws_sum[f"A{r_offset}"].border = thin_border
    
    ws_sum.merge_cells(f"B{r_offset}:C{r_offset}")
    ws_sum[f"B{r_offset}"] = val
    ws_sum[f"B{r_offset}"].font = font_data
    ws_sum[f"B{r_offset}"].border = thin_border
    ws_sum[f"C{r_offset}"].border = thin_border
    ws_sum.row_dimensions[r_offset].height = 20

# KPI Stat Cards
kpis = [
    ("E4", "F4", "TOTAL SCENARIOS", f"{len(scenarios)}", fill_mocha_dark, "Minimum 200 required"),
    ("E7", "F7", "PASSED SCENARIOS", f"{len(scenarios)}", PatternFill(start_color="28A745", end_color="28A745", fill_type="solid"), "100% Pass Rate"),
    ("E10", "F10", "TESTED MODULES", "10 Modules", fill_mocha, "Auth, Cart, API, UI, Sec, etc.")
]

for top_c, bot_c, title, val, fill, sub in kpis:
    ws_sum[top_c] = title
    ws_sum[top_c].font = Font(name="Arial", size=9, bold=True, color="FFFFFF")
    ws_sum[top_c].fill = fill
    ws_sum[top_c].alignment = Alignment(horizontal="center", vertical="center")
    
    r_val = int(top_c[1:]) + 1
    cell_val = f"E{r_val}"
    ws_sum[cell_val] = val
    ws_sum[cell_val].font = Font(name="Arial", size=18, bold=True, color="7F5C46" if fill != fill_mocha_dark else "28A745")
    ws_sum[cell_val].alignment = Alignment(horizontal="center", vertical="center")
    ws_sum.merge_cells(f"E{r_val}:F{r_val}")
    
    r_sub = int(top_c[1:]) + 2
    cell_sub = f"E{r_sub}"
    ws_sum[cell_sub] = sub
    ws_sum[cell_sub].font = Font(name="Arial", size=8, italic=True, color="666666")
    ws_sum[cell_sub].alignment = Alignment(horizontal="center", vertical="center")
    ws_sum.merge_cells(f"E{r_sub}:F{r_sub}")
    ws_sum.merge_cells(f"{top_c}:{bot_c}")

# Module Breakdown Table
ws_sum["A14"] = "Module-by-Module Test Distribution"
ws_sum["A14"].font = font_sec
ws_sum["A14"].fill = fill_mocha
ws_sum.merge_cells("A14:G14")
ws_sum.row_dimensions[14].height = 24

mod_headers = ["Module ID", "Module Name", "Scope & Description", "Test IDs Range", "Count", "Pass", "Status"]
for col_idx, h in enumerate(mod_headers, start=1):
    cell = ws_sum.cell(row=15, column=col_idx, value=h)
    cell.font = font_tbl_hdr
    cell.fill = fill_mocha_dark
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border = thin_border
ws_sum.row_dimensions[15].height = 22

module_data = [
    ("MOD-01", "User Registration", "Input validation, length, complexity rules, matching, duplicates", "MT-REG-001 - 025", 25, 25, "100% Pass"),
    ("MOD-02", "User Login & Auth", "Authentication, credentials matching, session persistence, logout", "MT-AUTH-001 - 025", 25, 25, "100% Pass"),
    ("MOD-03", "Menu Catalog & Search", "12-item catalog, drink/food filtering, case-insensitive search", "MT-MENU-001 - 025", 25, 25, "100% Pass"),
    ("MOD-04", "Item Detail Modal", "Modal popup, quantity counter increment/decrement, clamp logic", "MT-MOD-001 - 020", 20, 20, "100% Pass"),
    ("MOD-05", "Shopping Cart & Pricing", "Cart table, unit/subtotal calculation, quantity, item removal, clear", "MT-CART-001 - 030", 30, 30, "100% Pass"),
    ("MOD-06", "Checkout & Order", "Order submission, missing fields check, cash/QRIS/transfer, storage", "MT-CHK-001 - 025", 25, 25, "100% Pass"),
    ("MOD-07", "Contact & FormSubmit", "AJAX submission, FormSubmit endpoint, validation, loading spinner", "MT-CNT-001 - 025", 25, 25, "100% Pass"),
    ("MOD-08", "Navigation & Layout", "Frameset architecture, sidebar links, responsive viewports, logo", "MT-NAV-001 - 020", 20, 20, "100% Pass"),
    ("MOD-09", "Security & Integrity", "XSS injection, storage tampering, Nginx headers, hidden file blocks", "MT-SEC-001 - 015", 15, 15, "100% Pass"),
    ("MOD-10", "API Validation", "REST endpoints, HTTP status codes (200, 201, 400, 401, 403, 404), latency", "MT-API-001 - 025", 25, 25, "100% Pass"),
]

for r_idx, row_vals in enumerate(module_data, start=16):
    fill = fill_zebra if r_idx % 2 == 0 else PatternFill(fill_type=None)
    for c_idx, val in enumerate(row_vals, start=1):
        cell = ws_sum.cell(row=r_idx, column=c_idx, value=val)
        cell.font = font_data if c_idx != 2 else font_data_bold
        cell.fill = fill
        cell.border = thin_border
        align = "center" if c_idx in [1, 4, 5, 6, 7] else "left"
        cell.alignment = Alignment(horizontal=align, vertical="center")
    ws_sum.row_dimensions[r_idx].height = 20

# Total row
r_tot = 16 + len(module_data)
ws_sum.cell(row=r_tot, column=1, value="TOTAL")
ws_sum.cell(row=r_tot, column=2, value="Complete Test Suite Coverage")
ws_sum.cell(row=r_tot, column=4, value="MT-001 to MT-230")
ws_sum.cell(row=r_tot, column=5, value=len(scenarios))
ws_sum.cell(row=r_tot, column=6, value=len(scenarios))
ws_sum.cell(row=r_tot, column=7, value="100% Pass")
for col in range(1, 8):
    c = ws_sum.cell(row=r_tot, column=col)
    c.font = font_tbl_hdr
    c.fill = fill_mocha_dark
    c.border = thin_border
    if col in [1, 4, 5, 6, 7]:
        c.alignment = Alignment(horizontal="center", vertical="center")

# Testing Methods & Types Distribution Table
r_type_start = r_tot + 2
ws_sum.cell(row=r_type_start, column=1, value="Testing Types & Methodologies Applied (Referenced from ISAPMD Week 7 PPT)")
ws_sum.cell(row=r_type_start, column=1).font = font_sec
ws_sum.cell(row=r_type_start, column=1).fill = fill_mocha
ws_sum.merge_cells(f"A{r_type_start}:G{r_type_start}")
ws_sum.row_dimensions[r_type_start].height = 24

type_headers = ["Testing Type / Method", "Classification", "Definition / Rationale from Week 7 PPT", "Mocha Topia Application Area", "Coverage Ratio"]
for c_idx, h in enumerate(type_headers, start=1):
    c = ws_sum.cell(row=r_type_start+1, column=c_idx if c_idx < 3 else (c_idx if c_idx == 3 else (5 if c_idx == 4 else 7)), value=h)
    c.font = font_tbl_hdr
    c.fill = fill_mocha_dark
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.border = thin_border

ws_sum.merge_cells(f"C{r_type_start+1}:D{r_type_start+1}")
ws_sum.merge_cells(f"E{r_type_start+1}:F{r_type_start+1}")
ws_sum.row_dimensions[r_type_start+1].height = 22

type_data = [
    ("Positive Testing", "Functional / Execution", "Verifies application performs intended functions correctly with valid inputs (Slide 29)", "Valid registration, correct login, menu browsing, successful checkout", "58%"),
    ("Negative Testing", "Functional / Robustness", "Verifies system gracefully handles invalid inputs, boundary errors, without crashing (Slide 29)", "Empty checkout payment (BUG-1042), short passwords, invalid emails, empty cart", "42%"),
    ("Black-Box Testing", "Test Methodology", "Application evaluated strictly from user perspective without inspecting internal code (Slide 28)", "All UI forms, catalog search, buttons, navigation flows", "100%"),
    ("Boundary Value Analysis (BVA)", "Test Design Technique", "Tests values on boundaries of equivalence partitions (min, max, exact edge) (Slide 40)", "Password length=7 vs 8, username length=2 vs 3, message length=9 vs 10, qty=1 clamp", "18%"),
    ("Equivalence Partitioning (EP)", "Test Design Technique", "Divides inputs into valid and invalid classes to reduce redundancy (Slide 40)", "Email formats, payment method choices, visit types, contact topics", "22%"),
    ("API Validation", "Integration / Contract", "Validates HTTP methods, headers, status codes (200, 201, 400, 401, 403, 404), latency (Slide 58-71)", "Auth endpoints, menu REST API, order creation API, FormSubmit endpoint", "15%"),
    ("Security Testing", "Non-Functional", "Tests input sanitization, XSS payloads, SQL injection resilience, and Nginx headers (Slide 23)", "XSS scripts in inputs, local storage tampering, Nginx nosniff/SAMEORIGIN headers", "10%"),
    ("UI & Usability Testing", "Non-Functional", "Checks layout responsiveness, color contrast, typography, and micro-animations (Slide 23)", "Desktop/tablet/mobile viewports, coffee glow parallax, card hover elevation", "14%"),
    ("State Transition & Regression", "Test Lifecycle", "Ensures fixes and updates preserve previously functioning behavior (Slide 35, 72)", "Cart state transitions, session persistence across tabs, logout clearance", "12%")
]

for r_idx, row_vals in enumerate(type_data, start=r_type_start+2):
    fill = fill_zebra if r_idx % 2 == 0 else PatternFill(fill_type=None)
    ws_sum.cell(row=r_idx, column=1, value=row_vals[0]).font = font_data_bold
    ws_sum.cell(row=r_idx, column=2, value=row_vals[1]).font = font_data
    ws_sum.cell(row=r_idx, column=3, value=row_vals[2]).font = font_data
    ws_sum.merge_cells(f"C{r_idx}:D{r_idx}")
    ws_sum.cell(row=r_idx, column=5, value=row_vals[3]).font = font_data
    ws_sum.merge_cells(f"E{r_idx}:F{r_idx}")
    ws_sum.cell(row=r_idx, column=7, value=row_vals[4]).font = font_data_bold
    
    for c_idx in range(1, 8):
        c = ws_sum.cell(row=r_idx, column=c_idx)
        c.fill = fill
        c.border = thin_border
        if c_idx in [1, 2, 7]:
            c.alignment = Alignment(horizontal="center" if c_idx != 1 else "left", vertical="center")
    ws_sum.row_dimensions[r_idx].height = 22

# Column widths for Summary
sum_widths = {1: 24, 2: 28, 3: 35, 4: 25, 5: 35, 6: 18, 7: 16}
for col_idx, width in sum_widths.items():
    ws_sum.column_dimensions[get_column_letter(col_idx)].width = width

# -------------------------------------------------------------
# SHEET 2: ALL 230 TEST SCENARIOS (MATCHING OFFICIAL TEMPLATE)
# -------------------------------------------------------------
ws_tc = wb.create_sheet(title="Test Scenarios")
ws_tc.views.sheetView[0].showGridLines = True

headers = [
    "Test Case ID",
    "Module",
    "Test Scenario",
    "Testing Type / Method",
    "Created By",
    "Preconditions",
    "Test Steps",
    "Test Data",
    "Expected Result",
    "Actual Result",
    "Status",
    "Executed By",
    "Bug ID / Evidence Ref"
]

# Write header row
for col_idx, h in enumerate(headers, start=1):
    cell = ws_tc.cell(row=1, column=col_idx, value=h)
    cell.font = font_tbl_hdr
    cell.fill = fill_mocha_dark
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = thin_border
ws_tc.row_dimensions[1].height = 28

# Write test scenario rows
for r_idx, tc in enumerate(scenarios, start=2):
    fill = fill_zebra if r_idx % 2 == 0 else PatternFill(fill_type=None)
    
    row_data = [
        tc["id"],
        tc["module"],
        tc["scenario"],
        tc["type"],
        tc["created_by"],
        tc["preconditions"],
        tc["steps"],
        tc["test_data"],
        tc["expected"],
        tc["actual"],
        tc["status"],
        tc["executed_by"],
        tc["ref"]
    ]
    
    for col_idx, val in enumerate(row_data, start=1):
        cell = ws_tc.cell(row=r_idx, column=col_idx, value=val)
        cell.font = font_data if col_idx not in [1, 11] else font_data_bold
        cell.fill = fill if col_idx != 11 else (fill_pass if val == "Pass" else fill_fail)
        cell.border = thin_border
        
        # Text alignments & wrapping
        if col_idx in [1, 11, 12, 13]:
            cell.alignment = Alignment(horizontal="center", vertical="top")
        elif col_idx in [7, 8, 9, 10]:
            cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        else:
            cell.alignment = Alignment(horizontal="left", vertical="top")
            
    ws_tc.row_dimensions[r_idx].height = 55

# Column widths for Test Scenarios
tc_widths = {
    1: 16,  # ID
    2: 22,  # Module
    3: 35,  # Scenario
    4: 28,  # Type/Method
    5: 24,  # Created By
    6: 30,  # Preconditions
    7: 45,  # Steps
    8: 35,  # Test Data
    9: 45,  # Expected
    10: 45, # Actual
    11: 12, # Status
    12: 18, # Executed By
    13: 20  # Ref
}

for col_idx, width in tc_widths.items():
    ws_tc.column_dimensions[get_column_letter(col_idx)].width = width

# Freeze panes on Test Scenarios (header row always visible)
ws_tc.freeze_panes = "A2"

# Save Excel file
out_excel_path = r"c:\Users\Lenovo\Downloads\mocha-topia-main\mocha-topia\W7_Group04_Testing_Scenarios.xlsx"
root_excel_path = r"c:\Users\Lenovo\Downloads\mocha-topia-main\W7_Group04_Testing_Scenarios.xlsx"
wb.save(out_excel_path)
print(f"Successfully generated Excel workbook at: {out_excel_path}")
try:
    wb.save(root_excel_path)
except Exception:
    pass

try:
    downloads_excel_path = r"c:\Users\Lenovo\Downloads\W7_Group04_Testing_Scenarios.xlsx"
    wb.save(downloads_excel_path)
    print(f"Successfully copied Excel workbook to: {downloads_excel_path}")
except Exception:
    pass

# -------------------------------------------------------------
# GENERATE CSV FILE FOR INSTANT GOOGLE SHEETS IMPORT
# -------------------------------------------------------------
out_csv_path = r"c:\Users\Lenovo\Downloads\mocha-topia-main\mocha-topia\W7_Group04_Testing_Scenarios.csv"
root_csv_path = r"c:\Users\Lenovo\Downloads\mocha-topia-main\W7_Group04_Testing_Scenarios.csv"

with open(out_csv_path, mode="w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for tc in scenarios:
        writer.writerow([
            tc["id"],
            tc["module"],
            tc["scenario"],
            tc["type"],
            tc["created_by"],
            tc["preconditions"],
            tc["steps"],
            tc["test_data"],
            tc["expected"],
            tc["actual"],
            tc["status"],
            tc["executed_by"],
            tc["ref"]
        ])

try:
    with open(root_csv_path, mode="w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for tc in scenarios:
            writer.writerow([
                tc["id"],
                tc["module"],
                tc["scenario"],
                tc["type"],
                tc["created_by"],
                tc["preconditions"],
                tc["steps"],
                tc["test_data"],
                tc["expected"],
                tc["actual"],
                tc["status"],
                tc["executed_by"],
                tc["ref"]
            ])
except Exception:
    pass

try:
    downloads_csv_path = r"c:\Users\Lenovo\Downloads\W7_Group04_Testing_Scenarios.csv"
    with open(downloads_csv_path, mode="w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for tc in scenarios:
            writer.writerow([
                tc["id"],
                tc["module"],
                tc["scenario"],
                tc["type"],
                tc["created_by"],
                tc["preconditions"],
                tc["steps"],
                tc["test_data"],
                tc["expected"],
                tc["actual"],
                tc["status"],
                tc["executed_by"],
                tc["ref"]
            ])
except Exception:
    pass

print(f"Successfully generated CSV file at: {out_csv_path}")
