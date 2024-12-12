## Sample Python/Django Project

## Overview

This project is aimed at transforming the thesis project management system at Tribhuvan University (TU) by developing a dynamic web application using Django. The new system will replace the current, inefficient mix of email, Excel, and Word documents with a streamlined, interactive platform that enhances collaboration and efficiency for students, supervisors, and the Unit Coordinator.

## Table of Contents

- [Background](#background)
- [Current System](#current-system)
- [Pain Points](#pain-points)
- [Key Functionalities](#key-functionalities)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Current System

The current thesis project management process involves:

- Emailing and updating spreadsheets for thesis topics.
- Manual email exchanges for topic selection and supervisor approvals.
- Submitting signed supervision agreements via Learnline.

## Pain Points

The current system has several key pain points:

1. **Inefficient Workflow**: Manual processes are repetitive and error-prone.
2. **Supervisor Capacity Blind Spot**: Students often face disappointments due to hidden limitations in supervisor capacity.
3. **Form Errors and Delays**: Frequent errors in standard forms require time-consuming corrections.
4. **Manual Data Management**: Redundant updates and double data entry create unnecessary complexity.

## Key Functionalities

1. **Enhanced Efficiency**: Centralized workflows and automation reduce manual tasks and errors.
2. **Improved Communication**: A shared platform fosters transparent communication among all stakeholders.
3. **Accessibility**: The web-based application can be accessed from anywhere, anytime, on various devices.
4. **Data Integrity**: Secure data storage and access controls protect student and project information.

## Demo

https://github.com/user-attachments/assets/dc44dc16-8f2f-48dc-8d5e-23eb85cad44e

## 🚀 Getting Started

### Open Using Daytona

1. **Install Daytona**: Follow the [Daytona installation guide](https://www.daytona.io/docs/installation/installation/).
2. **Create the Workspace**:
   ```bash
   daytona create  https://github.com/SusheelThapa/Project-Management
   ```
3. **Start the Application**:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the website at `http://127.0.0.1:8000/login` to view available thesis topics.
2. For interactive functionalities, log in with your supervisor, student, or Unit Coordinator credentials.
3. Supervisors can manage thesis topics, students can apply for projects, and the Unit Coordinator can oversee the entire process.

## Credentials

1. Coordinator
   ```
   charlas@gmail.com
   Test@123
   ```
2. Supervisor

   ```
   sami@gmail.com
   Test@123
   ```

   ```
   yakub@gmail.com
   Test@123
   ```

   ```
   asif@gmail.com
   Test@123
   ```

   ```
   bharanidharan@gmail.com
   Test@123
   ```

3. Student

   ```
   nirmal@gmail.com
   Test@123
   ```

   ```
   binish@gmail.com
   Test@123
   ```

   ```
   sofian@gmail.com
   Test@123
   ```

   ```
   preson@gmail.com
   Test@123
   ```

## Recommended Workflow

1. Login via the Coordinator Account(**charlas@gmail.com**) so that you see the option to accept or reject project added by different supervisor.
2. Then, accept some of the project and reject some project. (_Accept one project of the Sami Azam and Reject another project of Sami Azam_)
3. Logout by clicking the usef profile badge which will display a tool tip to logout
4. Login via supervisor account(**sami@gmail.com**)
   5.You will see one project has the status **approved** and another has **rejected**. _But you cannot see any student application._
5. Logout and Login via Student account(**nirmal@gmail.com**). You will see an option to create group and join group. Click on create group and create a group with name **Team Alpha**. Then you will be able to see a dashboard where you can apply for the project.
6. Logout and Login via another Student account(**binish@gmail.com**)
7. Click on join group and join the **Team Alpha** group. Then click and apply to apply for the following project(*Make sure to apply the project with supervisor **Sami Azam***).
8. Logout and Login via Sami Azam. And you will notice a student application on one project and you can view the application too.
