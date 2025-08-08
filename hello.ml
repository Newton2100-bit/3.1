
let () =
  print_endline "Hello, world!";
  print_endline "Enter the number of elements:";
  let n = read_int () in
  let arr = Array.make n 0 in
  for i = 0 to n - 1 do
    Printf.printf "Enter element %d: " (i + 1);
    arr.(i) <- read_int ()
  done;
  print_endline "You entered:";
  Array.iter (fun x -> Printf.printf "%d " x) arr;
  print_newline ()
