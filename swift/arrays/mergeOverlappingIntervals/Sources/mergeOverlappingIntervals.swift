class Values {
  internal init(input: [[Int]]) {
    self.input = input
    self.input.sort(by: {
      $0[0] < $1[0]
    })
    self.output = [[Int]]()
    self.output.append(self.input[0])
  }

  var input: [[Int]]
  var output: [[Int]]
}

class Program {

  func mergeOverlappingIntervals(_ intervals: [[Int]]) -> [[Int]] {
    // Write your code here.

    if intervals.count == 1 {
      return intervals
    }

    let values: Values = Values(input: intervals)

    // var outputArray: [[Int]] = values.output

    var i: Int = 0

    var nextInterval: [Int] = values.input[1]

    while i < values.input.count - 1 {
      nextInterval = values.input[i + 1]

      while values.output.last![1] >= nextInterval[0] {
        values.output[values.output.count - 1][1] = max(values.output.last![1], nextInterval[1])

        i += 1

        if i >= values.input.count - 1 {
          break
        }

        nextInterval = values.input[i + 1]
      }

      if i >= values.input.count - 1 {
        break
      }

      values.output.append(nextInterval)

      i += 1
    }

    return values.output
  }
}
