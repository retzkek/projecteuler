const std = @import("std");
const expect = @import("std").testing.expect;

fn largestPrimeFactor(num: u64) u64 {
    var n: u64 = num;
    var result: u64 = 1;
    var fac: u64 = 2;
    while (fac*fac <= n) {
        if (@mod(num,fac) == 0 and fac > result) {
            result = fac;
            n = n / fac;
        } else {
            fac+=1;
        }
    }
    if (n != 1) {
        result = n;
    }
    return result;
}

test "largest prime factor of 13195" {
    expect(largestPrimeFactor(13195)==29);
}

pub fn main() void {
    std.debug.print("{}\n", .{largestPrimeFactor(600851475143)});
}
