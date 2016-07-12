pub struct Primes {
    primes: Vec<u32>,
}

impl Primes {
    pub fn new() -> Primes {
        Primes {
            primes: vec![],
        }
    }

    pub fn next(&mut self) -> u32 {
        let mut i = match self.last() {
            0 => 2,
            2 => 3,
            _ => self.last() + 2,
        };
        'candidates: loop {
            'primes: for p in &self.primes {
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

    pub fn last(&self) -> u32 {
        match self.primes.last() {
            Some(&x) => x,
            _ => 0,
        }
    }

    pub fn sieve(&mut self, max: usize) {
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
        for i in 2..max {
            if sieve[i] {
                self.primes.push(i as u32);
            }
        }
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
    fn sieve() {
        let mut p = Primes::new();
        p.sieve(100);
        assert_eq!(p.last(),97);
        assert_eq!(p.primes.len(),25);
    }
}
