# Book-Recomendation

## Repository Content

In this repository you’ll find the “Book Recommendation” Machine Learning project, which uses the k‐Nearest Neighbors algorithm from scikit‐learn to generate the best book recommendations based on a book’s title and its reviews. The project covers everything from collecting and preprocessing book data and reviews to validating the built model via a test. Additionally, the `notebooks` folder contains the full project notebook associated with earning the “Machine Learning with Python” certification.

## Technologies Used

- Language: Python
- Libraries: Scikit-Learn, Pandas, Requests, Pytest

## Project Execution Notes

Note that to fully run this project using the `run_all.sh script`, you must open a Linux Bash terminal.

Feel free to run whatever commands are necessary to train or to run the tests without relying on the `run_all.sh` script. Since the project separates the training and prediction code, you won’t need to retrain the model on the data every time you want to run the tests.

To run this project successfully, follow these steps:

1. Clone the repository using the command `git clone`.

2. Navigate to the project’s root directory and run `python -m venv venv` to create a virtual environment that isolates the project and ensures it runs correctly.

3. Finally, execute the command `sh run_all.sh`, which will start the program in its entirety.
