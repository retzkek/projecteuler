fn square(n: u32) -> u32 {
    n*n
}

fn sum(s: u32, n: u32) -> u32 {
    s+n
}

fn sum_of_squares(max: u32) -> u32 {
    (0..max+1).map(square).fold(0,sum)
}

#[test]
fn test_sum_of_squares() {
    assert_eq!(sum_of_squares(1),1);
    assert_eq!(sum_of_squares(2),5);
    assert_eq!(sum_of_squares(3),14);
}

fn square_of_sums(max: u32) -> u32 {
    square((0..max+1).fold(0,sum))
}

#[test]
fn test_square_of_sums() {
    assert_eq!(square_of_sums(1),1);
    assert_eq!(square_of_sums(2),9);
    assert_eq!(square_of_sums(3),36);
}

fn eu006(n: u32) -> u32 {
    square_of_sums(n)-sum_of_squares(n)
}

#[test]
fn test_eu006() {
    assert_eq!(eu006(10), 2640);
}

fn main() {
    println!("result: {}",eu006(100));
}
