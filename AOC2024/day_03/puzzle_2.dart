import '../../get_input_strings.dart' show getInputStrings;

// test results should be 48
// result is 80570939

// helper functions
bool isIncreasing(int a, int b) {
  return ((a - b) < 0) ? true : false;
}

void main(List<String> arguments) {
  var (String input, List<String> lines) = getInputStrings(arguments);
  int totalMulSum = 0;

  RegExp exp = RegExp(r"mul\((\d+),(\d+)\)");

  for (String do_part in input.split("do()")) {
    do_part = do_part.split("don't()")[0];

    Iterable<RegExpMatch> matches = exp.allMatches(do_part);
    for (final match in matches) {
      int fistNumber = int.parse(match.group(1)!);
      int secondNumber = int.parse(match.group(2)!);
      totalMulSum += fistNumber * secondNumber;
    }
  }
  // Print the total sum
  print('Total Sum: $totalMulSum');
}
