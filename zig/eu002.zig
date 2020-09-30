const std = @import("std");
const expect = @import("std").testing.expect;

fn fibsum(max: i32) i32 {
    var fib0: i32 = 1;
    var fib1: i32 = 2;
    var fibNext: i32 = 3;
    var result: i32 = 2;
    while (fib1 < max) {
        fibNext = fib0 + fib1;
        if (fibNext < max and @mod(fibNext,2) == 0) {
            result += fibNext;
        }
        fib0 = fib1;
        fib1 = fibNext;
    }
    return result;
}

test "sum of even terms of fibonacci seq below 90" {
    expect(fibsum(90)==44);
}

pub fn main() void {
    std.debug.print("{}\n",.{fibsum(@as(i32,4e6))});
}
