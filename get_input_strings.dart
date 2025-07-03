import 'dart:io';
import 'package:args/args.dart';

String INPUT = "input.txt"; //main name for input file
String TEST_INPUT = "test_input.txt"; // name of file with test data
String inputFile = INPUT;

/// Reads input from a file and returns the full input as a string,
/// along with a list of lines. If "test" is passed as an argument,
/// it reads from the test input file instead.
(String, List<String>) getInputStrings(List<String> arguments) {
  // Check if a file name is provided as an argument
  ArgParser parser = ArgParser();
  ArgResults results = parser.parse(arguments);

  if (results.rest.contains("test") && results.rest.length == 1) {
    inputFile = TEST_INPUT;
  }

  // Read the input from a file
  String input = File(inputFile).readAsStringSync().trim();
  // Split the input into lines
  List<String> lines = input.split('\n');
  return (input, lines);
}
