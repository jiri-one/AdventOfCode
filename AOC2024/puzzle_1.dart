import 'dart:io';

String INPUT = "input.txt"; // result is 2580760
String TEST_INPUT = "test_input.txt"; // result should be 11

void main() {
  // Read the input from a file named 'input.txt'
  final input = File(INPUT).readAsStringSync().trim();
  final testInput = File(TEST_INPUT).readAsStringSync().trim();
  
  // Split the input into lines
  final lines = input.split('\n');
  List<int> list1 = [];
  List<int> list2 = [];
  
  // Initialize a variable to hold the sum of all numbers
  int totalSum = 0;
  
  // Iterate through each line
  for (var line in lines) {
    var oneLineNumbers = line.split('   ');
    int nr1 = int.parse(oneLineNumbers[0]);
    int nr2 = int.parse(oneLineNumbers[1]);
    list1.add(nr1);
    list2.add(nr2);
  }

  list1.sort();
  list2.sort();

  for (int i = 0; i < list1.length; i++) {
    // Calculate the sum of the two numbers
    int dif = list1[i] - list2[i];
    if (dif < 0) {
        dif = -dif; // Ensure the sum is non-negative
    }
    
    // Add the sum to the total sum
    totalSum += dif;
  }
  
  // Print the total sum
  print('Total Sum: $totalSum');
}