def combine_text_files(file1_path, file2_path, output_file_path):

    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(output_file_path, 'w') as output_file:

            output_file.write("Compare the job description and the resume and rate the suitability of the candidate on a scale of 1 to 10. Provide justification for each deduction and addition of score. Enclose the rating within angled brackets. For example: Rating <7>\n\n")

            output_file.write("Job description:\n\n")

            for line in file1:
                output_file.write(line)

            output_file.write("\n\n")

            output_file.write("Resume:\n\n")

            for line in file2:
                output_file.write(line)

    except FileNotFoundError:
        print("Error: One or more input files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Details: {e}")

if __name__ == "__main__":
    file1_path = "job_description.txt"
    file2_path = "resume.txt"
    output_file_path = "input.txt"
    combine_text_files(file1_path, file2_path, output_file_path)
