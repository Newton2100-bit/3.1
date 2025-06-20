const print = @import("std").debug.print;

pub fn main() !void {
    const numbers1 = [_]u8{1,2,3,4,5};
    const numbers2 = [_]u8{6,7,8,9,1};
    var length: [2]i32 = undefined;
    length[0] = numbers1.len;
    length[1] = numbers2.len;
    const numbers3 = numbers1 ++ numbers2;

    print("The length of the reusltant array is {d}\n",.{numbers3.len});
}

