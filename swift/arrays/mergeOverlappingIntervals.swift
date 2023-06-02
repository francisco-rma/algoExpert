class Program {

  func mergeOverlappingIntervals(_ intervals: [[Int]]) -> [[Int]] {
    // Write your code here.

    if intervals.count == 1 {
      return intervals
    }

    var mutableIntervals: [[Int]] = intervals

    // var sortedArray: [[Int]] =
    mutableIntervals.sort(by: {
      $0[0] < $1[0]
    })

    var outputArray: [[Int]] = []

    var i: Int = 0

    var currentInterval: [Int] = mutableIntervals[0]

    var nextInterval: [Int] = mutableIntervals[1]

    outputArray.append(currentInterval)

    while i < mutableIntervals.count - 1 {
      nextInterval = mutableIntervals[i + 1]
      currentInterval = outputArray.last!

      while currentInterval[1] >= nextInterval[0] {
        currentInterval[1] = max(currentInterval[1], nextInterval[1])

        nextInterval = mutableIntervals[i + 1]
        i += 1
      }
      outputArray.append(nextInterval)
      i += 1
    }

    return outputArray
  }

  func main() {
    let array = [
      [1, 2],
      [3, 5],
      [4, 7],
      [6, 8],
      [9, 10],
    ]

    let test: [[Int]] = mergeOverlappingIntervals(array)

    print(test)

  }

}

let program: Program = Program()

program.main()
