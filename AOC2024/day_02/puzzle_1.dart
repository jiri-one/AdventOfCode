import 'dart:io';

String INPUT = "input.txt"; // result is
String TEST_INPUT = "test_input.txt"; // result should be 2

bool isIncreasing(int a, int b) {
  return ((a - b) <= 0) ? true : false;
}

void main() {
  // Read the input from a file named 'input.txt'
  final input = File(TEST_INPUT).readAsStringSync().trim();

  // Split the input into lines
  final lines = input.split('\n');

  int totalSafeSum = 0;

  // Iterate through each line
  for (var line in lines) {
    List<int> oneLineNumbers =
        line.split(' ').map((i) => int.parse(i)).toList();
    bool increasing = isIncreasing(oneLineNumbers[0], oneLineNumbers[1]);
    int previous = oneLineNumbers[0];

    bool safe = true;
    for (int i = 1; i < oneLineNumbers.length; i++) {
      if (isIncreasing(previous, oneLineNumbers[i]) != increasing) {
        safe = false;
        break;
      }
      if ((previous - oneLineNumbers[i]).abs() > 3) {
        safe = false;
        break;
      }
      previous = oneLineNumbers[i];
    }
    if (safe == true) {
      print(safe);
      print(line);
      totalSafeSum += 1;
    }
  }

  // Print the total sum
  print('Total Sum: $totalSafeSum');
}
