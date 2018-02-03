def generate_primes(n):
    primes = []
    is_prime = [True] * n

    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)

            for j in range(i, n, i):
                is_prime[j] = False

    return primes

print(generate_primes(20))