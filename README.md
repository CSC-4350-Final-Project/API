# **Project Name:** Event Planner

# **API: Ticketmaster API**
**Heroku link to app:** https://csc4350-final-project-ui.herokuapp.com/login <br>
***
**Links to our project repositories:**<br>
1. https://github.com/CSC-4350-Final-Project/UI (Frontend)
2. https://github.com/CSC-4350-Final-Project/API (Backend)
***
 
# **TicketMaster API**
Register for an API here: https://developer-acct.ticketmaster.com/user/register

*Upon registration and obtaining your API key, you will be able to access our Discovery APIs instantly. Using these APIs allows you to create a meaningful event discovery experience for your fans. <br>
*Link: https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/

*Ticketmaster APIs work against many platforms including Ticketmaster, TicketWeb, Universe, FrontGate, Ticketmaster Resale (TMR) and many more.

**Authentication:** <br>
To run a successful API call, you will need to pass your API Key in the apikey query parameter. Your API Key should automatically appear in all URLs throughout this portal.

**Example:** https://app.ticketmaster.com/discovery/v2/events.json?apikey={apikey}

**Base URL:** https://app.ticketmaster.com/discovery/v2/

**Event Resource:** <br>
The API provides access to content sourced from various platform, including Ticketmaster, Universe, FrontGate Tickets and Ticketmaster Resale (TMR). By default, the API returns events from all sources. To specify a specifc source(s), use the &source= parameter. Multiple, comma separated values are OK.

**Event Coverage:** <br>
With over 230K+ events available in the API, coverage spans different countries, including United States, Canada, Mexico, Australia, New Zealand, United Kingdom, Ireland, other European countries, and more. More events and more countries are added on continuous basis.

**Event Limits**
-The default quota is 5000 API calls per day and rate limitation of 5 requests per second. <br>
-Deep Paging: we only support retrieving the 1000th item. i.e. ( size * page < 1000)

***

# **Technologies:**
**Front-end:** ReactJS <br>
**Back-end:** Python Flask framework <br>
**Database:** PostgresSQL (SQALchemy) <br>
**Deployment:** Heroku <br>
**VSCode:** Code editor<br>
Command Line Interface (CLI) for file navigation. <br>
**Git/Github:** Manage source code and team collaboration with **Git via the CLI:** and used **Github** to store codebase.<br>
**Github Action:** for automatically run linter and tests for both client and server whenever somebody pushes/pull requests to the main branch.<br>
**Github Projects:** for break up the user stories into tasks and assign each of them to a member. All work must be on this board and up to date so the team knows what is being worked on.
***

# **Modules**
-**OS** module <br>
-**Flask** - request, jsonify <br>
-**Dotenv** - find_dotenv, loaddotenv <br>
-**Werkzeug.security** - check_password_hash <br>
-**Flask_cors** - CORS <br>
-**Flask_jwt_extended** - create_access_token, JWTManager, get_jwt_identity,verify_jwt_in_request <br>
-**Datetime** - timedelta


***

# **Formatting**
**Black Formatter** <br>
**ESlint** <br>
**AirBnB Rules**<br>

***

# **.env Configuration**
Create a `.env` file in your /API directory, and add the following key value pairs:<br>
    **1. DATABASE_URL** <br>
    2. (Optional) - include the key/value pair `DEBUG=True` to have the flask server run in debug mode <br>
    **3. SECRET_KEY** (App's unique key) <br>
    **4. TM_API** - Ticketmaster API key <br>

***
# **Linting**
1. We've disabled # pylint: disable=no-member in order for pylint to not complain about SQLAlchemy errors. <br>
2. We had to ignore eslint for no-alert, as we need to be able to show alerts on the front-end.<br>
3. We had to disable no-underscore-dangle because the api returns some properties with an underscore in front of them.<br>
***
# **Setup Guide**
### **Clone/fork the project:** <br>
>1. Open the main page of the repository in browser. click **Clone** or **Download**. <br>

>2. Click the **Copy** icon to copy the clone **URL** for the repository. <br>
>3. Launch Terminal(MacOS) or Command Prompt(Windows)<br>

>4. Type **'cd'** and the **directory location** where you want the cloned directory to be made. <br> **Example:** cd PATH-TO-LOCATION <br>

>5. Type **“git clone”**, and then paste the **URL** you copied in step 2. Press Enter. The local clone will be created.<br> **Example:** git clone URL

>6. After this step, you will have the repository cloned to the PATH you inserted earlier.
<br>

***
# Getting Started
1. run `pip3 install -r requirements.txt` to install required dependencies
2. Make sure you have 'pip' and 'python' installed to the latest versions.

***
# Heroku Setup
Login to Heroku, create and deploy the app**<br>
>heroku login<br>
**Note:** follow instructions on screen<br>

>heroku create<br>
**Note:** 2 links will generate. First link is the actual app URL. Second link is the repository URL

>git push heroku main<br>
>**Note:** pushing and deploy app


**Important files to be on the lookout for. These files must be named to the exact wording prior to a successful deployment:**<br>
>1. **requirements.txt** (contains Flask, requests, python-dotenv)<br>
>2. **.gitignore** (contains '.env', this means to store the .env file to later be ignored.)<br>
>3. **.env** (contains secret API key(s))<br>
>4. **Procfile** (contains 'web: python app.py' line)<br>
***
# **Database Setup**
**These actions are done on the Command Line/WSL**
1. Log into Heroku: heroku login -i
2. Create new Heroku app: heroku create
3. Run this command: heroku addons:create heroku-postgresql:hobby-dev (Note: if this command alone gives you an error, add "-a your-app-name" right after it.)
**Example: heroku addons:create heroku-postgresql:hobby-dev -a hello-world-12345**
4. Run: heroku config and copy the DATABASE_URL value
5. Enter "export DATABASE_URL='**copy-paste-value-in-here**'" in the Terminal/WSL
6. Replace **postgres** with **postgresql** in your DATABASE_URL

***

# Installing **npm via homebrew**
**Checking if brew is already installed in your machine:**
>brew -v<br>

**If not installed, run this command in your terminal:**
>/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/
Homebrew/install/master/install)"

**Once installed, run these commands:**
>brew update<br>

>brew install node

**Confirm Node.js version**
>node -v

**Confirm NPM version**
>npm -v

***
# **Getting Started with Creating a React App**

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## **Available Scripts**

In the project directory, you can run:

>### `npm start`
>Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.<br>
>The page will reload when you make changes.\
You may also see any lint errors in the console.

>### `npm test`
>Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

>### `npm run build`
>Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.<br>
>The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!<br>
>See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

>### `npm run eject`
>**Note: this is a one-way operation. Once you `eject`, you can't go back!**<br>
*If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.<br>
*Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.<br>
*You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## **Learn More**

>You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

>To learn React, check out the [React documentation](https://reactjs.org/).

### **Code Splitting**

>This section can be found [here](https://facebook.github.io/create-react-app/docs/code-splitting)

### **Analyzing the Bundle Size**

>This section can be found [here](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### **Making a Progressive Web App**

>This section can be found [here](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### **Advanced Configuration**

>This section can be found [here](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### **Deployment**

>This section can be found [here](https://facebook.github.io/create-react-app/docs/deployment)

### **`npm run build` fails to minify**

>This section can be found [here](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
​

***


























