//## Rust
// What does this function do?


// Inputs: `values` is a list of 32bit integers, such as [1,2,3] ("values: &[i32]")
// Returns: A 32bit integer ("-> i32")

fn mysteryFunction(values: &[i32]) -> i32 {
    let mut returnValue = 0;
    for v in values {
        if *v > 0 {
            returnValue += v;
        }
    }
    returnValue
}
