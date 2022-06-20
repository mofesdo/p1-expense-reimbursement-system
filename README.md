# Project 1
### Overall General requirement:
You are tasked with creating an expense reimbursement system for a small company/group. 
This program will allow employees to create reimbursement requests for their business expenditures, 
while also providing a way to track the amount of money they have spent.

### Our Chosen Theme to Flavor the Requirement:
Our app is built for a fantasy pirate crew aboard a battle-hardened ship, where the Captain and
First Mate serve as "managers." Swabbies, deckhands, and other sailors are regarded as "employees."
Whenever the ship takes anchor at port in Nassau, Havana, or any other coastal city, the ever
lively and nautical crew aboard the ship takes to town to buy supplies. These supplies can
include anything from medical supplies, food, ship repair materials, and pirate battle gear to
maritime favorites like pet parrots, rum, eye patches, and hooked prosthetic hands.

Crew mates make purchases with their own funds, aka their share of the loot, and can be issued 
reimbursements out of the surplus loot from the last raid. The reason that they put for the
reimbursement request has to be good though, or else the captain might not approve it. For
example, if Deckhand Flapjack is always having too much rum and making a mess on deck, then
Captain Blackbeard may choose not to reimburse poor Flapjack for buying Rum.
But if Edward Kenway, the swabbie
that everyone knows is showing promise, buys wooden planks to repair the ship, the captain
would feel more compelled to reimburse him.

## Key Features

- Employees/sailors can:
    - Log into an account/session with unique credentials
    - Submit reimbursement requests with a description and dollar amount
      - Bonus completed: requests are categorized by urgency level
    - See ongoing and previous requests
    - Cancel ongoing requests


- Managers/Captain/First-Mate:
  - Have all the same features as Employees
  - Can approve/deny requests


- Additional Features:
  - Users can sort requests by date, ascending or descending
  - Users can filter requests by request status and urgency

- Security Features:
  - Session token is checked before main API is served on most calls/requests
  - All requests to manager parts of API are checked to see if user is a manager
  - SQL injection protection established through Psycopg
  - Input validation via Regex and supporting logic


## Business Requirements Met

- Requests must be for $1-$1000, via UI and direct requests
- Requests descriptions can be 100 characters, max
- Reimbursement requests are represented using multiple numbers


