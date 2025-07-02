import 'dart:io';

String INPUT = "input.txt"; // result is 
String TEST_INPUT = "test_input.txt"; // result should be 31

void main() {
  // Read the input from a file named 'input.txt'
  final input = File(INPUT).readAsStringSync().trim();
  final testInput = File(TEST_INPUT).readAsStringSync().trim();
  
  // Split the input into lines
  final lines = input.split('\n');
  List<int> list1 = [];
  List<int> list2 = [];
  
  // Initialize a variable to hold the sum of all numbers
  double totalSum = 0;
  
  // Iterate through each line
  for (var line in lines) {
    var oneLineNumbers = line.split('   ');
    int nr1 = int.parse(oneLineNumbers[0]);
    int nr2 = int.parse(oneLineNumbers[1]);
    list1.add(nr1);
    list2.add(nr2);
  }

  for (int i = 0; i < list1.length; i++) {
    int number = list1[i];
    int occurences = 0;
    for (int j = 0; j < list2.length; j++) {
      if (list2[j] == number) {
        occurences++;
      } 
    }
    
    // Add the sum to the total sum
    totalSum += number * occurences;
  }
  
  // Print the total sum
  int totalSumInt = totalSum.toInt();
  print('Total Sum: $totalSumInt');
}