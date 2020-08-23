pub struct Primes {
    primes: Vec<u32>,
}

impl Primes {
    /// Initialize and return new empty Primes struct.
    pub fn new() -> Primes {
        Primes {
            primes: Vec::with_capacity(100),
        }
    }

    /// Initialize and return new Primes struct populated
    /// with all primes below max.
    pub fn new_to(max: usize) -> Primes {
        let mut sieve = vec![true;max];
        let mut i:usize = 2;
        while i*i < max {
            if sieve[i] {
                // i is prime, all multiples of i are not
                let mut j:usize = 2*i;
                while j < max {
                    sieve[j] = false;
                    j = j+i;
                }
            }
            i = i+1;
        }
        // extract primes
        let maxf = max as f32;
        let mut p = Primes {
            primes: Vec::with_capacity((maxf/maxf.log10()) as usize),
        };
        for i in 2..max {
            if sieve[i] {
                p.primes.push(i as u32);
            }
        }
        p

    }

    /// Calculate and return new prime.
    pub fn next(&mut self) -> u32 {
        let mut i = match self.last() {
            0 => 2,
            2 => 3,
            _ => self.last() + 2,
        };
        'candidates: loop {
            for p in &self.primes {
                if i%p == 0 {
                    i = i+2;
                    continue 'candidates;
                }
                if p*p > i {
                    break 'candidates;
                }
            }
            break;
        }
        self.primes.push(i);
        i
    }

    /// Return last prime calculated.
    pub fn last(&self) -> u32 {
        match self.primes.last() {
            Some(&x) => x,
            _ => 0,
        }
    }
}

impl IntoIterator for Primes {
    type Item = u32;
    type IntoIter = ::std::vec::IntoIter<u32>;

    fn into_iter(self) -> Self::IntoIter {
        self.primes.into_iter()
    }
}

#[cfg(test)]
mod test {
    use super::Primes;

    #[test]
    fn new() {
        let p = Primes::new();
        assert_eq!(p.last(),0);
    }

    #[test]
    fn next() {
        let mut p = Primes::new();
        assert_eq!(p.next(),2);
        assert_eq!(p.next(),3);
        assert_eq!(p.next(),5);
        assert_eq!(p.next(),7);
        assert_eq!(p.next(),11);
        assert_eq!(p.next(),13);
        assert_eq!(p.next(),17);
        assert_eq!(p.next(),19);
        assert_eq!(p.next(),23);
    }

    #[test]
    fn new_to() {
        let p = Primes::new_to(100);
        assert_eq!(p.last(),97);
        assert_eq!(p.primes.len(),25);
    }

    #[test]
    fn into_iter() {
        let p = Primes::new_to(10);
        let mut sum:u32 = 0;
        for n in p {
            sum = sum + n;
        }
        assert_eq!(sum,17);
    }
}
