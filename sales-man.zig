const std = @import("std");

fn tsp(graph: [][]const u32) u32 {
    const n = graph.len;
    var dp: [1 << n][n]u32 = undefined;
    for (0..(1 << n)) |i| {
        for (0..n) |j| {
            dp[i][j] = std.math.maxInt(u32);
        }
    }
    dp[1][0] = 0;

    for (0..(1 << n)) |mask| {
        for (0..n) |u| {
            if ((mask & (1 << u)) == 0) continue;
            for (0..n) |v| {
                if ((mask & (1 << v)) == 0 or u == v) continue;
                dp[mask][u] = @min(dp[mask][u], dp[mask ^ (1 << u)][v] + graph[v][u]);
            }
        }
    }

    var min_cost: u32 = std.math.maxInt(u32);
    for (1..n) |u| {
        min_cost = @min(min_cost, dp[(1 << n) - 1][u] + graph[u][0]);
    }
    return min_cost;
}

pub fn main() void {
    const graph = [_][]const u32{
        [_]u32{0, 10, 15, 20},
        [_]u32{10, 0, 35, 25},
        [_]u32{15, 35, 0, 30},
        [_]u32{20, 25, 30, 0},
    };

    std.debug.print("Minimum cost: {}\n", .{tsp(graph)});
}

