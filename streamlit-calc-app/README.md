# Streamlit Calculation App

This project is a Streamlit application designed to perform various calculations based on user inputs. It features a user-friendly interface with two separate tabs for different calculation functionalities.

## Project Structure

```
streamlit-calc-app
├── src
│   ├── app.py                # Main entry point of the Streamlit application
│   ├── views
│   │   ├── calculation_tab1.py  # First calculation tab implementation
│   │   └── calculation_tab2.py  # Second calculation tab implementation
│   └── utils
│       └── calculations.py    # Utility functions for calculations
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-calc-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application, execute the following command in your terminal:

```
streamlit run src/app.py
```

This will start the Streamlit server and open the application in your default web browser.

## Features

- Two calculation tabs, each with its own set of user inputs and calculations.
- Easy-to-use interface for performing calculations.
- Modular design with separate files for views and utility functions.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.