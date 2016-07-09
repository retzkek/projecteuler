fn fibsum(max: i32) -> i32 {
    let (mut f0, mut f1, mut r) = (1,2,2);
    while f1 < max {
        let f2 = f0 + f1;
        if f2 < max && f2%2 == 0 {
            r += f2;
        }
        f0 = f1;
        f1 = f2;
    }
    println!("sum of even fibonacci numbers under {}: {}",max,r);
    r
}

fn main() {
    if fibsum(90) != 44 {
        panic!("test failed! expecting result: 44}");
    }
    fibsum(4000000);
}
