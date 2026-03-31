Project overview:
Developing this function went well considering I've never had to write a browser automation script before nor have I worked with playwright, luckily I'm a fast learner.
I'm happy with what I have produced and believe there should be no problems.
Was fun to learn playwright, very useful tool.

Documentation:
Setup instructions
  - Have both abn_lookup.py and main.py in same dir.
  - Have playwright and playwright browser extensions installed.
  - Execute main.

How to run script
 Headless is set to false so the browser will pop up to show it's working.
  - cd into abn-lookup dir containing both abn_lookup.py and main.py
  - call main with "python main.py" in terminal.
  - You will be prompted to enter an ABN (can also enter a business name).
  - As main runs, the script will gather the business details and a screenshot.
  - The terminal will the prompt for a screenshot name and a json file name.
  - Json will save in the main dir and screenshots have their own dir that will generate after the first execution of main.py

Any Assumptions:
The assumptions made include
  - The person executing the code has a python interpreter
  - Has Playwright installed
  - Has playwright broswer extentions installed(chromium in particular for my script)

AI use in workflow:
  - The way I used AI in my workflow was combining online video tutorials with AI tools to quickly understand how playwright works.
  - This allowed me to tackle the problem quicker than if I needed to rely on just video tutorials alone.
