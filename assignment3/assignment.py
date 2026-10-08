"""UCS420 Assignment 3: pandas data manipulation exercises."""

from pathlib import Path

import pandas as pd


OUTPUT_DIR = Path(__file__).parent
EMPLOYEES_CSV = OUTPUT_DIR / "employees.csv"
MODIFIED_EMPLOYEES_CSV = OUTPUT_DIR / "employees_modified.csv"
IRIS_URL = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/master/data/iris.csv"


def question_1() -> pd.DataFrame:
	"""Create and display the tax and marital-status dataset."""
	data = {
		"Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
		"Refunded": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
		"Marital Status": [
			"Single",
			"Married",
			"Single",
			"Married",
			"Divorced",
			"Married",
			"Divorced",
			"Single",
			"Married",
			"Single",
		],
		"Taxable Income": ["125K", "100K", "70K", "120K", "95K", "60K", "220K", "85K", "75K", "90K"],
		"Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"],
	}
	dataset = pd.DataFrame(data)
	print("Q1 - Dataset:\n", dataset, sep="")
	return dataset


def question_2(dataset: pd.DataFrame) -> None:
	"""Locate rows 0, 4, and 7 using DataFrame indexing."""
	print("\nQ2 - Rows 0, 4, and 7:\n", dataset.loc[[0, 4, 7]], sep="")


def question_3(dataset: pd.DataFrame) -> None:
	"""Demonstrate the requested row and column selections."""
	print("\nQ3(a) - Rows 3 to 7, columns 2 to 4:\n", dataset.iloc[3:8, 2:5], sep="")
	print("\nQ3(b) - Rows 4 to 8, columns 2 to 4:\n", dataset.iloc[4:9, 2:5], sep="")
	print("\nQ3(c) - All rows, columns 1 to 3:\n", dataset.iloc[:, 1:4], sep="")


def question_4() -> pd.DataFrame:
	"""Read the iris CSV and display its first five rows."""
	iris = pd.read_csv(IRIS_URL)
	print("\nQ4 - First five rows of iris.csv:\n", iris.head(), sep="")
	return iris


def question_5(iris: pd.DataFrame) -> pd.DataFrame:
	"""Remove the fourth row and third column from the iris dataset."""
	result = iris.drop(index=iris.index[3]).drop(columns=iris.columns[2])
	print("\nQ5 - Iris data after deleting row 4 and column 3:\n", result, sep="")
	return result


def create_employee_dataset() -> pd.DataFrame:
	"""Create the employee dataset required for Question 6."""
	data = {
		"Employee_ID": [101, 102, 103, 104, 105],
		"Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
		"Department": ["HR", "IT", "Finance", "Marketing", "Sales"],
		"Age": [29, 34, 41, 28, 38],
		"Salary": [50000, 70000, 95000, 55000, 80000],
		"Year_of_Experience": [2, 5, 10, 3, 12],
		"Joining_Date": pd.to_datetime(
			["2020-01-15", "2017-03-19", "2013-06-01", "2021-02-10", "2010-11-25"]
		),
		"Gender": ["Female", "Male", "Male", "Female", "Male"],
		"Bonus": [5000, 7000, 10000, 4500, 5000],
		"Rating": [4.5, 4.0, 4.8, 4.7, 5.0],
	}
	employees = pd.DataFrame(data)
	employees.to_csv(EMPLOYEES_CSV, index=False)
	return employees


def question_6() -> pd.DataFrame:
	"""Perform all employee DataFrame operations requested in the assignment."""
	employees = create_employee_dataset()

	print("\nQ6(a) - Shape:", employees.shape)
	print("\nQ6(b) - Summary:")
	employees.info()
	print("\nQ6(c) - Descriptive statistics:\n", employees.describe(include="all"), sep="")
	print("\nQ6(d) - First and last five rows:\n", pd.concat([employees.head(), employees.tail()]), sep="")

	print("\nQ6(e) - Calculations:")
	print("Average salary:", employees["Salary"].mean())
	print("Total bonus:", employees["Bonus"].sum())
	print("Youngest employee's age:", employees["Age"].min())
	print("Highest-performing employee(s):\n", employees[employees["Rating"] == employees["Rating"].max()])

	employees = employees.sort_values("Salary", ascending=False)
	print("\nQ6(f) - Sorted by salary:\n", employees, sep="")

	employees["Performance_Category"] = employees["Rating"].apply(
		lambda rating: "Excellent" if rating >= 4.5 else "Good" if rating >= 4.0 else "Average"
	)
	print("\nQ6(g) - Performance categories:\n", employees, sep="")

	print("\nQ6(h) - Missing values:\n", employees.isna().sum(), sep="")

	employees = employees.rename(columns={"Employee_ID": "ID"})
	print("\nQ6(i) - Renamed Employee_ID to ID:\n", employees, sep="")

	experienced_employees = employees[
		(employees["Salary"] > 60000) & (employees["Year_of_Experience"] > 5)
	]
	it_employees = employees[employees["Department"] == "IT"]
	print("\nQ6(j) - Salary > 60000 and experience > 5:\n", experienced_employees, sep="")
	print("\nQ6(j) - IT department:\n", it_employees, sep="")

	employees["Tax"] = employees["Salary"] * 0.10
	employees.to_csv(MODIFIED_EMPLOYEES_CSV, index=False)
	print("\nQ6(k-l) - Added 10% tax and saved:", MODIFIED_EMPLOYEES_CSV)
	return employees


def main() -> None:
	dataset = question_1()
	question_2(dataset)
	question_3(dataset)
	try:
		iris = question_4()
		question_5(iris)
	except Exception as error:
		print("\nQ4-Q5 could not read the iris dataset:", error)
	question_6()


if __name__ == "__main__":
	main()
