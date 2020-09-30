const std = @import("std");
const expect = @import("std").testing.expect;

fn natMult3or5(max: i32) i32 {
    var result: i32 = 0;
    var i: i32 = 0;
    while (i < max): (i+=1) {
        if (@mod(i,3) == 0 or @mod(i,5) == 0) {
            result += i;
        }
    }
    return result;
}

test "sum of natural numbers below 10 that are multiples of 3 or 5" {
    expect(natMult3or5(10) == 23);
}

pub fn main() void {
    std.debug.print("{}\n",.{natMult3or5(@as(i32,1000))});
}
