import subprocess

def test_bestrelayteam():
    # Define the input and expected output
    input_data = "5\nAlice 12.5 9.5\nBob 11.0 8.0\nCharlie 13.0 10.0\nDavid 10.5 7.5\nEve 12.0 9.0\n"
    expected_output = "36.5\nDavid\nBob\nEve\nAlice\n"

    # Run the script with the input data
    result = subprocess.run(
        ["python3", "bestrelayteam.py"],
        input=input_data,
        text=True,
        capture_output=True
    )

    # Check if the output matches the expected output
    assert result.stdout == expected_output, f"Expected {expected_output}, but got {result.stdout}"

# Run the test
test_bestrelayteam()