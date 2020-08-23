extern crate pe;

use pe::BigInt;

use std::io;
use std::io::Read;
use std::fs::File;


fn sum_numbers_from_file(filename:&str) -> Result<BigInt, io::Error> {
    let mut f = File::open(filename)?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    let mut n = BigInt::new();
    for line in s.lines() {
        let m = BigInt::new_from_string(line);
        //println!("{} {}",n,m);
        n.add_in_place(&m);
    }
    Ok(n)
}


fn main() {
    match sum_numbers_from_file("../data/eu013.dat") {
        Ok(n) => println!("result: {}",&n.to_string()[0..10]),
        Err(e) => println!("error: {}",e),
    }
}
