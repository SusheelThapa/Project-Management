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
