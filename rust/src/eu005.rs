fn smallest_div_by(n: u32) -> u32 {
    let mut i:u32 = 0;
    'outer: loop {
        i = i+n;
        for j in ((n/2)..n).rev() {
            if i%j != 0 {
                continue 'outer;
            }
        }
        break;
    }
    i
}

fn main() {
    assert_eq!(smallest_div_by(10),2520);
    println!("result: {}",smallest_div_by(20));
}
