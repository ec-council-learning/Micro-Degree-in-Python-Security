def primes(int nb_primes):  # Convert argument to C integer
    cdef int n, i, len_p  # Define local C variables as C integers
    cdef int p[1000]  # Define local C variable as C array; arrays are size-limited due to C call stack
    if nb_primes > 1000:  # Prevent segfault by limiting static array size
        nb_primes = 1000

    # Still C integers
    len_p = 0  # The current number of elements in p.
    n = 2

    # All the variables in the following loop are processed as true C code for max speed
    while len_p < nb_primes:  # Test numbers for primeness until requested number of primes is found
        for i in p[:len_p]:  # Loop is converted to C loop
            if n % i == 0:  # 'n' not prime
                break
        else:  # 'n' is prime
            p[len_p] = n
            len_p += 1
        n += 1

    result_as_list  = [prime for prime in p[:len_p]]  # Copy C array to Python list
    return result_as_list