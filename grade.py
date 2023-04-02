# Define the weights for each category
hw_weight = 0.4
quiz_weight = 0.2
test_weight = 0.4

# Get the scores for each category from the user
hw_score = float(input("Enter the homework score (out of 100): "))
quiz_score = float(input("Enter the quiz score (out of 100): "))
test_score = float(input("Enter the test score (out of 100): "))

# Calculate the weighted score for each category
hw_weighted = hw_score * hw_weight
quiz_weighted = quiz_score * quiz_weight
test_weighted = test_score * test_weight

# Calculate the overall weighted score
overall_score = hw_weighted + quiz_weighted + test_weighted

# Print the overall weighted score and the corresponding letter grade
print("Overall weighted score:", overall_score)
if overall_score >= 90:
    print("Grade: A")
elif overall_score >= 80:
    print("Grade: B")
elif overall_score >= 70:
    print("Grade: C")
elif overall_score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
