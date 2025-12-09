Based on the uploaded files, here is the README documentation for the project.

-----

# DAA Project 2025: Divide & Conquer Algorithms

This project implements various algorithms based on the **Divide & Conquer** paradigm. It consists of a series of foundational exercises (Part 1) and a main GUI application (Parts 2, 3, & 4) that visualizes the **Closest Pair of Points** and **Karatsuba Multiplication** algorithms.

## Team Members

  * **Taaha Khan** (23K-0583)
  * **Abdul Basit** (23K-0526)
  * **Alishba** (23K-0756)

## Project Structure

The repository is organized into the following sections:

### Part 1: Algorithmic Exercises

Standalone Python scripts implementing classical Divide & Conquer problems:

  * `count_inversions.py`: Counts split inversions in an array using Merge Sort logic.
  * `majority_element.py`: Identifies the majority element in an array.
  * `max_profit.py`: Calculates maximum profit from price data (Stock Span problem).
  * `median_sorted_arrays.py`: Finds the median of two sorted arrays.
  * `peak_finder.py`: Finds a peak element in an array ($A[i]$ where neighbors are smaller).

### Parts 2, 3, & 4: Main Project (GUI Application)

A comprehensive application using **CustomTkinter** to visualize and execute advanced algorithms on generated datasets.

**Location:** `Part 2,3 and 4/Main Project/`

**Key Components:**

  * **GUI (`gui.py`):** The main entry point. Provides an interface to switch between algorithms, select input files, and view input/output side-by-side.
  * **Algorithms:**
      * **Closest Pair of Points (`algorithms/closest_pair.py`):** Finds the Euclidean distance between the two closest points in a 2D plane with $O(n \log n)$ complexity. Includes a dataset generator.
      * **Karatsuba Multiplication (`algorithms/karatsuba_str.py`):** Performs fast multiplication of large integers (100-150 digits) with time complexity $O(n^{\log_2 3})$. Includes a large-integer generator.
  * **Parsers:** Helper scripts to read 2D points and large integer files.
  * **Data:**
      * `closest_inputs/`: Text files containing coordinate pairs.
      * `karatsuba_string_inputs/`: Text files containing large integer pairs.
      * `closest_results/` & `karatsuba_string_results/`: Output files storing computed results.

## Prerequisites

  * **Python 3.x**
  * **CustomTkinter** (Required for the GUI)

To install the required library:

```bash
pip install customtkinter
```

## Usage Instructions

### Running the Main GUI Application

1.  Navigate to the project directory:
    ```bash
    cd "Part 2,3 and 4/Main Project"
    ```
2.  Run the application:
    ```bash
    python gui.py
    ```
3.  **Functionality:**
      * Select **Closest Pair of Points** or **Karatsuba Multiplication** from the main menu.
      * Choose a test dataset (e.g., `points_1.txt` or `input_1.txt`) from the file list.
      * The application will display the raw input data on the left and the computed result on the right.

### Running Part 1 Exercises

Navigate to the `Part 1` folder and run individual scripts via the terminal. Input may be required via standard input (stdin) or hardcoded in the `__main__` block depending on the script.

Example:

```bash
cd "Part 1"
python count_inversions.py
```

## Data Generation

The main algorithms (`closest_pair.py` and `karatsuba_str.py`) include `__main__` blocks that automatically generate random test datasets (10 files each) when executed directly.

To regenerate data:

```bash
python algorithms/closest_pair.py
python algorithms/karatsuba_str.py
```

## References

  * T. H. Cormen et al., *Introduction to Algorithms*.
  * Kleinberg & Tardos, *Algorithm Design*.
  * Anany Levitin, *Introduction to the Design and Analysis of Algorithms*.
