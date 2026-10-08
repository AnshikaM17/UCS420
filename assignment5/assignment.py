"""UCS420 Assignment 4: NumPy Introduction-1."""

import numpy as np


def question_1() -> None:
	"""Perform arithmetic operations on a one-dimensional array."""
	numbers = np.array([1, 2, 3, 4, 5])
	print("Q1 - Original array:", numbers)
	print("Addition of 2:", numbers + 2)
	print("Multiplication by 3:", numbers * 3)
	print("Division by 2:", numbers / 2)


def question_2() -> None:
	"""Reverse an array and access its first five and last three elements."""
	array = np.array([1, 2, 3, 6, 4, 5])
	print("\nQ2(a) - Reversed array:", array[::-1])

	x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1])
	y = np.array([1, 1, 1, 1, 2, 4, 3, 3, 3])
	print("Q2(b) - First five elements of x:", x[:5])
	print("Q2(b) - Last three elements of x:", x[-3:])
	print("Q2(b) - First five elements of y:", y[:5])
	print("Q2(b) - Last three elements of y:", y[-3:])


def question_3() -> None:
	"""Access specified values in a two-dimensional array."""
	array_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
	print("\nQ3 - 2-D array:\n", array_2d, sep="")
	print("First row, second column:", array_2d[0, 1])
	print("Third row, first column:", array_2d[2, 0])


def question_4() -> None:
	"""Create an evenly spaced one-dimensional array and inspect it."""
	your_name_array = np.linspace(10, 100, 25)
	print("\nQ4 - 25 evenly spaced values:\n", your_name_array, sep="")
	print("Dimensions:", your_name_array.ndim)
	print("Shape:", your_name_array.shape)
	print("Total elements:", your_name_array.size)
	print("Data type of each element:", your_name_array.dtype)
	print("Total bytes consumed:", your_name_array.nbytes)
	print("Transpose using T:\n", your_name_array.T, sep="")
	print("T gives the same values for a 1-D array:", np.array_equal(your_name_array, your_name_array.T))


def question_5() -> None:
	"""Calculate statistics and reshape the requested two-dimensional array."""
	ucs420_student = np.array(
		[[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]]
	)
	print("\nQ5 - Original 2-D array:\n", ucs420_student, sep="")
	print("Mean:", np.mean(ucs420_student))
	print("Median:", np.median(ucs420_student))
	print("Maximum:", np.max(ucs420_student))
	print("Minimum:", np.min(ucs420_student))

	reshaped_ucs420_student = ucs420_student.reshape(4, 3)
	print("Reshaped array with 4 rows and 3 columns:\n", reshaped_ucs420_student, sep="")


def main() -> None:
	question_1()
	question_2()
	question_3()
	question_4()
	question_5()


if __name__ == "__main__":
	main()
