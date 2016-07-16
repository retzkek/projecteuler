extern crate pe;

use pe::primes::Primes;

fn sum_primes(p:Primes, max:u32) -> u64 {
    p.into_iter().filter(|n| *n < max).map(|n| n as u64).fold(0,std::ops::Add::add)
}
        

fn main() {
    let p = Primes::new_to(2000000);
    println!("result: {}",sum_primes(p,2000000));
}

#[cfg(test)]
mod test {
    use super::sum_primes;
    use pe::primes::Primes;

    #[test]
    fn test_sum_primes() {
        let p = Primes::new_to(10);
        assert_eq!(sum_primes(p,10),17);
    }
}
