fn largest_prime_factor(num: u64) -> u64 {
    let (mut n, mut r, mut fac) = (num, 1, 2);
    while fac*fac <= n {
        if n%fac == 0 && fac > r {
            r = fac;
            n = n/fac;
        } else {
            fac+=1;
        }
    }
    if n != 1 {
        r = n;
    }
    println!("largest prime factor of {}: {}",num,r);
    r
}

fn main() {
    if largest_prime_factor(13195) != 29 {
        panic!("test failed! expecting result: 29}");
    }
    largest_prime_factor(600851475143);
}
