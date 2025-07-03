import '../../get_input_strings.dart' show getInputStrings;

// test results should be 2
// result is 390

// helper functions
bool isIncreasing(int a, int b) {
  return ((a - b) < 0) ? true : false;
}

void main(List<String> arguments) {
  var (String input, List<String> lines) = getInputStrings(arguments);
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
      if (previous == oneLineNumbers[i]) {
        safe = false;
        break;
      }
      previous = oneLineNumbers[i];
    }
    if (safe == true) {
      totalSafeSum += 1;
    }
  }

  // Print the total sum
  print('Total Sum: $totalSafeSum');
}
