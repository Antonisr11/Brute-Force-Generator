# Brute-Force-Generator
Generate every possible combination from a given vocabulary **without randomness**

## Arguments 

### 1. vocabulary (**mandatory**)
> Vocabulary must take a list (or tuple) of characters which it will use to create combinations. For instance if we provide only numbers in that list, all results will contain only numbers.

**BruteForceGenerator provides some ready vocabularies such as English Letters, Greek Letters, Numbers, Special Characters.**


	example
		generator = BruteForceGenerator(vocabulary=["a", "b", "c"])
		generator = BruteForceGenerator(vocabulary=BruteForceGenerator.ENGLISH_LETTERS)
		generator = BruteForceGenerator(vocabulary=BruteForceGenerator.GREEK_LETTERS)
		generator = BruteForceGenerator(vocabulary=BruteForceGenerator.NUMBERS)
		generator = BruteForceGenerator(vocabulary=BruteForceGenerator.SPECIAL_CHARACTERS)
		generator = BruteForceGenerator(vocabulary=BruteForceGenerator.ENGLISH_LETTERS + BruteForceGenerator.SPECIAL_CHARACTERS + BruteForceGenerator.NUMBERS)


### 2. max_length
> Max_length must take a number greater than 0 and presents 

> For instance if max_length is set 2 and vocabulary is only numbers, BruteForceGenerator will produce 1, 2, 3, .., 98, 99. 

**Default value is 10**

## Uses
We can use BruteForceGenerator class with two ways:
* [Static Way](#Static)
* [GenerateNext Way](#GenerateNext)

## Static
We can use BruteForceGenerator without creating instance.

	example
		print(BruteForceGenerator.generateList(["a","b","c"], 3))
		
	result
		'a', 'b', 'c', 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc', 'aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc'

## GenerateNext
We can create a BruteForceGenerator instance and produce each combination with generateNext() method.

	example
		generator = BruteForceGenerator(vocabulary=BruteForceGenerator.NUMBERS, max_length=3)
    	for _ in range(0, 1111):
        	    print(generator.generateNext())
	result
		0
		1
		2
		.
		.
		998
		999
		0

## GenerateCurrent
We can print current combination with generateCurrent() method.

	example
		generator = BruteForceGenerator(vocabulary=BruteForceGenerator.NUMBERS, max_length=3)
    		print(generator.generateNext())
    		print(generator.generateCurrent())
    		print(generator.generateCurrent())
    		print(generator.generateNext())
    		print(generator.generateNext())
    		print(generator.generateCurrent())
	
	results
		0
		0
		0
		1
		2
		2
