fn is_palindrome(s: &str) -> bool {
    for (c,d) in s.chars().zip(s.chars().rev()) {
        if c != d {
            return false;
        }
    }
    true
}

fn palindrome(digits: u32) -> u32 {
    let base:i32 = 10;
    let min = base.pow(digits - 1);
    let max = base.pow(digits)-1;
    let mut largest:u32 = 0;
    for i in (min..max+1).rev() {
        for j in (min..i+1).rev() {
            let n:u32 = i*j;
            if is_palindrome(format!("{}",n)) && n > largest {
                largest = n;
                println!("found {} ({}*{})",n,i,j);
            }
        }
    }
    largest
}

fn main() {
    assert!(!is_palindrome("foo"));
    assert!(is_palindrome("foof"));
    assert!(is_palindrome("fofof"));
    palindrome(1);
}
