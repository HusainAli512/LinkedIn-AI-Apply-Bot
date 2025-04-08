# Job Application Bot 🚀
### Video Tutorial 🎥

[Click here to watch the Job Application Bot demo](./media/linkedinaibotauto.mp4)



This project automates the process of applying for jobs on LinkedIn using **Selenium** and **Gemini** to dynamically fill out application forms. The bot filters job listings, navigates through various application steps, and submits the job applications.

### Features ✨
- **Job Filtering**: Automatically filters job listings based on job name and applies the "Easy Apply" filter.
- **Dynamic Form Filling**: Uses Gemini model-generated responses to dynamically fill out form fields (text inputs, radio buttons, dropdowns).
- **Navigation**: Handles navigating through multiple pages of the job application process, including clicking the next buttons, selecting radio options, and submitting forms.
- **Automated Job Submission**: The bot automatically submits job applications, handling various job application steps with ease.

### Technologies Used ⚙️
- **Selenium**: For browser automation (navigating pages, interacting with forms, clicking buttons).
- **Gemini Model**: Generates human-like responses to fill out the application forms dynamically.
- **Python**: The primary language used for scripting the automation.

### How It Works 🤖
1. The bot navigates to LinkedIn's job section.
2. It filters jobs based on the specified job name and applies the "Easy Apply" filter.
3. It then proceeds to each job listing, filling in the necessary application fields by interacting with form elements such as text inputs, radio buttons, and dropdowns.
4. After filling the form, the bot clicks through multiple "Next" buttons and submits the job application.
5. It continues until the "Done" button is clicked, indicating the completion of the application.
