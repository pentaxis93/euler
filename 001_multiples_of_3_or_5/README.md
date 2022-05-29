# Project Euler Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

## General Strategy

The most straightforward approach to the problem seems to be simply to check each number from 1 to 999 inclusive, adding the number to a running total if it is a multiple of 3 or 5.

Seems almost too simple to comment.

## Code

```python
//- file:src/35er.py
for i in range(1, 1000):
    if i % 3 == 0
```



## File `src/main.rs`

To create code in a certain files, use `file:<path/to/file>` as the block name.
First, we create a file `main.rs` in subfolder `src`:

```rust
//- file:src/main.rs
fn main() {
    println!("Hello Literate Programmer!");
    // ==> More code in main.
}
```

The macro `// ==> More code in main.` pulls the code from the next code block into function `main`.

```rust
//- More code in main
println!("Have fun with yarner!");
```

## File `Cargo.toml`

For a complete Rust project, we also need a `Cargo.toml` file:

```toml
//- file:Cargo.toml
[package]
name = "hello-yarner"
version = "0.1.0"
authors = ["Your Name <you@example.com>"]
edition = "2018"
```

## Output

After running the command `yarner` in the project directory, extracted code can be found in sub-directory `code`, while documentation files are placed in `docs`.
