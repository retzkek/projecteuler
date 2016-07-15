use std::io;
use std::io::prelude::*;
use std::fs::File;

fn max_product_five(filename:&str) -> Result<u32, io::Error> {
    let mut f = try!(File::open(filename));
    let mut s = Vec::new();
    try!(f.read_to_end(&mut s));
    // convert to vector of digits and throw away non-digit chars
    let ns: Vec<_> = s.iter()
        .filter_map(|c| (*c as char).to_digit(10))
        .collect();
    println!("number:\n{:?}",ns);
    // find max product of five digits
    let mut maxp:u32 = 0;
    for w in ns.windows(5) {
        let p: u32 = w.iter().fold(1,std::ops::Mul::mul);
        //println!("{:?} {}",w, p);
        maxp = std::cmp::max(maxp,p);
    }
    Ok(maxp)
}


fn main() {
    match max_product_five("../data/eu008.dat") {
        Ok(n) => println!("result: {}",n),
        Err(e) => println!("error: {}",e),
    }
}
