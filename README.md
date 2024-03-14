# interactive LUT using SGX
Only the codes in `decryptor` directory need to run in SGX.<br>
But there are some I/O files need to be prepared first. As the OS systems are different, I cannot give the compiled and intermediate result(ctxt) files. Those files have to be prepared by the os with SGX.

The files can used directly:<br>
`Table`<br>

 Structure:
 ```
 src --- decryptor --- bin (compiled)
      |              |- build (cmake files)
      |              |- CMakeList.txt
      |              |- demo.hpp
      |              |- keyGeneration.cpp
      |              |- makeQuery.cpp (for one-input functions)
      |              |- makeQueryTwo.cpp (for two-input functions)
      |              |- makeQueryThree.cpp (for three-input functions)
      |              
      |- serveruser -- bin (compiled)
      |              |- build (cmake files)
      |              |- CMakeList.txt
      |              |- demo.hpp
      |              |- makeInput.cpp (for one-input functions)
      |              |- makeInputTwo.cpp (for two-input functions)
      |              |- makeInputThree.cpp (for three-input functions)
      |              |- searchInput.cpp (for one-input functions)
      |              |- searchInputTwo.cpp (for two-input functions)
      |              |- searchInputThree.cpp (for three-input functions)
      |              |- extractOutput.cpp (for one-input functions)
      |              |- extractOutputTwo.cpp (for two-input functions)
      |              |- extractOutputThree.cpp (for three-input functions)
      |- Key (Save keys and parameters)
      |- Result (Save intermediate result)
      |- Table (Save plaintext tables)
 ```
 All of the `CMakeList.txt` and codes are finished.<br>
 You need to run as follows.<br>

 Step 1: generate keys<br>
 In `decryptor/build`:
 ```
 cmake ..
 make
 ```
 After compiled, back to `decryptor/`, run the command below and please test the runtime and memory usage.
 ```
 bin/keyGeneration
 ```

 Step 2: make input and search input, get intermediate result<br>
 In `serveruser/build`:
 ```
 cmake ..
 make
 ```
 After compiled, back to `decryptor/`, run the command below. (Do not need to test the runtime and memory usage.)
 ```
 bin/makeInputThree
 ```
When you run `searchInput(searchInputTwo or searchInputThree`, you need to input the bit number of table by keyboard.<br>
I am soooooo sorry that you may need to run them many times, because I need the results with different bit numbers.<br>
For example, when using the 12 bit LUT, please run:
```
bin/searchInput
```
you will see "*** Give the input LUT bit num:", please type 12 by keyboard.<br>

Step 3: test the the runtime and memory usage in SGX<br>
After you got the intermediate result by run the codes before, please go back to `decryptor/`.<br>
Run the command below and please test the runtime and memory usage.
```
bin/makeQuery
(or makeQueryTwo, makeQueryThree)
```
You also need to run them many times, and input the bit number of LUT by keyboard.

## The commands needs to run (summary)
Let me give you the command need to run with Step 2 and Step 3:<br>
`bin/searchInput` and `bin/makeQuery`, for one-input functions. Please use `(12), 14, 16, 18` bit, respectively.<br>
`bin/searchInputTwo` and `bin/makeQueryTwo`, for two-input functions. Please use `(8), 10, 12` bit, respectively.<br>
`bin/searchInputThree` and `bin/makeQueryThree`, for three-input functions. Please use `4, 6, 8` bit, respectively.<br>

Compile<br>
In `decryptor/build` and `serveruser/build`, run (just run):
```
cmake ..
make
```
respectively.<br>

After compiled all codes in `serveruser/` and `decryptor`.<br>
In `decryptor/`, run and test runtime and memory usage:
```
bin/keyGeneration
```
In `serveruser/`, run:
```
bin/makeInputThree
bin/searchInput (3 times, bit 14 16 18)
bin/searchInputTwo (2 times, bit 10 12)
bin/searchInputThree (3 times, bit 4 5 8)
```
In `decryptor/`, run and test runtime and memory usage:
```
bin/makeQuery (4 times, bit 12 14 16 18)
bin/makeQueryTwo (3 times, bit 8 10 12)
bin/makeQueryThree (3 times, bit 4 6 8)
```
In `decryptor/`, run and test runtime and memory usage:
```
bin/checkResult
```

Change the number of thread need to edit `demo.hpp`, `#define NF NUM_THREAD`.<br>
Only `makeQuery.cpp` adopted multi-thread.
