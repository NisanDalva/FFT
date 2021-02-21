# FFT
Here is an implemention of a FFT algorithm.
Used to efficiently multiply two polynomials.

## Usage
Let's start with making an instance of the FFT object, that incude all relevant parameters:  
```fft = FFT(A=[1, 0, 1], B=[3, -2])```  

Then you can run the algorithm by command ```run()```:  
```fft.run()```  
Notice this command also return the results of multiplication.  
You can also print the result as a polynomial by called the method ```fft.print_as_polynomial()```.  It will print ```C(x)```.

## Parameters

* ```A```: Vector of coefficient of polynomial A(x).
* ```B```: Vector of coefficient of polynomial B(x).

* ```n```: Optional, default is None. Is the FFT order. If None it will be determined automatically.
* ```round_results```: Optional, default is 3. How many digits after the point will appear.

* ```reverse```: Optional, default is False. True if wanted a FFT^-1.

* ```tol```: Optional, default is 0.001. Used only for printing as a polynomial. It is used to check if need to round to the closest integer.