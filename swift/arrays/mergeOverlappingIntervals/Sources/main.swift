// The Swift Programming Language
// https://docs.swift.org/swift-book

print("Hello, world!")

let array: [[Int]] = [
  [100, 105],
  [1, 104],
]

let program: Program = Program()

let test: [[Int]] = program.mergeOverlappingIntervals(array)

print(test)
