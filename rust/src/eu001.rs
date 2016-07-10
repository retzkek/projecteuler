fn natmult(bases: &[i32], max: i32) -> i32 {
    let mut result = 0;
    for i in 0..max {
        for b in bases {
            if i % b == 0 {
                result += i;
                break;
            }
        }
    }
    println!("bases: {:?}; max: {}; result: {}",bases, max, result);
    result
}

fn main() {
    let bases = [3,5];
    let max = 10;
    if natmult(&bases[..],max) != 23 {
        panic!("test failed! expecting result: 23");
    }
    natmult(&bases[..],1000);
}
