import '../../get_input_strings.dart' show getInputStrings;

// test results should be 4
// result is 439

// helper functions
bool isIncreasing(int x, int y) {
  if ((y - x).abs() > 3 || y <= x) {
    return false;
  } else {
    return true;
  }
}

bool checkList(List<int> numbers) {
  bool increasing = true;
  for (int index = 0; index < numbers.length - 1; index++) {
    int current = numbers[index];
    int next = numbers[index + 1];
    increasing = isIncreasing(current, next);
    if (increasing == false) {
      return increasing;
    }
  }
  return increasing;
}

bool checker(List<int> numbers) {
  bool increasing = checkList(numbers);
  if (increasing == true) {
    return true;
  } else {
    for (int index = 0; index < numbers.length; index++) {
      List<int> newNumbers = List.from(numbers);
      newNumbers.removeAt(index);
      increasing = checkList(newNumbers);
      if (increasing == true) {
        return increasing;
      }
    }
    return increasing;
  }
}

void main(List<String> arguments) {
  var (String input, List<String> lines) = getInputStrings(arguments);
  int totalSafeSum = 0;

  // Iterate through each line
  for (var line in lines) {
    List<int> oneLineNumbers =
        line.split(' ').map((i) => int.parse(i)).toList();
    bool safe =
        checker(oneLineNumbers) || checker(oneLineNumbers.reversed.toList());
    if (safe == false) {
      print("$oneLineNumbers, $safe");
    }
    if (safe == true) {
      totalSafeSum += 1;
    }
  }
  // Print the total sum
  print('Total Sum: $totalSafeSum');
}
