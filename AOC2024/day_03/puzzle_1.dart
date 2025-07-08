import '../../get_input_strings.dart' show getInputStrings;

// test results should be 161
// result is 179834255

// helper functions
bool isIncreasing(int a, int b) {
  return ((a - b) < 0) ? true : false;
}

void main(List<String> arguments) {
  var (String input, List<String> lines) = getInputStrings(arguments);
  int totalMulSum = 0;

  RegExp exp = RegExp(r"mul\((\d+),(\d+)\)");
  Iterable<RegExpMatch> matches = exp.allMatches(input);
  for (final match in matches) {
    int fistNumber = int.parse(match.group(1)!);
    int secondNumber = int.parse(match.group(2)!);
    totalMulSum += fistNumber * secondNumber;
  }

  // Print the total sum
  print('Total Sum: $totalMulSum');
}
