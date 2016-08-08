//! BigInt is a simple arbitrary-precision integer type, stored 
//! in a big-endian Vec<u8>.

use std::fmt;
use std::iter;

#[derive(Debug, Clone)]
pub struct BigInt {
    digits: Vec<u8>,
}

impl BigInt {
    pub fn new() -> BigInt {
        BigInt {
            digits: Vec::with_capacity(50),
        }
    }

    pub fn new_from_string(ns: &str) -> BigInt {
        let dig = ns.chars().rev().map(|c| c.to_digit(10).unwrap() as u8).collect::<Vec<u8>>();
        //println!("{} {:?}",ns,dig);
        BigInt {
            digits: dig,
        }
    }

    pub fn len(&self) -> usize {
        self.digits.len()
    }

    /// Add two BigInts, returning result.
    pub fn add(&self, n: &BigInt) -> BigInt {
        let mut r = self.clone();
        r.add_in_place(n);
        r
    }

    /// Add n to self, result in self.
    pub fn add_in_place(&mut self, n: &BigInt) {
        let mut carry = 0;
        if n.len() > self.len() {
            self.digits.resize(n.len(),0);
        }
        for (a,b) in self.digits.iter_mut().zip(n.digits.iter().chain(iter::repeat(&0))) {
            let d = (*a+b+carry)%10;
            carry = (*a+b+carry)/10;
            *a = d;
        }
        if carry > 0 {
            self.digits.push(carry);
        }
    }
}

impl fmt::Display for BigInt {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let s = self.digits.iter().rev()
            .map(|n| n.to_string())
            .collect::<Vec<String>>()
            .concat();
        write!(f, "{}", s)
    }
}

#[cfg(test)]
mod test {
    use super::BigInt;

    #[test]
    fn test_new_from_string() {
        let n = BigInt::new_from_string("12345");
        assert_eq!(n.to_string(),"12345")
    }

    #[test]
    fn test_add() {
        let n = BigInt::new_from_string("12345");
        let m = BigInt::new_from_string("654321");
        let r = n.add(&m);
        assert_eq!(r.to_string(),"666666");
    }

    #[test]
    fn test_add2() {
        let n = BigInt::new_from_string("12345");
        let m = BigInt::new_from_string("98765");
        let r = m.add(&n);
        assert_eq!(r.to_string(),"111110");
    }

    #[test]
    fn test_add_with_carry() {
        let n = BigInt::new_from_string("987654321");
        let r = n.add(&n);
        assert_eq!(r.to_string(),"1975308642");
    }

    #[test]
    fn test_add_in_place() {
        let mut n = BigInt::new_from_string("12345");
        let m = BigInt::new_from_string("654321");
        n.add_in_place(&m);
        assert_eq!(n.to_string(),"666666");
    }

    #[test]
    fn test_add_in_place_with_carry() {
        let mut n = BigInt::new_from_string("987654321");
        let m = BigInt::new_from_string("987654321");
        n.add_in_place(&m);
        assert_eq!(n.to_string(),"1975308642");
    }
}
