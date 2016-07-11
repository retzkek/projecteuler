extern crate pe;

use pe::primes::Primes;

fn main() {
    let mut p = Primes::new();
    for _ in 3..10002 {
        p.next();
    }
    println!("result: {}",p.last());
}
