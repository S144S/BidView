<p align="center">
  <img src="assets/images/bidview_logo_250x150.png" alt="Logo" width="200"/>
</p>

# BidView - Track your bids
A freelancer who tracks and analyzes his/her proposals is a freelancer who gets projects one after another.

## Description
*BidView* is a tool designed for freelancers to keep track of their bids across different projects.
With *BidView*, you can easily monitor how many bids you've sent, the countries to which you've sent bids, the date of your first bid, and more. This tool helps freelancers organize and analyze their bidding activity to optimize their efforts and increase their chances of success.
In the current version, this tool is very suitable for tracking bids in **Upwork**, but with your help, it will soon be developed for other platforms as well.
#### Technologies:
* Python
* Dash
* Pandas
* Plotly
* Bootstrap


## How to Run the BidView
As long as we transfer *BidView* to the cloud servers and it is available online to everyone, you can run it locally for yourself.

#### Step 1: Cloning
**This project is implemented with Python, make sure you have Python 3.10 or higher on your system.**

Download [latest release](https://github.com/S144S/BidView/archive/refs/tags/v1.2.0.zip) of the BidView

or
`git clone https://github.com/S144S/BidView.git`

or
`git clone git@github.com:S144S/BidView.git`

then go to BidView directory.

#### Last Step if you're using Windows
Just double-click on ran.bat file 😊.

#### Step 2: Change settings based on your desired
1. make a copy of .env.sample
2. change .env.sample to .env
3. Open .env file with any editor you want(even notepad)
4. Feel free to change DEFUALT_BIDDER, CATEGORIES and PROPOSAL_VERSION with your desire as in the existing example
5. Keep the rest unchanged

#### Step 3: Set Up Virtual Environment
Before running the BidView, you need to set up a virtual environment to manage the project's dependencies. Follow the instructions for your operating system below:
##### Windows
1. Open the cmd in BidView directory
2. write `virtualenv .venv` and wait to complete
3. activate your virtual environment with `.\venv\Scripts\activate`
##### Mac and Linux
1. Open a terminal in BidView directory
2. write `python3 -m venv .venv` and wait to complete
3. activate your virtual environment with `source venv/bin/activate`

Now you shoud install required packages with `pip install -r requirements.txt` in your venv termianl.
Now everything is ready!

#### Step 4: Run the App
1. write `python app.py` in your venv terminal
2. Once the application is running, open your web browser and navigate to: `http://127.0.0.1:8050/`
3. Enjoy 😉


## Contributing to the BidView
I welcome contributions to improve the BidView project! If you would like to contribute, please follow these steps:

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your feature or bug fix.
3. Please follow the Python PEP8 standards in your codes. I used Flake8 and iSort tools myself. Also, don't forget to comment 😊.
4. Make your changes and commit them with clear and concise messages, I would be very grateful if you use [this](https://github.com/ariopulse/Ario-Enhancement-Proposal/blob/main/AGEP-Commits.md) instruction for commits, but don't bother yourself too much.
5. Push your changes to your fork and submit a pull request.

Please prioritize resolving issues listed in the[ project issues](https://github.com/S144S/BidView/issues), This helps maintain stability and ensures that key functionalities are working correctly


## License
This project is licensed under the GNU General Public License v3.0. For more details, see the [LICENSE file](https://github.com/S144S/BidView/blob/main/LICENSE).


---
Thank you for your interest in BidView! I look forward to your contributions.