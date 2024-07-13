# Lost Item Notification Flask App

This is a Flask application that allows users to send emails about lost items using a form. The form captures details about the lost item and sends a formal notification email to the specified recipient.

## Features

- Capture details of the lost item, including description, model, item, location, date, and contact information.
- Send a formal notification email with the captured details.
- Secure email configuration using environment variables.

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone this repository to your local machine using:

```bash
git clone https://github.com/LAKSHDGR8/FormToEmail.git
cd your-repo-name
```
### Step 2: Set Up a Virtual Environment

Set up a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the root directory of your project and add your email credentials:

```
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-specific-password
```

#### How to Generate an App-Specific Password for Gmail

1. **Go to your Google Account:**
   - Visit [Google Account](https://myaccount.google.com/).

2. **Navigate to Security:**
   - On the left navigation panel, click **Security**.

3. **App Passwords:**
   - Under the "Signing in to Google" section, if 2-Step Verification is already turned on, you will see an "App Passwords" option. Click on **App Passwords**.
   - You might need to sign in to your Google account again.

4. **Generate App Password:**
   - In the "Select app" dropdown, choose **Other (Custom name)**.
   - Enter a name for your app (e.g., "Flask App").
   - Click **Generate**.
   - Google will provide you with a 16-character app password. Copy this password and paste it into your `.env` file.

### Step 5: Run the Flask Application

1. **Activate the virtual environment:**

   If you haven't already activated the virtual environment, you can do so with the following command:

   ```bash
   source venv/bin/activate
   ```

2. **Run the Flask application:**

   Start the Flask application using the following command:

   ```bash
   flask run
   ```

3. **Access the application:**

   Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
 to see the application in action.

### Step 6: Testing the Application

1. **Fill out the form:**
   - Enter the recipient's email address.
   - Provide the description of the lost item (e.g., color, case color, or design).
   - Enter the brand and model of the lost item.
   - Specify the item type (e.g., phone, wallet).
   - Choose the location where the item was lost from the dropdown.
   - Select the date when the item was lost using the date picker.
   - Provide your phone number and email address for contact.
   - Enter your name, semester, and section.

2. **Submit the form:**
   - Click the "Send Email" button to send the notification email. You should see a confirmation message indicating whether the email was sent successfully.
